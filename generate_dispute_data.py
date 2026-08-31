"""
Card Dispute Evidence Reconstruction & Resolution Agent
Synthetic Data Generator
================================================
Generates all evidence types required for the hackathon:
  1. Disputes (case headers)
  2. Transaction Events
  3. Customer Statements
  4. Merchant Records
  5. Receipts
  6. Delivery Records
  7. Authentication Events
  8. Correspondence (emails / chat)
  9. Audit Trail
 10. FINALE INJECT — Late contradicting merchant evidence

Output: ./synthetic_data/<entity>.json  +  one bundled dispute_cases.json

Run:
  pip install faker
  python generate_dispute_data.py
"""

import json
import random
import uuid
import os
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()
random.seed(42)
Faker.seed(42)

OUTPUT_DIR = "synthetic_data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ─── Config ────────────────────────────────────────────────────────────────────
NUM_CASES        = 500   # total dispute cases
NOW              = datetime.utcnow()

DISPUTE_REASONS  = [
    "Item not received",
    "Item significantly not as described",
    "Unauthorised transaction",
    "Duplicate charge",
    "Service not provided",
    "Credit not processed",
    "Cancelled recurring transaction",
]

DISPUTE_STATUSES = [
    "Raised", "Evidence Gathering", "Under Review",
    "Specialist Review", "Resolution Progressed", "Closed – Won", "Closed – Lost",
]

MCC_CODES = {
    "5411": "Grocery Stores",
    "5812": "Eating Places & Restaurants",
    "5999": "Miscellaneous Retail",
    "7011": "Hotels & Lodging",
    "4111": "Transportation",
    "5732": "Electronics Stores",
    "5261": "Lawn & Garden Supplies",
    "5945": "Hobby, Toy & Game Shops",
    "7922": "Theatrical Producers & Ticket Agencies",
    "4812": "Telecom Equipment & Phone Sales",
}

CARD_NETWORKS  = ["Visa", "Mastercard", "Amex", "Discover"]
CARD_TYPES     = ["Debit", "Credit"]
AUTH_METHODS   = ["3DS2", "PIN", "Contactless", "Chip & PIN", "Biometric", "None"]
DEVICE_TYPES   = ["Mobile App", "Browser", "POS Terminal", "IVR", "In-Branch"]
CHANNELS       = ["Email", "Secure Message", "Phone Transcript", "Chat Log"]

# ─── Helpers ───────────────────────────────────────────────────────────────────

def uid():
    return str(uuid.uuid4())

def ts(base: datetime, delta_seconds: int = 0) -> str:
    return (base + timedelta(seconds=delta_seconds)).strftime("%Y-%m-%dT%H:%M:%SZ")

def jitter(base: datetime, min_s: int, max_s: int) -> datetime:
    return base + timedelta(seconds=random.randint(min_s, max_s))

def amount(lo=5.0, hi=2500.0) -> float:
    return round(random.uniform(lo, hi), 2)

def save(name: str, data):
    path = os.path.join(OUTPUT_DIR, f"{name}.json")
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"  ✓  {path}  ({len(data)} records)")
    return path

# ═══════════════════════════════════════════════════════════════════════════════
# 1. DISPUTE CASES  (master index)
# ═══════════════════════════════════════════════════════════════════════════════

def gen_disputes(n=NUM_CASES):
    cases = []
    for i in range(n):
        raised_at    = fake.date_time_between(start_date="-90d", end_date="-5d")
        deadline     = raised_at + timedelta(days=random.choice([30, 45, 60]))
        mcc_code     = random.choice(list(MCC_CODES.keys()))
        reason       = random.choice(DISPUTE_REASONS)
        status_idx   = random.randint(0, len(DISPUTE_STATUSES) - 1)

        # Finale inject flag – last 5 cases always get one
        finale_inject = (i >= n - 5) or (random.random() < 0.20)

        cases.append({
            "case_id":          uid(),
            "case_number":      f"DSP-{2025000 + i:07d}",
            "raised_at":        raised_at.isoformat() + "Z",
            "deadline":         deadline.isoformat() + "Z",
            "status":           DISPUTE_STATUSES[status_idx],
            "dispute_reason":   reason,
            "claim_amount":     amount(20, 3000),
            "currency":         "USD",
            "card_network":     random.choice(CARD_NETWORKS),
            "card_type":        random.choice(CARD_TYPES),
            "mcc_code":         mcc_code,
            "mcc_description":  MCC_CODES[mcc_code],
            "customer_id":      uid(),
            "merchant_id":      uid(),
            "finale_inject":    finale_inject,   # drives late-evidence scenario
            "created_at":       raised_at.isoformat() + "Z",
            "updated_at":       NOW.isoformat() + "Z",
        })
    return cases


# ═══════════════════════════════════════════════════════════════════════════════
# 2. TRANSACTION EVENTS
# ═══════════════════════════════════════════════════════════════════════════════

def gen_transactions(cases):
    txns = []
    for c in cases:
        base         = datetime.fromisoformat(c["raised_at"].replace("Z", ""))
        txn_at       = base - timedelta(days=random.randint(1, 10))
        authorised   = random.random() > 0.08
        settled      = authorised and random.random() > 0.05
        duplicate    = c["dispute_reason"] == "Duplicate charge" and random.random() > 0.5

        txn = {
            "transaction_id":     uid(),
            "case_id":            c["case_id"],
            "txn_reference":      f"TXN{random.randint(10**11, 10**12 - 1)}",
            "timestamp":          txn_at.isoformat() + "Z",
            "amount":             c["claim_amount"],
            "currency":           c["currency"],
            "merchant_id":        c["merchant_id"],
            "merchant_name":      fake.company(),
            "merchant_city":      fake.city(),
            "merchant_country":   fake.country_code(),
            "mcc_code":           c["mcc_code"],
            "card_network":       c["card_network"],
            "card_last4":         str(random.randint(1000, 9999)),
            "card_type":          c["card_type"],
            "channel":            random.choice(["Online", "In-Store", "MOTO", "Contactless"]),
            "authorisation_code": f"AUTH{random.randint(100000,999999)}" if authorised else None,
            "authorised":         authorised,
            "settled":            settled,
            "settlement_date":    (txn_at + timedelta(days=random.randint(1, 3))).isoformat() + "Z" if settled else None,
            "reversal":           False,
            "reversal_reference": None,
            "provenance":         "CORE_BANKING",
            "version":            1,
        }
        txns.append(txn)

        if duplicate:
            dup = dict(txn)
            dup["transaction_id"]  = uid()
            dup["txn_reference"]   = f"TXN{random.randint(10**11, 10**12-1)}"
            dup["timestamp"]       = (txn_at + timedelta(minutes=random.randint(1,30))).isoformat() + "Z"
            dup["authorisation_code"] = f"AUTH{random.randint(100000,999999)}"
            dup["provenance"]      = "CORE_BANKING"
            dup["version"]         = 1
            txns.append(dup)

    return txns


# ═══════════════════════════════════════════════════════════════════════════════
# 3. CUSTOMER STATEMENTS
# ═══════════════════════════════════════════════════════════════════════════════

STMT_TEMPLATES = {
    "Item not received": (
        "I placed an order on {order_date} for {item} from {merchant}. "
        "The expected delivery was {delivery_date} but nothing has arrived. "
        "I have not received any shipping notification. I am requesting a full refund of ${amount}."
    ),
    "Item significantly not as described": (
        "I purchased {item} from {merchant} on {order_date}. "
        "The product received on {delivery_date} was completely different from what was advertised — "
        "the colour was wrong, the size did not match, and the quality was inferior. "
        "I am disputing the charge of ${amount}."
    ),
    "Unauthorised transaction": (
        "I did not authorise the transaction of ${amount} that appeared on my statement on {txn_date}. "
        "I had my card with me at the time and have never shopped at {merchant}. "
        "I believe this is a fraudulent charge."
    ),
    "Duplicate charge": (
        "I was charged ${amount} twice by {merchant} for the same purchase made on {order_date}. "
        "Only one transaction was authorised by me. Please reverse the duplicate charge."
    ),
    "Service not provided": (
        "I paid ${amount} to {merchant} on {order_date} for {item}. "
        "Despite multiple follow-ups the service was never delivered. "
        "I am requesting a full chargeback."
    ),
    "Credit not processed": (
        "I returned {item} to {merchant} on {delivery_date}. The merchant confirmed the return "
        "but the credit of ${amount} has not appeared on my account after {days} days."
    ),
    "Cancelled recurring transaction": (
        "I cancelled my subscription with {merchant} on {cancel_date} as confirmed by their email. "
        "Despite cancellation they charged ${amount} on {txn_date}. This charge is unauthorised."
    ),
}

def gen_customer_statements(cases, transactions):
    txn_map = {t["case_id"]: t for t in transactions}
    stmts   = []
    for c in cases:
        txn   = txn_map.get(c["case_id"])
        base  = datetime.fromisoformat(c["raised_at"].replace("Z", ""))
        tmpl  = STMT_TEMPLATES.get(c["dispute_reason"], STMT_TEMPLATES["Item not received"])

        narrative = tmpl.format(
            order_date    = (base - timedelta(days=random.randint(7, 20))).strftime("%d %b %Y"),
            delivery_date = (base - timedelta(days=random.randint(1, 6))).strftime("%d %b %Y"),
            txn_date      = (base - timedelta(days=random.randint(1, 10))).strftime("%d %b %Y"),
            cancel_date   = (base - timedelta(days=random.randint(5, 30))).strftime("%d %b %Y"),
            item          = fake.catch_phrase(),
            merchant      = fake.company(),
            amount        = c["claim_amount"],
            days          = random.randint(7, 45),
        )

        stmts.append({
            "statement_id":    uid(),
            "case_id":         c["case_id"],
            "customer_id":     c["customer_id"],
            "submitted_at":    c["raised_at"],
            "channel":         random.choice(["Online Portal", "Phone", "Branch", "Mobile App"]),
            "dispute_reason":  c["dispute_reason"],
            "narrative":       narrative,
            "claimed_amount":  c["claim_amount"],
            "currency":        c["currency"],
            "attachments":     random.sample(
                                 ["screenshot.png", "order_confirmation.pdf",
                                  "email_thread.eml", "bank_statement.pdf"],
                                 k=random.randint(0, 2)),
            "provenance":      "CUSTOMER_PORTAL",
            "version":         1,
            "superseded_by":   None,
        })
    return stmts


# ═══════════════════════════════════════════════════════════════════════════════
# 4. MERCHANT RECORDS
# ═══════════════════════════════════════════════════════════════════════════════

def gen_merchant_records(cases, transactions):
    txn_map  = {t["case_id"]: t for t in transactions}
    records  = []
    for c in cases:
        txn  = txn_map.get(c["case_id"])
        base = datetime.fromisoformat(c["raised_at"].replace("Z", ""))

        fulfilled    = c["dispute_reason"] not in ["Item not received", "Service not provided"]
        order_status = random.choice(["Delivered", "Dispatched", "Processing", "Cancelled", "Refunded"])

        records.append({
            "merchant_record_id": uid(),
            "case_id":            c["case_id"],
            "merchant_id":        c["merchant_id"],
            "merchant_name":      fake.company(),
            "order_id":           f"ORD-{random.randint(100000, 999999)}",
            "order_date":         (base - timedelta(days=random.randint(7, 20))).isoformat() + "Z",
            "order_status":       order_status,
            "items":              [
                                     {
                                         "sku":         f"SKU-{random.randint(1000,9999)}",
                                         "description": fake.catch_phrase(),
                                         "qty":         random.randint(1, 3),
                                         "unit_price":  round(c["claim_amount"] / random.randint(1, 3), 2),
                                     }
                                  ],
            "total_charged":      c["claim_amount"],
            "currency":           c["currency"],
            "fulfilled":          fulfilled,
            "refund_issued":      c["dispute_reason"] == "Credit not processed" and random.random() > 0.5,
            "refund_amount":      c["claim_amount"] if c["dispute_reason"] == "Credit not processed" else None,
            "refund_date":        (base - timedelta(days=random.randint(1, 5))).isoformat() + "Z"
                                  if c["dispute_reason"] == "Credit not processed" else None,
            "merchant_response":  random.choice([
                "Order delivered as described.",
                "Item dispatched; tracking number provided.",
                "Refund already processed.",
                "Subscription cancelled after charge date.",
                "Customer accepted delivery.",
            ]),
            "received_at":        c["raised_at"],
            "provenance":         "MERCHANT_PORTAL",
            "version":            1,
            "superseded_by":      None,
        })
    return records


# ═══════════════════════════════════════════════════════════════════════════════
# 5. RECEIPTS
# ═══════════════════════════════════════════════════════════════════════════════

def gen_receipts(cases, merchant_records):
    mr_map   = {r["case_id"]: r for r in merchant_records}
    receipts = []
    for c in cases:
        mr   = mr_map.get(c["case_id"])
        base = datetime.fromisoformat(c["raised_at"].replace("Z", ""))

        receipts.append({
            "receipt_id":        uid(),
            "case_id":           c["case_id"],
            "order_id":          mr["order_id"] if mr else f"ORD-{random.randint(100000,999999)}",
            "merchant_id":       c["merchant_id"],
            "issued_at":         (base - timedelta(days=random.randint(8, 20))).isoformat() + "Z",
            "receipt_number":    f"RCT-{random.randint(1000000, 9999999)}",
            "line_items":        mr["items"] if mr else [],
            "subtotal":          c["claim_amount"],
            "tax":               round(c["claim_amount"] * 0.08, 2),
            "total":             round(c["claim_amount"] * 1.08, 2),
            "currency":          c["currency"],
            "payment_method":    f"{c['card_type']} {c['card_network']} ****{random.randint(1000,9999)}",
            "format":            random.choice(["PDF", "HTML", "Image"]),
            "hash_sha256":       uuid.uuid4().hex + uuid.uuid4().hex[:32],
            "provenance":        "MERCHANT_RECEIPT_SYSTEM",
            "version":           1,
        })
    return receipts


# ═══════════════════════════════════════════════════════════════════════════════
# 6. DELIVERY RECORDS
# ═══════════════════════════════════════════════════════════════════════════════

CARRIERS    = ["FedEx", "UPS", "DHL", "USPS", "Royal Mail", "Aramex"]
DLVR_STATUS = ["Delivered", "In Transit", "Out for Delivery", "Failed Delivery", "Returned to Sender", "Lost"]

def gen_delivery_records(cases, merchant_records):
    mr_map  = {r["case_id"]: r for r in merchant_records}
    records = []
    for c in cases:
        mr   = mr_map.get(c["case_id"])
        base = datetime.fromisoformat(c["raised_at"].replace("Z", ""))

        shipped_at = base - timedelta(days=random.randint(5, 18))
        expected   = shipped_at + timedelta(days=random.randint(2, 7))
        actual     = expected + timedelta(days=random.randint(-1, 5))

        # For "Item not received" disputes, delivery often shows failed/lost
        if c["dispute_reason"] == "Item not received":
            dlv_status = random.choice(["Failed Delivery", "Lost", "In Transit", "Returned to Sender"])
            delivered  = False
            signature  = None
        else:
            dlv_status = random.choice(["Delivered", "Delivered", "Delivered", "In Transit"])
            delivered  = dlv_status == "Delivered"
            signature  = fake.name() if delivered and random.random() > 0.3 else None

        events = [
            {"event": "Order Received",    "timestamp": shipped_at.isoformat() + "Z", "location": fake.city()},
            {"event": "Dispatched",        "timestamp": (shipped_at + timedelta(hours=6)).isoformat() + "Z",  "location": fake.city()},
            {"event": "In Transit",        "timestamp": (shipped_at + timedelta(days=1)).isoformat() + "Z",   "location": fake.city()},
        ]
        if delivered:
            events.append({"event": "Delivered", "timestamp": actual.isoformat() + "Z", "location": fake.city()})
        elif dlv_status == "Failed Delivery":
            events.append({"event": "Failed Delivery Attempt", "timestamp": actual.isoformat() + "Z", "location": fake.city()})

        records.append({
            "delivery_id":        uid(),
            "case_id":            c["case_id"],
            "order_id":           mr["order_id"] if mr else f"ORD-{random.randint(100000,999999)}",
            "carrier":            random.choice(CARRIERS),
            "tracking_number":    f"{random.choice(['1Z','JD','GM'])}{random.randint(10**14,10**15-1)}",
            "shipped_at":         shipped_at.isoformat() + "Z",
            "expected_by":        expected.isoformat() + "Z",
            "actual_delivery_at": actual.isoformat() + "Z" if delivered else None,
            "status":             dlv_status,
            "delivered":          delivered,
            "delivery_address":   fake.address().replace("\n", ", "),
            "signature_obtained": signature,
            "proof_of_delivery":  f"pod_{uid()[:8]}.jpg" if delivered else None,
            "events":             events,
            "provenance":         "CARRIER_API",
            "version":            1,
        })
    return records


# ═══════════════════════════════════════════════════════════════════════════════
# 7. AUTHENTICATION EVENTS
# ═══════════════════════════════════════════════════════════════════════════════

def gen_auth_events(cases, transactions):
    txn_map = {t["case_id"]: t for t in transactions}
    events  = []
    for c in cases:
        txn  = txn_map.get(c["case_id"])
        base = datetime.fromisoformat(c["raised_at"].replace("Z", ""))
        txn_ts = datetime.fromisoformat(
            txn["timestamp"].replace("Z","")) if txn else base - timedelta(days=3)

        auth_method = random.choice(AUTH_METHODS)
        success     = c["dispute_reason"] != "Unauthorised transaction" or random.random() > 0.6
        device      = random.choice(DEVICE_TYPES)
        ip          = fake.ipv4_public()
        geo         = f"{fake.city()}, {fake.country()}"

        # For unauthorised disputes: sometimes show geo mismatch
        geo_mismatch = (c["dispute_reason"] == "Unauthorised transaction") and (random.random() > 0.4)

        events.append({
            "auth_event_id":     uid(),
            "case_id":           c["case_id"],
            "transaction_id":    txn["transaction_id"] if txn else None,
            "event_type":        random.choice(["AUTHORISATION", "3DS_CHALLENGE", "PIN_VERIFY", "BIOMETRIC_VERIFY"]),
            "timestamp":         txn_ts.isoformat() + "Z",
            "auth_method":       auth_method,
            "success":           success,
            "failure_reason":    None if success else random.choice(
                                     ["Wrong PIN", "3DS timeout", "Biometric mismatch", "OTP expired"]),
            "device_type":       device,
            "device_fingerprint":uid()[:16],
            "ip_address":        ip,
            "geo_location":      geo,
            "geo_mismatch":      geo_mismatch,
            "customer_id":       c["customer_id"],
            "risk_score":        round(random.uniform(0, 1), 4),
            "risk_decision":     random.choice(["APPROVE", "APPROVE", "APPROVE", "DECLINE", "REFER"]),
            "provenance":        "AUTH_ENGINE",
            "version":           1,
        })
    return events


# ═══════════════════════════════════════════════════════════════════════════════
# 8. CORRESPONDENCE
# ═══════════════════════════════════════════════════════════════════════════════

CORR_TEMPLATES = [
    {
        "direction": "BANK_TO_CUSTOMER",
        "subject":   "Your dispute {case_number} has been received",
        "body":      (
            "Dear {name},\n\nWe have received your dispute case {case_number} and are "
            "investigating the charge of {currency} {amount} from {merchant}. "
            "We will update you within 5 business days.\n\nRegards,\nDisputes Team"
        ),
    },
    {
        "direction": "BANK_TO_MERCHANT",
        "subject":   "Retrieval Request – {case_number}",
        "body":      (
            "Dear Merchant,\n\nWe are requesting evidence for dispute {case_number}. "
            "Please provide order records, delivery confirmation and any signed receipts "
            "within 10 business days.\n\nDisputes Operations"
        ),
    },
    {
        "direction": "MERCHANT_TO_BANK",
        "subject":   "RE: Retrieval Request – {case_number}",
        "body":      (
            "Please find attached our order confirmation, dispatch note and proof of delivery "
            "for case {case_number}. The item was delivered and signed for on {delivery_date}."
        ),
    },
    {
        "direction": "CUSTOMER_TO_BANK",
        "subject":   "Additional info for {case_number}",
        "body":      (
            "Hi,\n\nI'm following up on my dispute {case_number}. "
            "I still have not received the item or a refund. "
            "Please find the attached screenshot of the tracking page showing no delivery.\n\n{name}"
        ),
    },
]

def gen_correspondence(cases):
    corrs = []
    for c in cases:
        base     = datetime.fromisoformat(c["raised_at"].replace("Z", ""))
        name     = fake.name()
        merchant = fake.company()
        num_msgs = random.randint(2, 5)
        selected = random.sample(CORR_TEMPLATES, min(num_msgs, len(CORR_TEMPLATES)))

        for idx, tmpl in enumerate(selected):
            sent_at = base + timedelta(days=idx * random.randint(1, 3))
            body    = tmpl["body"].format(
                case_number   = c["case_number"],
                name          = name,
                currency      = c["currency"],
                amount        = c["claim_amount"],
                merchant      = merchant,
                delivery_date = (base - timedelta(days=2)).strftime("%d %b %Y"),
            )
            corrs.append({
                "correspondence_id": uid(),
                "case_id":           c["case_id"],
                "case_number":       c["case_number"],
                "channel":           random.choice(CHANNELS),
                "direction":         tmpl["direction"],
                "sent_at":           sent_at.isoformat() + "Z",
                "from_party":        tmpl["direction"].split("_TO_")[0].title(),
                "to_party":          tmpl["direction"].split("_TO_")[1].title(),
                "subject":           tmpl["subject"].format(case_number=c["case_number"]),
                "body":              body,
                "attachments":       random.sample(
                                         ["order_confirmation.pdf", "pod.jpg",
                                          "tracking_screenshot.png", "invoice.pdf"],
                                         k=random.randint(0, 2)),
                "provenance":        "CORRESPONDENCE_SYSTEM",
                "version":           1,
                "superseded_by":     None,
            })
    return corrs


# ═══════════════════════════════════════════════════════════════════════════════
# 9. AUDIT TRAIL
# ═══════════════════════════════════════════════════════════════════════════════

AUDIT_ACTIONS = [
    "Dispute raised by customer",
    "Initial evidence assembled",
    "Transaction event retrieved",
    "Merchant retrieval request sent",
    "Customer statement recorded",
    "Authentication event retrieved",
    "Delivery record retrieved",
    "Evidence gap identified",
    "Specialist review assigned",
    "Human decision recorded",
    "Resolution progressed",
    "Case status updated",
]

def gen_audit_trail(cases):
    entries = []
    for c in cases:
        base = datetime.fromisoformat(c["raised_at"].replace("Z", ""))
        num  = random.randint(4, 10)
        for i in range(num):
            actor_type = random.choice(["SYSTEM", "AI_AGENT", "HUMAN_ANALYST", "HUMAN_MANAGER"])
            entries.append({
                "audit_id":          uid(),
                "case_id":           c["case_id"],
                "case_number":       c["case_number"],
                "sequence":          i + 1,
                "timestamp":         (base + timedelta(hours=i * random.randint(1, 12))).isoformat() + "Z",
                "action":            AUDIT_ACTIONS[i % len(AUDIT_ACTIONS)],
                "actor_type":        actor_type,
                "actor_id":          uid()[:8] if actor_type.startswith("HUMAN") else f"agent-{actor_type.lower()}",
                "description":       f"{AUDIT_ACTIONS[i % len(AUDIT_ACTIONS)]} for case {c['case_number']}.",
                "entity_type":       random.choice(["DISPUTE", "TRANSACTION", "MERCHANT_RECORD",
                                                    "DELIVERY", "CORRESPONDENCE", "AUTH_EVENT"]),
                "entity_id":         uid(),
                "previous_state":    DISPUTE_STATUSES[max(0, (i // 3) - 1)],
                "new_state":         DISPUTE_STATUSES[min(len(DISPUTE_STATUSES)-1, i // 3)],
                "ai_inference":      actor_type == "AI_AGENT",
                "human_approved":    actor_type in ("HUMAN_ANALYST", "HUMAN_MANAGER"),
                "provenance":        "AUDIT_SERVICE",
            })
    return entries


# ═══════════════════════════════════════════════════════════════════════════════
# 10. FINALE INJECT — Late contradicting merchant evidence
# ═══════════════════════════════════════════════════════════════════════════════
#
# Scenario: After the case has progressed (Evidence Gathering or Under Review),
# the merchant submits NEW evidence that DIRECTLY CONTRADICTS the customer's
# original statement. The agent must:
#   (a) incorporate the new evidence
#   (b) re-assess all dependent conclusions
#   (c) make the change visible in the audit trail
# ═══════════════════════════════════════════════════════════════════════════════

CONTRADICTION_TYPES = [
    {
        "type":                "DELIVERY_PROOF_CONTRADICTS_NOT_RECEIVED",
        "customer_claim":      "Customer stated item was never received and no delivery was attempted.",
        "merchant_rebuttal":   "Merchant provides GPS-timestamped proof-of-delivery photo and carrier signature log showing item was delivered and signed for by a household member.",
        "new_evidence_type":   "proof_of_delivery_photo",
        "impact":              "HIGH",
        "reassess_targets":    ["customer_statement", "delivery_record", "outcome_recommendation"],
    },
    {
        "type":                "CANCELLATION_AFTER_CHARGE_DATE",
        "customer_claim":      "Customer stated subscription was cancelled before the disputed charge.",
        "merchant_rebuttal":   "Merchant submits cancellation confirmation email timestamped AFTER the charge date, proving the charge was valid at time of processing.",
        "new_evidence_type":   "cancellation_timestamp_log",
        "impact":              "HIGH",
        "reassess_targets":    ["customer_statement", "correspondence", "outcome_recommendation"],
    },
    {
        "type":                "ITEM_MATCHES_DESCRIPTION",
        "customer_claim":      "Customer claimed item received was significantly not as described.",
        "merchant_rebuttal":   "Merchant provides product listing snapshot at time of purchase with verified images matching the shipped item, plus a third-party quality inspection report.",
        "new_evidence_type":   "product_listing_snapshot",
        "impact":              "MEDIUM",
        "reassess_targets":    ["customer_statement", "merchant_record", "outcome_recommendation"],
    },
    {
        "type":                "AUTH_DEVICE_MATCHES_CUSTOMER",
        "customer_claim":      "Customer claimed transaction was unauthorised and they did not initiate it.",
        "merchant_rebuttal":   "Merchant provides server-side session log showing the customer's registered device fingerprint and billing address were used, with successful 3DS2 verification.",
        "new_evidence_type":   "session_log_with_device_match",
        "impact":              "HIGH",
        "reassess_targets":    ["customer_statement", "auth_event", "outcome_recommendation"],
    },
    {
        "type":                "REFUND_ALREADY_PROCESSED",
        "customer_claim":      "Customer stated no refund was received for the returned item.",
        "merchant_rebuttal":   "Merchant provides bank ledger reference showing the refund was posted to the card 3 days after the dispute was raised, before case review began.",
        "new_evidence_type":   "merchant_refund_ledger",
        "impact":              "MEDIUM",
        "reassess_targets":    ["customer_statement", "merchant_record", "outcome_recommendation"],
    },
]

def gen_finale_injects(cases, customer_statements, merchant_records):
    cs_map = {s["case_id"]: s for s in customer_statements}
    mr_map = {r["case_id"]: r for r in merchant_records}
    injects = []

    for c in cases:
        if not c.get("finale_inject"):
            continue

        base        = datetime.fromisoformat(c["raised_at"].replace("Z", ""))
        inject_at   = base + timedelta(days=random.randint(10, 25))  # arrives LATE
        contradiction = random.choice(CONTRADICTION_TYPES)
        cs          = cs_map.get(c["case_id"])
        mr          = mr_map.get(c["case_id"])

        injects.append({
            "inject_id":              uid(),
            "case_id":                c["case_id"],
            "case_number":            c["case_number"],

            # When it arrived — always AFTER initial evidence phase
            "received_at":            inject_at.isoformat() + "Z",
            "arrived_late":           True,
            "case_status_at_arrival": random.choice(["Under Review", "Specialist Review",
                                                     "Evidence Gathering"]),

            # What the merchant submitted
            "submitted_by":           "MERCHANT",
            "merchant_id":            c["merchant_id"],
            "evidence_type":          contradiction["new_evidence_type"],
            "evidence_reference":     f"EVD-{uid()[:12].upper()}",
            "evidence_payload": {
                "file":           f"{contradiction['new_evidence_type']}_{uid()[:8]}.pdf",
                "hash_sha256":    uuid.uuid4().hex + uuid.uuid4().hex[:32],
                "description":    contradiction["merchant_rebuttal"],
                "verified":       False,   # awaiting human review at inject time
            },

            # What it contradicts
            "contradiction_type":     contradiction["type"],
            "original_customer_claim": contradiction["customer_claim"],
            "merchant_rebuttal":      contradiction["merchant_rebuttal"],
            "impact_level":           contradiction["impact"],

            # What the agent must reassess
            "reassess_targets":       contradiction["reassess_targets"],
            "conclusions_invalidated": [
                f"Prior recommendation based on '{contradiction['customer_claim'][:60]}...' "
                f"must be re-evaluated against new merchant evidence."
            ],

            # Agent actions required
            "required_agent_actions": [
                "Ingest new evidence and update case evidence set",
                "Version-stamp prior conclusions as potentially stale",
                "Re-run gap analysis against updated evidence set",
                "Reassess outcome recommendation",
                "Flag change delta to human reviewer",
                "Append inject event to audit trail",
            ],

            # Visibility — the change must be surfaced to reviewers
            "change_visible":         False,   # set True after agent processes
            "reviewer_notified":      False,
            "delta_summary":          None,    # populated by agent post-processing

            # Audit
            "provenance":             "MERCHANT_PORTAL_LATE_SUBMISSION",
            "version":                1,
            "superseded_prior_version": {
                "merchant_record_id": mr["merchant_record_id"] if mr else None,
                "version":            mr["version"] if mr else None,
            },
        })
    return injects


# ═══════════════════════════════════════════════════════════════════════════════
# MASTER BUNDLE  — one self-contained file per dispute case
# ═══════════════════════════════════════════════════════════════════════════════

def build_case_bundle(cases, transactions, statements, merchant_records,
                      receipts, deliveries, auth_events, correspondence,
                      audit_trail, finale_injects):
    txn_map    = {t["case_id"]: t for t in transactions}
    stmt_map   = {s["case_id"]: s for s in statements}
    mr_map     = {r["case_id"]: r for r in merchant_records}
    rcpt_map   = {r["case_id"]: r for r in receipts}
    dlv_map    = {d["case_id"]: d for d in deliveries}
    auth_map   = {a["case_id"]: a for a in auth_events}
    fi_map     = {i["case_id"]: i for i in finale_injects}
    corr_map   = {}
    for co in correspondence:
        corr_map.setdefault(co["case_id"], []).append(co)
    audit_map  = {}
    for a in audit_trail:
        audit_map.setdefault(a["case_id"], []).append(a)

    bundles = []
    for c in cases:
        cid = c["case_id"]
        bundles.append({
            "dispute":             c,
            "transaction":         txn_map.get(cid),
            "customer_statement":  stmt_map.get(cid),
            "merchant_record":     mr_map.get(cid),
            "receipt":             rcpt_map.get(cid),
            "delivery_record":     dlv_map.get(cid),
            "auth_event":          auth_map.get(cid),
            "correspondence":      corr_map.get(cid, []),
            "audit_trail":         audit_map.get(cid, []),
            "finale_inject":       fi_map.get(cid),   # None if no inject
        })
    return bundles


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    print("\n🏗  Generating synthetic dispute data …\n")

    cases           = gen_disputes()
    transactions    = gen_transactions(cases)
    statements      = gen_customer_statements(cases, transactions)
    merch_records   = gen_merchant_records(cases, transactions)
    receipts        = gen_receipts(cases, merch_records)
    deliveries      = gen_delivery_records(cases, merch_records)
    auth_events     = gen_auth_events(cases, transactions)
    correspondence  = gen_correspondence(cases)
    audit_trail     = gen_audit_trail(cases)
    finale_injects  = gen_finale_injects(cases, statements, merch_records)

    print("Saving individual entity files:")
    save("disputes",           cases)
    save("transactions",       transactions)
    save("customer_statements",statements)
    save("merchant_records",   merch_records)
    save("receipts",           receipts)
    save("delivery_records",   deliveries)
    save("auth_events",        auth_events)
    save("correspondence",     correspondence)
    save("audit_trail",        audit_trail)
    save("finale_injects",     finale_injects)

    print("\nBuilding master case bundles …")
    bundles = build_case_bundle(
        cases, transactions, statements, merch_records,
        receipts, deliveries, auth_events, correspondence,
        audit_trail, finale_injects,
    )
    save("dispute_cases_bundled", bundles)

    # Summary
    inject_count = sum(1 for c in cases if c["finale_inject"])
    print(f"""
╔══════════════════════════════════════════════════╗
║  Synthetic Data Generation Complete              ║
╠══════════════════════════════════════════════════╣
║  Dispute cases         : {len(cases):<5}                    ║
║  Transactions          : {len(transactions):<5}                    ║
║  Customer statements   : {len(statements):<5}                    ║
║  Merchant records      : {len(merch_records):<5}                    ║
║  Receipts              : {len(receipts):<5}                    ║
║  Delivery records      : {len(deliveries):<5}                    ║
║  Auth events           : {len(auth_events):<5}                    ║
║  Correspondence msgs   : {len(correspondence):<5}                    ║
║  Audit trail entries   : {len(audit_trail):<5}                    ║
║  Finale inject cases   : {inject_count:<5}                    ║
╚══════════════════════════════════════════════════╝

Output folder : ./{OUTPUT_DIR}/
Bundle file   : ./{OUTPUT_DIR}/dispute_cases_bundled.json
    """)


if __name__ == "__main__":
    main()
