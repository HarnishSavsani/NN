# 🚀 Skills & Commands Reference Guide

> **Your complete playbook for building enterprise-grade projects with GSD + Superpowers**

---

## 📑 Table of Contents

- [🔧 Superpowers Commands](#-superpowers-commands)
- [⚡ GSD Commands](#-gsd-commands)
  - [🏗️ Project Initialization](#️-project-initialization)
  - [📐 Phase Planning](#-phase-planning)
  - [▶️ Execution](#️-execution)
  - [🧭 Smart Router & Quick Modes](#-smart-router--quick-modes)
  - [🗺️ Roadmap Management](#️-roadmap-management)
  - [🏁 Milestone Management](#-milestone-management)
  - [📊 Progress & Sessions](#-progress--sessions)
  - [🐛 Debugging](#-debugging)
  - [🧪 Spiking & Sketching](#-spiking--sketching)
  - [💡 Capture Ideas & Todos](#-capture-ideas--todos)
  - [✅ UAT, Ship & Review](#-uat-ship--review)
  - [🛡️ Quality, Security & Auditing](#️-quality-security--auditing)
  - [🔩 Diagnostics & Maintenance](#-diagnostics--maintenance)
  - [🧠 Knowledge & Context](#-knowledge--context)
  - [⚙️ Configuration](#️-configuration)
  - [🔀 Workflow & Orchestration](#-workflow--orchestration)
  - [📥 Import & Ingest](#-import--ingest)
  - [📬 Repository Integration](#-repository-integration)
  - [🔀 Namespace Routers](#-namespace-routers)
- [🗺️ Workflow & Lifecycle Guide](#️-workflow--lifecycle-guide)
  - [Path A — GSD Only](#path-a--gsd-only-enterprise-lifecycle)
  - [Path B — Superpowers Only](#path-b--superpowers-only-lifecycle)
  - [Path C — Combined (Recommended)](#path-c--combined-gsd--superpowers-recommended)

---

## 🔧 Superpowers Commands

> Process-level skills that govern **how** you work — brainstorming, debugging, planning, reviewing, shipping.

| Command | Description |
|---------|-------------|
| `/superpowers:brainstorming` | 🧠 Explore user intent, requirements, and design through collaborative dialogue **before** any code is written. Use before creating features or modifying behavior. |
| `/superpowers:writing-plans` | 📝 Produce a comprehensive implementation plan with file-level detail, code pointers, testing guidance, and bite-sized tasks. Follows DRY, YAGNI, TDD, and frequent-commit principles. |
| `/superpowers:executing-plans` | ▶️ Load a written plan, review it critically, execute all tasks with review checkpoints, and report when complete. |
| `/superpowers:subagent-driven-development` | 🤖 Dispatch a fresh implementer subagent per task, run spec compliance + code quality review after each, and a broad whole-branch review at the end. |
| `/superpowers:dispatching-parallel-agents` | 🔀 Delegate 2+ independent tasks to specialized subagents with precisely crafted, isolated context for maximum parallelism. |
| `/superpowers:test-driven-development` | 🧪 Enforce red-green-refactor: write the test first, watch it fail, then write minimal code to pass. Always before implementation. |
| `/superpowers:systematic-debugging` | 🔍 Find the **root cause** before proposing fixes. Uses evidence → hypothesis → test cycle. Symptom fixes are treated as failure. |
| `/superpowers:requesting-code-review` | 📤 Dispatch a code reviewer subagent with crafted context to catch issues before they cascade. Use before merging. |
| `/superpowers:receiving-code-review` | 📥 Enforce technical rigor when receiving review feedback — verify before blindly implementing suggestions. |
| `/superpowers:verification-before-completion` | ✅ Require running verification commands and confirming actual output before claiming work is done. Evidence before assertions. |
| `/superpowers:finishing-a-development-branch` | 🏁 Guide the integration decision: verify tests, detect environment, present options (merge, PR, squash), execute, and clean up. |
| `/superpowers:using-git-worktrees` | 🌳 Start feature work in isolation using git worktrees. Prefers platform-native tools; falls back to `git worktree` commands. |
| `/superpowers:writing-skills` | ✍️ Create, edit, and verify custom skills using TDD principles applied to process documentation. |
| `/superpowers:using-superpowers` | 🎯 Bootstrapper — establishes skill discovery and requires skill invocation before any response. Runs at conversation start. |

---

## ⚡ GSD Commands

### 🏗️ Project Initialization

| Command | Description |
|---------|-------------|
| `/gsd:new-project` | 🆕 Initialize a new project: deep questioning → optional domain research (4 parallel agents) → requirements → roadmap with phase breakdown. Creates all `.planning/` artifacts. |
| `/gsd:map-codebase [--fast] [--focus] [--query]` | 🗺️ Map an existing codebase for brownfield projects. Creates 7 focused documents covering stack, architecture, conventions, testing, integrations, and concerns. |

### 📐 Phase Planning

| Command | Description |
|---------|-------------|
| `/gsd:discuss-phase <N>` | 💬 Articulate your vision for a phase before planning. Creates CONTEXT.md. Flags: `--chain`, `--analyze`, `--power`, `--assumptions`, `--batch`. |
| `/gsd:spec-phase <N> [--auto] [--text]` | 📋 Clarify **what** a phase delivers with ambiguity scoring. Produces SPEC.md before discuss-phase. |
| `/gsd:plan-phase <N>` | 📐 Create a detailed execution plan with task breakdown, dependencies, and verification criteria. Flags: `--research`, `--tdd`, `--mvp`, `--prd`, `--ingest`. |
| `/gsd:mvp-phase <N> [--force]` | 🎯 Plan a phase as a vertical MVP slice using user-story prompts (As a / I want to / So that) with SPIDR splitting. |
| `/gsd:ai-integration-phase [N]` | 🤖 Generate an AI-SPEC.md design contract for phases involving AI/LLM systems. |
| `/gsd:ui-phase [N]` | 🎨 Generate a UI-SPEC.md design contract for frontend phases. |
| `/gsd:ultraplan-phase [N]` | ☁️ *[BETA]* Offload plan-phase to Claude Code's ultraplan cloud; review in browser and import back. |
| `/gsd:plan-review-convergence <N>` | 🔄 Cross-AI plan convergence loop — replan with review feedback until no HIGH concerns remain. Supports `--gemini`, `--claude`, `--codex`, `--all`. |

### ▶️ Execution

| Command | Description |
|---------|-------------|
| `/gsd:execute-phase <N>` | 🚀 Execute all plans in a phase. Groups by wave, runs waves sequentially, plans within a wave in parallel. Verifies goal after. Flags: `--wave N`, `--gaps-only`, `--tdd`. |
| `/gsd:autonomous [--from N] [--to N]` | 🤖 Run all remaining phases autonomously: discuss → plan → execute per phase, end-to-end. `--interactive` for approval checkpoints. |

### 🧭 Smart Router & Quick Modes

| Command | Description |
|---------|-------------|
| `/gsd:progress --do "<text>"` | 🧭 Route freeform text to the right GSD command automatically. Smart dispatcher — never does the work itself. |
| `/gsd:quick [--full] [--validate]` | ⚡ Execute small ad-hoc tasks with GSD guarantees but a shorter path. Tasks live in `.planning/quick/`. |
| `/gsd:fast [description]` | 💨 Execute a trivial task inline — no subagents, no planning files. For tasks with ≤ 3 file edits. |

### 🗺️ Roadmap Management

| Command | Description |
|---------|-------------|
| `/gsd:phase <description>` | ➕ Add a new phase to the end of the current milestone. |
| `/gsd:phase --insert <after> <desc>` | 📌 Insert urgent work as a decimal phase between existing phases (e.g., 7.1). |
| `/gsd:phase --remove <N>` | ❌ Remove a future phase and renumber subsequent phases. |
| `/gsd:phase --edit <N> [--force]` | ✏️ Edit any field of an existing roadmap phase in place. |

### 🏁 Milestone Management

| Command | Description |
|---------|-------------|
| `/gsd:new-milestone <name>` | 🎯 Start a new milestone — deep questioning, optional research, requirements, roadmap. For brownfield projects. |
| `/gsd:complete-milestone <ver>` | 🏆 Archive completed milestone, create MILESTONES.md entry, git tag, and prepare workspace for next version. |
| `/gsd:milestone-summary [ver]` | 📄 Generate comprehensive project summary from milestone artifacts for team onboarding and review. |

### 📊 Progress & Sessions

| Command | Description |
|---------|-------------|
| `/gsd:progress` | 📊 Visual progress bar, recent work, current position, key decisions, open issues. `--next` to execute next plan. |
| `/gsd:resume-work` | 🔄 Resume work from a previous session with full context restoration from STATE.md. |
| `/gsd:pause-work [--report]` | ⏸️ Create context handoff when pausing. Creates `.continue-here` and updates STATE.md. |
| `/gsd:stats` | 📈 Display project statistics: phases, plans, requirements, git metrics, and timeline. |

### 🐛 Debugging

| Command | Description |
|---------|-------------|
| `/gsd:debug [desc] [--diagnose]` | 🐛 Systematic debugging with persistent state across context resets. Scientific method. Survives `/clear`. |
| `/gsd:forensics [problem]` | 🔬 Post-mortem investigation for failed GSD workflows — diagnoses what went wrong. |

### 🧪 Spiking & Sketching

| Command | Description |
|---------|-------------|
| `/gsd:spike [idea] [--quick]` | 🧪 Rapidly spike an idea with throwaway experiments. 2-5 focused experiments, verdicts: VALIDATED/INVALIDATED/PARTIAL. |
| `/gsd:spike --wrap-up` | 📦 Package spike findings into a persistent project skill. |
| `/gsd:sketch [idea] [--quick]` | 🎨 Rapidly sketch UI ideas as throwaway HTML mockups with multi-variant exploration (2-3 tabbed variants). |
| `/gsd:sketch --wrap-up` | 📦 Package sketch design findings into a persistent project skill. |
| `/gsd:explore` | 💭 Socratic ideation and idea routing. Think through ideas before committing to plans. |

### 💡 Capture Ideas & Todos

| Command | Description |
|---------|-------------|
| `/gsd:capture [desc]` | 💡 Capture an idea or task as a structured todo. Checks for duplicates, updates STATE.md. |
| `/gsd:capture --note <text>` | 📝 Zero-friction note capture — timestamped note to `.planning/notes/`. |
| `/gsd:capture --list [area]` | 📋 List pending todos and select one to work on. |
| `/gsd:capture --seed [idea]` | 🌱 Capture a forward-looking idea with trigger conditions for automatic surfacing. |
| `/gsd:capture --backlog [desc]` | 🅿️ Add an idea to the backlog parking lot (999.x in ROADMAP.md). |
| `/gsd:review-backlog` | 📦 Review and promote backlog items to the active milestone. |

### ✅ UAT, Ship & Review

| Command | Description |
|---------|-------------|
| `/gsd:verify-work [phase]` | ✅ Validate features through conversational UAT. Presents tests one-at-a-time, diagnoses failures. |
| `/gsd:ship [phase]` | 🚢 Push branch, create PR with auto-generated body from artifacts, optionally request code review. |
| `/gsd:review --phase N` | 🔍 Cross-AI peer review — invoke external AI CLIs to independently review plans. Supports `--gemini`, `--claude`, `--codex`, `--all`. |
| `/gsd:pr-branch [target]` | 🌿 Create a clean PR branch by cherry-picking only code commits (filtering `.planning/`). |

### 🛡️ Quality, Security & Auditing

| Command | Description |
|---------|-------------|
| `/gsd:code-review <phase> [--fix]` | 🔎 Review source files for bugs, security issues, code quality. `--fix` applies findings automatically. |
| `/gsd:secure-phase [phase]` | 🔒 Verify threat mitigations for a completed phase. Produces SECURITY.md. |
| `/gsd:validate-phase [phase]` | 📏 Audit and fill Nyquist validation gaps for a completed phase. |
| `/gsd:ui-review [phase]` | 🎨 Retroactive 6-pillar visual audit of frontend code. Produces scored UI-REVIEW.md. |
| `/gsd:eval-review [phase]` | 🤖 Audit AI phase evaluation coverage. Produces EVAL-REVIEW.md remediation plan. |
| `/gsd:audit-fix --source <src>` | 🔧 Autonomous audit-to-fix pipeline: find → classify → fix → test → commit. Flags: `--severity`, `--max`, `--dry-run`. |
| `/gsd:add-tests <phase>` | 🧪 Generate tests for a completed phase based on UAT criteria and implementation. |
| `/gsd:audit-uat` | 📋 Cross-phase audit of all outstanding UAT items. Produces prioritized human test plan. |
| `/gsd:audit-milestone [ver]` | 🏗️ Audit milestone completion against original intent. Produces MILESTONE-AUDIT.md with gaps and tech debt. |

### 🔩 Diagnostics & Maintenance

| Command | Description |
|---------|-------------|
| `/gsd:health [--repair] [--context]` | 🩺 Diagnose planning directory health and optionally repair issues. |
| `/gsd:undo --last N \| --phase NN` | ⏪ Safe git revert. Roll back phase or plan commits with dependency checks. |
| `/gsd:docs-update [--force]` | 📚 Generate or update project documentation verified against the codebase. |
| `/gsd:extract-learnings <phase>` | 🎓 Extract decisions, lessons, patterns, and surprises from completed phase artifacts. |
| `/gsd:cleanup` | 🧹 Archive phase directories from completed milestones to `.planning/milestones/`. |

### 🧠 Knowledge & Context

| Command | Description |
|---------|-------------|
| `/gsd:graphify [build\|query\|status]` | 🕸️ Build, query, and inspect the project knowledge graph in `.planning/graphs/`. |
| `/gsd:thread [list\|close\|status]` | 🧵 Manage persistent context threads for cross-session work. |
| `/gsd:profile-user [--questionnaire]` | 👤 Generate developer behavioral profile and Claude-discoverable artifacts. |

### ⚙️ Configuration

| Command | Description |
|---------|-------------|
| `/gsd:settings` | ⚙️ Configure workflow toggles and model profile interactively. |
| `/gsd:config [--profile\|--advanced]` | 🔧 Power-user tuning: model profile quick-switch, integrations, advanced settings. |
| `/gsd:surface [list\|enable\|disable]` | 👁️ Toggle which skills are surfaced. Apply a profile or disable/enable skill clusters. |
| `/gsd:update [--sync] [--reapply]` | 🔄 Update GSD to latest version with changelog preview. |
| `/gsd:help` | ❓ Show the full command reference. |

### 🔀 Workflow & Orchestration

| Command | Description |
|---------|-------------|
| `/gsd:manager [--analyze-deps]` | 🎛️ Interactive command center for managing multiple phases from one terminal. |
| `/gsd:workspace [--new\|--list\|--remove]` | 🏢 Manage isolated workspace environments. |
| `/gsd:workstreams` | 🔀 Manage parallel workstreams: create, switch, track progress, complete, resume. |

### 📥 Import & Ingest

| Command | Description |
|---------|-------------|
| `/gsd:import --from <path>` | 📥 Ingest external plans with conflict detection. `--from-gsd2` for GSD v2 → v1 migration. |
| `/gsd:ingest-docs [path]` | 📄 Bootstrap `.planning/` from existing ADRs, PRDs, SPECs. Flags: `--mode`, `--manifest`, `--resolve`. |

### 📬 Repository Integration

| Command | Description |
|---------|-------------|
| `/gsd:inbox [--issues\|--prs\|--label]` | 📬 Triage open GitHub issues and PRs against project templates and contribution guidelines. |

### 🔀 Namespace Routers

> Meta-skills that route you to the right sub-command cluster.

| Router | Routes To |
|--------|-----------|
| `/gsd-context` | 🗺️ `map`, `graphify`, `docs`, `learnings` |
| `/gsd-ideate` | 💭 `explore`, `sketch`, `spike`, `spec`, `capture` |
| `/gsd-manage` | ⚙️ `workstreams`, `thread`, `update`, `ship`, `inbox` |
| `/gsd-project` | 🏗️ `milestones`, `audits`, `summary` |
| `/gsd-quality` | 🛡️ `code-review`, `debug`, `audit`, `security`, `eval`, `ui` |
| `/gsd-workflow` | 🔄 `discuss`, `plan`, `execute`, `verify`, `phase`, `progress` |

---

## 🗺️ Workflow & Lifecycle Guide

> How to take a project from **zero → production-ready** with enterprise-grade quality.

---

### Path A — GSD Only (Enterprise Lifecycle)

> Best for: Structured, phased delivery with planning artifacts, auditing, and traceability.

```
📦 PROJECT LIFECYCLE WITH GSD
═══════════════════════════════

  ┌─────────────────────────────────────────────────────────────┐
  │  PHASE 0: PROJECT INIT                                      │
  │                                                             │
  │  /gsd:new-project          ← Deep questioning + roadmap     │
  │  /gsd:map-codebase         ← If brownfield (existing code)  │
  │  /gsd:settings             ← Configure model + toggles      │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │  PHASE N: PLAN (repeat per phase)                           │
  │                                                             │
  │  /gsd:spec-phase N         ← Clarify WHAT (ambiguity score) │
  │  /gsd:discuss-phase N      ← Articulate vision + context    │
  │  /gsd:plan-phase N         ← Detailed task plan + deps      │
  │  /gsd:plan-review-conv. N  ← Cross-AI convergence (opt.)    │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │  PHASE N: BUILD                                             │
  │                                                             │
  │  /gsd:execute-phase N      ← Run all plans (wave-parallel)  │
  │  /gsd:debug                ← If something breaks            │
  │  /gsd:progress             ← Track where you are            │
  │  /gsd:pause-work           ← Context handoff if stopping    │
  │  /gsd:resume-work          ← Pick up next session           │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │  PHASE N: VERIFY & HARDEN                                  │
  │                                                             │
  │  /gsd:verify-work N        ← Conversational UAT             │
  │  /gsd:code-review N        ← Bug + quality review           │
  │  /gsd:secure-phase N       ← Security threat verification   │
  │  /gsd:validate-phase N     ← Nyquist validation gaps        │
  │  /gsd:add-tests N          ← Generate missing tests         │
  │  /gsd:ui-review N          ← Frontend visual audit (if UI)  │
  │  /gsd:eval-review N        ← AI eval coverage (if AI)       │
  │  /gsd:audit-fix            ← Auto-fix audit findings        │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │  PHASE N: SHIP                                              │
  │                                                             │
  │  /gsd:docs-update          ← Generate/update documentation  │
  │  /gsd:ship N               ← Create PR from phase work      │
  │  /gsd:extract-learnings N  ← Capture decisions + patterns   │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
                          (repeat for each phase)
                                 │
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │  MILESTONE COMPLETE                                         │
  │                                                             │
  │  /gsd:audit-milestone      ← Final gap analysis             │
  │  /gsd:audit-uat            ← Cross-phase UAT audit          │
  │  /gsd:complete-milestone   ← Archive + git tag + next ver   │
  │  /gsd:milestone-summary    ← Onboarding-ready summary       │
  │  /gsd:cleanup              ← Archive phase directories      │
  └─────────────────────────────────────────────────────────────┘
```

**🤖 Autopilot shortcut:** `/gsd:autonomous --from 1 --to 10` runs discuss → plan → execute for every phase hands-free.

---

### Path B — Superpowers Only Lifecycle

> Best for: Lightweight projects, solo dev, or when you want process rigor without `.planning/` artifacts.

```
🔧 PROJECT LIFECYCLE WITH SUPERPOWERS
═══════════════════════════════════════

  ┌─────────────────────────────────────────────────────────────┐
  │  STEP 1: BRAINSTORM                                         │
  │                                                             │
  │  /superpowers:brainstorming                                 │
  │  ↳ Explore requirements, constraints, design collaboratively│
  │  ↳ Clarify intent before touching any code                  │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │  STEP 2: PLAN                                               │
  │                                                             │
  │  /superpowers:writing-plans                                 │
  │  ↳ Comprehensive plan: file-level detail, code pointers,    │
  │    testing guidance, bite-sized tasks                        │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │  STEP 3: IMPLEMENT (choose one)                             │
  │                                                             │
  │  Option A: /superpowers:executing-plans                     │
  │  ↳ Execute plan sequentially with review checkpoints        │
  │                                                             │
  │  Option B: /superpowers:subagent-driven-development         │
  │  ↳ Dispatch subagent per task + quality review after each   │
  │                                                             │
  │  Option C: /superpowers:dispatching-parallel-agents         │
  │  ↳ Fan out independent tasks to parallel subagents          │
  │                                                             │
  │  Always use:                                                │
  │  /superpowers:test-driven-development                       │
  │  ↳ Red → Green → Refactor for every feature                 │
  │                                                             │
  │  /superpowers:using-git-worktrees                           │
  │  ↳ Isolate feature work in worktrees                        │
  │                                                             │
  │  If bugs: /superpowers:systematic-debugging                 │
  │  ↳ Root-cause analysis before any fix attempt               │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │  STEP 4: REVIEW & VERIFY                                    │
  │                                                             │
  │  /superpowers:requesting-code-review                        │
  │  ↳ Dispatch reviewer subagent to catch issues               │
  │                                                             │
  │  /superpowers:receiving-code-review                         │
  │  ↳ Apply feedback with technical rigor                      │
  │                                                             │
  │  /superpowers:verification-before-completion                │
  │  ↳ Run verification, confirm output. Evidence > assertions  │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │  STEP 5: SHIP                                               │
  │                                                             │
  │  /superpowers:finishing-a-development-branch                 │
  │  ↳ Verify tests → merge/PR/squash → clean up               │
  └─────────────────────────────────────────────────────────────┘
```

---

### Path C — Combined GSD + Superpowers (⭐ Recommended)

> Best for: **Maximum quality.** GSD provides the structure, roadmap, and artifacts. Superpowers provides the process discipline at every step.

```
🏆 ENTERPRISE LIFECYCLE: GSD + SUPERPOWERS COMBINED
═════════════════════════════════════════════════════

  ╔═════════════════════════════════════════════════════════════╗
  ║  🌟  PHASE 0: PROJECT INITIALIZATION                       ║
  ╚═════════════════════════════════════════════════════════════╝

  1. /superpowers:brainstorming        ← Explore the idea first
  2. /gsd:new-project                  ← Deep questioning + roadmap
  3. /gsd:map-codebase                 ← If existing code (brownfield)
  4. /gsd:settings                     ← Configure model + toggles


  ╔═════════════════════════════════════════════════════════════╗
  ║  📐  FOR EACH PHASE: PLAN                                  ║
  ╚═════════════════════════════════════════════════════════════╝

  5.  /gsd:spec-phase N                ← Clarify WHAT with scoring
  6.  /gsd:discuss-phase N             ← Vision + boundaries
  7.  /gsd:spike [idea]                ← Validate unknowns first
  8.  /superpowers:writing-plans       ← (optional) detailed sub-plan
  9.  /gsd:plan-phase N --tdd          ← Full plan with TDD flag
  10. /gsd:plan-review-convergence N   ← Cross-AI sanity check


  ╔═════════════════════════════════════════════════════════════╗
  ║  ▶️  FOR EACH PHASE: BUILD                                  ║
  ╚═════════════════════════════════════════════════════════════╝

  11. /superpowers:using-git-worktrees ← Isolate in worktree
  12. /superpowers:test-driven-development ← TDD for every feature
  13. /gsd:execute-phase N             ← Wave-parallel execution

      ↳ During build:
        • /superpowers:systematic-debugging   ← If bugs appear
        • /gsd:debug                          ← Persistent debug state
        • /gsd:capture --note "..."           ← Quick notes
        • /gsd:progress                       ← Track status
        • /gsd:pause-work / resume-work       ← Session management


  ╔═════════════════════════════════════════════════════════════╗
  ║  🛡️  FOR EACH PHASE: VERIFY & HARDEN                       ║
  ╚═════════════════════════════════════════════════════════════╝

  14. /superpowers:verification-before-completion ← Evidence first
  15. /gsd:verify-work N               ← Conversational UAT
  16. /superpowers:requesting-code-review ← Subagent code review
  17. /gsd:code-review N               ← Structured review + REVIEW.md
  18. /gsd:secure-phase N              ← Security audit
  19. /gsd:validate-phase N            ← Validation gaps
  20. /gsd:add-tests N                 ← Fill test coverage
  21. /gsd:ui-review N                 ← Frontend audit (if applicable)
  22. /gsd:eval-review N               ← AI eval audit (if applicable)
  23. /gsd:audit-fix --source audit-uat ← Auto-fix findings


  ╔═════════════════════════════════════════════════════════════╗
  ║  🚢  FOR EACH PHASE: SHIP                                  ║
  ╚═════════════════════════════════════════════════════════════╝

  24. /gsd:docs-update                 ← Generate documentation
  25. /superpowers:finishing-a-development-branch ← Merge decision
  26. /gsd:ship N                      ← Create PR with full context
  27. /gsd:extract-learnings N         ← Capture patterns + decisions


  ╔═════════════════════════════════════════════════════════════╗
  ║  🏆  MILESTONE COMPLETE                                     ║
  ╚═════════════════════════════════════════════════════════════╝

  28. /gsd:audit-milestone             ← Gap analysis vs intent
  29. /gsd:audit-uat                   ← Cross-phase UAT audit
  30. /gsd:complete-milestone v1.0     ← Archive + tag + next ver
  31. /gsd:milestone-summary           ← Team onboarding summary
  32. /gsd:cleanup                     ← Archive old phase dirs
```

---

## 🎯 Quick Reference: When to Use What

| Situation | Use This |
|-----------|----------|
| 🆕 Starting from scratch | `/gsd:new-project` → roadmap first |
| 💡 Have a vague idea | `/superpowers:brainstorming` → then `/gsd:explore` |
| 🏗️ Existing codebase | `/gsd:map-codebase` → then `/gsd:new-milestone` |
| 🐛 Something is broken | `/superpowers:systematic-debugging` → then `/gsd:debug` |
| ⚡ Tiny change (≤ 3 files) | `/gsd:fast` |
| 🔥 Small task, some rigor | `/gsd:quick` |
| 🏭 Full enterprise phase | `/gsd:discuss-phase` → `plan-phase` → `execute-phase` |
| 🤖 Hands-free everything | `/gsd:autonomous` |
| 📋 Capture a stray thought | `/gsd:capture` |
| 🔒 Security-sensitive phase | `/gsd:secure-phase` after execution |
| 🧪 Unsure if idea works | `/gsd:spike` |
| 🎨 UI prototype needed | `/gsd:sketch` |
| 📊 Where am I? | `/gsd:progress` |
| 🚢 Ready to ship | `/gsd:ship` → `/superpowers:finishing-a-development-branch` |

---

## 💎 Pro Tips

| Tip | Why |
|-----|-----|
| 🧠 Always brainstorm before planning | Prevents building the wrong thing |
| 🧪 Always `--tdd` on plan-phase | Tests are written alongside code, not after |
| 🔄 Use `/gsd:pause-work` before closing terminal | STATE.md lets you resume perfectly next session |
| 🔍 Run `/gsd:code-review --fix` after execution | Catches bugs before UAT finds them |
| 📝 `/gsd:capture --note` for fleeting ideas | They surface automatically during milestones |
| 🤖 `/gsd:autonomous` for well-scoped milestones | Full hands-free discuss → plan → execute loop |
| 🔀 Use namespace routers when unsure | `/gsd-quality` shows all quality commands |
| 🏗️ `/gsd:graphify build` after major phases | Knowledge graph makes context queries instant |

---

> 📌 **Run `/gsd:help` or `/superpowers:using-superpowers` anytime to refresh your memory.**

*Generated for Hackathon Machine Setup — Happy building! 🚀*
