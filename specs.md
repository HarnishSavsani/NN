# EnterpriseMind — Complete Input Data Reference

This document captures **all the underlying sample/seed data** used to power both the
**starter repo backend** (`enterprisemind.zip`) and the **interactive HTML UI demo**
(`EnterpriseMind_UI.html`). Nothing here is "real" enterprise data — it's illustrative
seed content designed to demonstrate every success criterion end-to-end.

---

## 1. Manufacturing — Seed Knowledge (`api/app/seed.py`)

| Source ID | Modality | Content | Roles Allowed |
|---|---|---|---|
| `EQ-CNC-7-HISTORY` | text | "CNC-Machine-7 maintenance history: bearing replaced 2026-05, spindle calibration overdue. Requires certification `cnc_l2` and `machine_required_cert`." | supervisor, technician, viewer |
| `SOP-SAFETY-ZONEA` | pdf | "Zone-A safety SOP: lockout-tagout mandatory. Only technicians with `machine_zone` permission may enter during day shift." | supervisor, technician, viewer |
| `INSPECTION-IMG-441` | image | Caption: "Spindle wear visible on CNC-Machine-7" (parsed via mock Vision LLM) | supervisor, technician |

**Business Rule:** `RULE-WO-ASSIGN` — "Assign only certified, on-shift, zone-permitted technicians." → maps to spec `work_order_assignment`

---

## 2. Healthcare — Seed Knowledge (`api/app/seed.py`)

| Source ID | Modality | Content | Roles Allowed |
|---|---|---|---|
| `PATIENT-DIABETES-GUIDE` | text | "Diabetes care guideline GL-DIABETES-2025: HbA1c targets, medication titration, and mandatory patient consent before plan approval." | clinician, viewer |
| `LAB-REPORT-VOICE-88` | audio | Transcript: "Patient reports improved glucose control this month." (parsed via mock Whisper) | clinician |

**Business Rule:** `RULE-CARE-APPROVE` — "Approve care plans only with consent + licensed clinician + guideline." → maps to spec `care_plan_approval`

---

## 3. Machine-Readable Specs (Spec-Driven Development)

### `specs/work_order_assignment.json` (Manufacturing)
```json
{
  "rule": "technician_assignment",
  "domain": "manufacturing",
  "description": "A technician may be assigned to a machine only if certified, on-shift, and permitted for the machine's zone.",
  "acceptance_criteria": [
    {"field": "technician.certifications", "op": "includes", "value": "machine_required_cert"},
    {"field": "technician.shift", "op": "matches", "value": "work_order_shift"},
    {"field": "technician.zones", "op": "includes", "value": "machine_zone"}
  ],
  "on_fail": "reject_and_explain"
}
```

### `specs/care_plan_approval.json` (Healthcare)
```json
{
  "rule": "care_plan_approval",
  "domain": "healthcare",
  "description": "A care plan may be approved only if patient consent exists, a licensed clinician signs off, and it follows the approved clinical guideline.",
  "acceptance_criteria": [
    {"field": "patient.consent", "op": "equals", "value": true},
    {"field": "clinician.license", "op": "not_empty", "value": null},
    {"field": "plan.guideline_ref", "op": "not_empty", "value": null}
  ],
  "on_fail": "reject_and_explain"
}
```

### Candidate actions the demo agent proposes (in `orchestration/graph.py`)
```json
// Manufacturing candidate
{
  "technician": {
    "certifications": ["cnc_l2", "machine_required_cert"],
    "shift": "work_order_shift",
    "zones": ["zone-A", "machine_zone"],
    "name": "T-Ramesh"
  }
}

// Healthcare candidate
{
  "patient": {"consent": true},
  "clinician": {"license": "MD-4471"},
  "plan": {"guideline_ref": "GL-DIABETES-2025"}
}
```

---

## 4. RBAC Matrix (`governance/rbac.py`)

| Role | document | work_order | assignment | care_plan | patient_record |
|---|---|---|---|---|---|
| **viewer** | * (read) | — | — | — | — |
| **technician** | * (read) | assigned only | — | — | — |
| **supervisor** | * (read) | * | * | — | — |
| **clinician** | * (read) | — | — | * | consented only |
| **admin** | * | * | * | * | * |

`*` = full access. Blank = no access → triggers RBAC denial in the agent flow.

---

## 5. HTML UI Mock Knowledge Base (`enterprisemind_ui.html`)

The standalone UI demo uses a client-side JavaScript `KB` object that mirrors the backend
logic so the whole experience runs offline in a browser with no server.

### Manufacturing domain
```js
quick: [
  "Assign a technician to repair CNC-Machine-7",
  "What is the safety SOP for Zone-A?",
  "Show maintenance history for CNC-Machine-7"
]

citationPool: [
  {type:"text",  name:"EQ-CNC-7-HISTORY",      meta:"Text · v1"},
  {type:"pdf",   name:"SOP-SAFETY-ZONEA",       meta:"PDF · v1"},
  {type:"image", name:"INSPECTION-IMG-441",     meta:"Image · v1"},
  {type:"video", name:"INSPECTION-VIDEO-CNC7",  meta:"Video · 0:42"}
]

multimodalQuick: [
  {kind:"image", label:"Analyze inspection photo"},
  {kind:"video", label:"Review inspection video"}
]

// Validated answer (supervisor/technician):
"Assign technician T-Ramesh to CNC-Machine-7 — certified (cnc_l2), on day shift, zone-A permitted."

// Denied answer (viewer):
"Access denied — your role (viewer) does not have permission to assign work orders."
```

### Healthcare domain
```js
quick: [
  "Approve diabetes care plan for patient",
  "Summarize latest lab results",
  "Who can access this patient's record?"
]

citationPool: [
  {type:"text",  name:"PATIENT-DIABETES-GUIDE", meta:"Text · v1"},
  {type:"audio", name:"LAB-REPORT-VOICE-88",    meta:"Audio · 1:12"},
  {type:"image", name:"PATIENT-SCAN-IMG-12",    meta:"Image · v1"},
  {type:"video", name:"TELECONSULT-CLIP-09",    meta:"Video · 2:05"}
]

multimodalQuick: [
  {kind:"audio", label:"Transcribe patient voice note"},
  {kind:"image", label:"Analyze lab scan image"}
]

// Validated answer (clinician/admin/supervisor):
"Approve care plan following guideline GL-DIABETES-2025 — patient consent confirmed, clinician licensed."

// Denied answer (other roles):
"Access denied — your role does not have clinical authority to approve this care plan."
```

### Attachment → Answer mapping (multimodal simulation)
| Domain | Attachment kind | Simulated agent answer |
|---|---|---|
| Manufacturing | image | "Analyzed attached inspection photo — visible spindle wear consistent with logged maintenance history; recommend replacement within 2 shifts." |
| Manufacturing | audio | "Transcribed attached voice note — technician reports unusual vibration on CNC-Machine-7 spindle, matches prior sensor alerts." |
| Manufacturing | video | "Analyzed attached inspection video — confirms coolant leak near the zone-A guard rail, flagged for safety review." |
| Manufacturing | doc | "Extracted key clauses from attached document — cross-referenced against SOP-SAFETY-ZONEA for compliance." |
| Healthcare | image | "Analyzed attached lab/diagnostic image — glucose and lipid markers trending above optimal range, consistent with care-plan notes." |
| Healthcare | audio | "Transcribed attached voice note — patient reports improved glucose control this month, no adverse symptoms." |
| Healthcare | video | "Analyzed attached teleconsult clip — clinician confirms medication adherence and schedules follow-up in 30 days." |
| Healthcare | doc | "Extracted key fields from attached document — cross-referenced against guideline GL-DIABETES-2025." |

### Dashboard stat tiles (illustrative, hardcoded for demo realism)
| Stat | Value |
|---|---|
| Avg. context retrieval time | 1.4s (▼62%) |
| Chunks in unified memory | 2,481 (▲8%) |
| Spec-validated decisions | 96.2% (▲3%) |
| Unresolved compliance flags | 0 (stable) |
| Text & PDF chunks | 1,142 |
| Images ingested | 618 |
| Audio transcripts | 347 |
| Video segments | 374 |

### Seeded audit trail (pre-populated on page load)
| Query | Role | Result | Rationale |
|---|---|---|---|
| Assign a technician to repair CNC-Machine-7 | supervisor | ALLOWED | Spec satisfied; Responsible-AI clean. |
| Assign a technician to repair CNC-Machine-7 | viewer | BLOCKED | RBAC: viewer lacks assignment/* scope. |
| Approve diabetes care plan for patient | clinician | ALLOWED | Spec satisfied; consent & license confirmed. |

### Sample images used for citation thumbnails
Two AI-generated stand-in images represent the "Image" modality in citations and attachments:
- **Manufacturing:** close-up of a CNC machine spindle showing wear (used for `INSPECTION-IMG-441` and image attachments)
- **Healthcare:** clinical tablet showing a lab report / diagnostic chart (used for `PATIENT-SCAN-IMG-12` and image attachments)

---

## 6. How Backend and UI Data Relate

The HTML UI's mock `KB` object was deliberately written to **mirror** the FastAPI backend's
`seed.py` + `specs/*.json` + `rbac.py` logic 1:1, so:
- Same source IDs (`EQ-CNC-7-HISTORY`, `PATIENT-DIABETES-GUIDE`, etc.)
- Same spec-driven pass/fail criteria language
- Same RBAC denial behavior (viewer blocked on assignment; non-clinical roles blocked on care plans)

This means the UI is a **faithful offline simulation** of what the real API (`/api/agent/run`)
returns — swapping the UI's JS `resolve()` calls for real `fetch()` calls to the backend would
require no changes to the citation/rationale/audit rendering logic.
