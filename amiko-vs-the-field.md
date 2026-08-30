# Amiko vs. the Field

**Issuer-side payment dispute management platforms — vendor landscape, August 2026**

Rivero's Amiko automates cardholder disputes for issuers with a 24/7 virtual agent and scheme-certified case management. Seven platforms solve the same problem in materially different ways — and three adjacent categories get mistaken for it.

- **Scope:** issuer-side platforms comparable to Amiko
- **Compared:** 7 alternatives across 8 criteria
- **Basis:** vendor-published claims, unverified
- **Companion artifact:** [Amiko vs. the Field](https://claude.ai/code/artifact/ecb2a9ad-128f-468a-a9a3-ed627a94c9e4)

---

## How to read the AI column

Every vendor in this market now says "AI." The distinction that matters to a buyer is whether software closes cases on its own, merely speeds up a human, or just moves paperwork.

| Level | What it means |
| --- | --- |
| **Agentic** | A named agent takes autonomous action on cases — intake, decisioning, filing — with humans on exception handling. |
| **Assisted** | AI summarizes, recommends and pre-fills. A human still advances every case. |
| **Rules / RPA** | Deterministic automation: rules engines, scripted bots, deadline tracking. Reliable, not adaptive. |

---

## The matrix — capability

| Platform | Delivery model | AI depth | Cardholder intake | Scheme connectivity |
| --- | --- | --- | --- | --- |
| **Amiko** *(Rivero, CH)* | Fully managed SaaS; compliance releases included | **Agentic** — 24/7 virtual agent resolves, collects or deflects claims | Virtual agent inside the bank's own app or portal | Certified direct with Visa (VROL) and Mastercard (Mastercom); Ethoca, Verifi, MC Fraud & Loss DB, Visa FRS |
| **QFD** *(Quavo, US)* | Cloud SaaS, bi-annual releases at no client effort | **Agentic** — "Aria" analyst; claims ~50% of claim volume handled independently | Dynamic intake with eligibility filtering, agent and digital channels | VROL, Mastercom, Verifi, Ethoca; Visa, Mastercard, Pulse, PLUS |
| **Smart Dispute** *(Pega, US)* | Licensed enterprise platform, cloud or client-managed | **Assisted** — agentic intake plus guided handling, humans in the loop | Branch, IVR, contact centre, digital and API, with context-preserving channel switching | Visa, Mastercard **and** Amex; VROL/Mastercom, Ethoca/Verifi; Reg E & Z, UK Section 75 |
| **Dispute Resolution / CBK** *(FIS, US)* | Hosted or on-premise; FIS runs PCI and ops on the hosted tier | **Rules / RPA** — robotic automation over repetitive claim tasks | Inherited from existing FIS channels | Visa Claim Resolution, Mastercom |
| **Automated Dispute Manager** *(ACI Worldwide, US)* | Module of the fraud platform; issuer and acquirer in one system | **Rules / RPA** — configurable workflow and case automation | Multiple customer channels; merchant portals on the acquiring side | All major schemes, rules kept current |
| **CentrixDQS** *(Q2, US)* | Module inside Q2 digital banking | **Rules / RPA** — workflow and tracking within the platform | Q2 digital banking channels | Standard card scheme processes via Q2 |
| **Issuer Edition** *(Chargebacks911, US)* | Managed service — vendor analysts work your cases | **Assisted** — AI tooling behind a human analyst team | Handled by the service, not by your software | Scheme representment handled on your behalf |
| **Financial Compliance** *(Verint, US)* | Contact-centre tooling | **Rules / RPA** — call recording, agent workflow, case creation | Contact centre only — its actual strength | None — no network representment |

## The matrix — fit

| Platform | Beyond cards | Integration burden | Where it fits | Watch-outs |
| --- | --- | --- | --- | --- |
| **Amiko** | Cards only | **Low** — connects to schemes directly, not to your processing stack | European banks, BaaS providers and fintech issuers wanting cardholder self-service | Visa/Mastercard only; European reference base; no published implementation timeline |
| **QFD** | ACH, Wire, Zelle, RTP | **Medium** — connectors for Jack Henry, Fiserv, FIS, Keystone, TSYS | US issuers, credit unions and processors with Reg E exposure and multi-rail disputes | Automation figures are vendor-published; centre of gravity is US regulation |
| **Smart Dispute** | Multi-payment-type | **High** — reported 6–12 month implementations | Large global banks with many channels, rails and regulatory regimes | Longest time-to-value; needs a configuration practice you must staff |
| **Dispute Resolution / CBK** | Claims beyond cards | **Low** if you run FIS core; otherwise weak | Existing FIS core shops valuing native data over automation depth | Feature depth varies by core version; positioned as reliable, not innovative |
| **Automated Dispute Manager** | Scheme-wide | **Medium** — lowest if ACI fraud is already in place | Institutions that both issue and acquire, or where fraud drives most disputes | Value drops sharply without the ACI fraud platform |
| **CentrixDQS** | Card-centric | **Very low** inside Q2; no reason to buy outside it | Banks already standardised on Q2 avoiding an integration project | Limited value outside Q2; single secondary source — confirm directly |
| **Issuer Edition** | Cards | **Minimal** — you outsource rather than deploy | Smaller issuers without the volume to justify a platform | An outsourcing decision, not a software one |
| **Financial Compliance** | n/a | **Low**, but it sits alongside a real dispute platform | Intake capture and audit trail | Not a substitute for a dispute engine |

---

## What each one is actually selling

### Amiko — Rivero

Rivero's bet is that the cardholder conversation is the bottleneck, not the back office. The virtual agent handles the claim in the banking app, then feeds a case-management layer that runs the full Visa and Mastercard lifecycle through arbitration. Certified directly with both schemes, so it bypasses your processor.

- **Proof:** Cembra, SIX, Viseca, Advanzia; PCI DSS and ISO 27001
- **Watch:** Visa/Mastercard only; European reference base; no published implementation timeline

### Quavo QFD

The most direct functional rival. Quavo automates the whole US issuer workflow — provisional credit, GL accounting, card reissue, chargeback filing, correspondence — and its Aria analyst claims to close roughly half of claim volume without a human. It also covers ACH, Zelle, RTP and wire, which card-only platforms do not.

- **Proof:** core connectors across Jack Henry, Fiserv, FIS, TSYS; Snowflake partnership
- **Watch:** automation figures are vendor-published; centre of gravity is US regulation

### Pega Smart Dispute

Sold to institutions whose complexity is the problem: many intake channels, several rails, and Reg E, Reg Z and Section 75 in the same estate. The rules engine is the deepest in the set, and Amex is covered where most rivals stop at Visa and Mastercard. Nationwide's published case cut resolution from 15 days to 2.

- **Proof:** 86% resolution-time improvement claimed; no per-token AI fees
- **Watch:** 6–12 month implementations and a configuration practice you must staff

### FIS Dispute Resolution / CBK

An incumbency play. Native access to account and transaction records makes it the cheapest option for an FIS core shop, and the hosted tier removes PCI and ops overhead. Automation is RPA-era: it removes keystrokes rather than decisions, and feature depth varies by core version.

- **Proof:** Visa Claim Resolution and Mastercom integration; hosted PCI-compliant option
- **Watch:** positioned as reliable, not innovative — weak fit outside the FIS estate

### ACI Automated Dispute Manager

Disputes live inside the fraud platform, so a confirmed fraud case flows into a chargeback without re-keying. Uniquely in this set it serves both sides of the transaction — issuer case handling and acquirer merchant portals — which suits universal banks.

- **Proof:** Rabobank chargeback and recovery case study
- **Watch:** value drops sharply if you don't already run ACI fraud

### Q2 CentrixDQS · Chargebacks911 · Verint

Three narrower answers. Q2's module is the path of least resistance for Q2 banks and irrelevant elsewhere. Chargebacks911 Issuer Edition replaces the platform decision with an outsourcing decision. Verint captures intake and audit trail in the contact centre but never touches the network — pair it, don't compare it.

- **Watch:** none of the three is a like-for-like Amiko replacement

---

## Two categories that aren't competitors

Both come up in vendor searches for "dispute management" and neither substitutes for an issuer platform.

### Network rails — complements

| Service | What it is |
| --- | --- |
| **Visa: Dispute Intelligence, Doc Analyzer, Dispute Case Manager** | Visa's own 2026 modernisation of issuer dispute handling. Sits under, not instead of, a platform. |
| **Mastercom · VROL** | The scheme case-filing rails. Certification is table stakes; Amiko, Quavo and Pega all hold it. |
| **Ethoca · Verifi** | Pre-dispute deflection networks that resolve with the merchant before a chargeback exists. Buy in addition, always. |

### Merchant-side chargeback tools — opposite side of the transaction

| Tool | What it is |
| --- | --- |
| **Chargeflow · Justt · ChargePay** | AI-native representment: they generate evidence packages to win disputes *against* issuers. Structurally adversarial to your side of the case. |
| **Disputifier** | Shopify-focused, template-driven, success-fee priced. SMB merchant tooling. |
| **Chargebacks911 (merchant edition)** | The same firm sells to both sides — check which product a proposal actually references. |

---

## Shortlist logic

Most issuer evaluations resolve on estate and geography before they reach a feature comparison.

| If | Then |
| --- | --- |
| European issuer, BaaS or fintech; cardholder experience is the pain point | **Amiko** — direct scheme certification means the shortest path to live |
| US bank or credit union with Reg E volume and non-card rails | **Quavo QFD** — the only comparable platform covering ACH, Zelle, RTP and wire |
| Global bank, multiple regulators, Amex in scope, heavy contact-centre intake | **Pega Smart Dispute** — accept the implementation cost for the rules depth |
| Already committed to FIS core, ACI fraud or Q2 digital banking | **The bundled module** wins on integration cost and loses on automation depth — price the gap before defaulting to it |
| Dispute volume too low to justify a platform at all | **Chargebacks911 Issuer Edition** — an outsourcing decision, not a software one |

---

## Caveats

Capability claims — automation percentages, resolution-time improvements, implementation timelines — are drawn from vendor marketing and one third-party market roundup, and none have been independently verified. Treat them as claims to test in an RFI, not as benchmarks. Coverage of Q2, Chargebacks911 and Verint rests on a single secondary source and should be confirmed directly.

**Known gaps:** no pricing or commercial terms for any vendor; no independent customer references or analyst ratings; implementation timelines published for Pega only; Fiserv dispute tooling not covered — add it if it is in the estate.

---

## Sources

**Primary (vendor)**

- [Amiko by Rivero](https://rivero.tech/amiko)
- [Amiko FAQ](https://rivero.tech/faq-amiko)
- [Quavo QFD](https://www.quavo.com/qfd/)
- [Pega Smart Dispute](https://www.pega.com/industries/financial-services/smart-dispute)
- [FIS CBK](https://www.fisglobal.com/products/fis-cbk)
- [ACI Automated Dispute Manager](https://www.aciworldwide.com/solutions/automated-dispute-manager)
- [Visa dispute resolution services](https://corporate.visa.com/en/sites/visa-perspectives/newsroom/dispute-resolution-services.html)

**Secondary**

- [The 7 Best Issuer Dispute Management Platforms for Banks and Fintech Issuers — FintechSpecs](https://fintechspecs.com/blog/dispute-management-software-for-banks/)
- [Chargeback AI: The Issuer Side of the Race to Automate Disputes — FraudBeat](https://www.fraudbeat.com/chargeback-ai-issuer-side/)
- [Top AI Chargeback & Dispute Management Platforms — Startup Stash](https://startupstash.com/top-ai-chargeback-and-dispute-management-platforms/)

---

*Prepared 30 August 2026 · Next review due February 2027 or on the next Visa/Mastercard rule release. Structured data: `dispute-matrix.metadata.json`.*
