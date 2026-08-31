"""
Card Dispute Evidence Reconstruction & Resolution Agent
Synthetic Data Generator — v2 (Real-Dataset Calibrated)
=========================================================
Calibrated against:
  • PaySim       — balance tracking, transaction types, fraud-on-TRANSFER/CASHOUT
  • Sparknov     — merchant categories (grocery, gas, entertainment…)
  • Fraud eCommerce (Kaggle) — device_id, browser, ip_address, signup/purchase times
  • IEEE-CIS     — 3DS ECI, device type, identity fields
  • CFPB         — company_response, timely_response, consumer_disputed
  • Zenodo Digital Payment — journal_type, channel_reference_number, is_verified
  • Chargebacks911 2026 — amount distribution (~$84 avg), 0.6–1% CNP rate,
                          friendly fraud 40–80%, merchant win 43.8%
  • Visa/Mastercard reason codes — real chargeback codes used

Output: ./synthetic_data_v2/<entity>.json  +  dispute_cases_bundled.json

Run:
    pip install faker numpy
    python generate_dispute_data_v2.py
"""

import json, random, uuid, os, math
from datetime import datetime, timedelta
from faker import Faker

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

fake = Faker()
random.seed(42)
Faker.seed(42)
if HAS_NUMPY:
    np.random.seed(42)

OUTPUT_DIR = "synthetic_data_v2"
os.makedirs(OUTPUT_DIR, exist_ok=True)

NOW = datetime.utcnow()
NUM_RANDOM_CASES = 495   # + 5 hand-crafted = 500 total


# ═══════════════════════════════════════════════════════════════════════════════
# REAL-DATA REFERENCE TABLES
# ═══════════════════════════════════════════════════════════════════════════════

# --- Merchant categories (Sparknov + standard MCC) ---
MERCHANT_CATEGORIES = {
    "grocery_net":      {"mcc": "5411", "label": "Grocery Stores",              "avg_txn": 68,   "std": 45},
    "gas_transport":    {"mcc": "5541", "label": "Service Stations (Fuel)",     "avg_txn": 52,   "std": 20},
    "entertainment":    {"mcc": "7922", "label": "Theatrical Producers & Tickets","avg_txn": 89, "std": 60},
    "food_dining":      {"mcc": "5812", "label": "Eating Places & Restaurants", "avg_txn": 38,   "std": 30},
    "home":             {"mcc": "5722", "label": "Household Appliance Stores",  "avg_txn": 320,  "std": 250},
    "kids_pets":        {"mcc": "5945", "label": "Hobby, Toy & Game Shops",     "avg_txn": 55,   "std": 40},
    "personal_care":    {"mcc": "7297", "label": "Health & Beauty Spas",        "avg_txn": 75,   "std": 50},
    "health_fitness":   {"mcc": "7941", "label": "Sports Clubs & Athletic",     "avg_txn": 42,   "std": 25},
    "shopping":         {"mcc": "5999", "label": "Miscellaneous Retail",        "avg_txn": 95,   "std": 80},
    "travel":           {"mcc": "7011", "label": "Hotels & Lodging",            "avg_txn": 285,  "std": 200},
    "electronics":      {"mcc": "5732", "label": "Electronics Stores",          "avg_txn": 420,  "std": 300},
    "telecom":          {"mcc": "4812", "label": "Telecom Equipment & Phones",  "avg_txn": 110,  "std": 90},
    "subscription":     {"mcc": "7372", "label": "Prepackaged Software/SaaS",   "avg_txn": 29,   "std": 20},
    "misc_services":    {"mcc": "7299", "label": "Services Not Elsewhere",      "avg_txn": 60,   "std": 45},
}
CATEGORY_KEYS = list(MERCHANT_CATEGORIES.keys())

# --- Real Visa / Mastercard chargeback reason codes ---
# Source: Visa Core Rules / Mastercard Chargeback Guide
REASON_CODES = {
    "Item not received": [
        {"network": "Visa",       "code": "13.1", "label": "Merchandise/Services Not Received"},
        {"network": "Mastercard", "code": "4853", "label": "Cardholder Dispute – Not as Described or Defective"},
    ],
    "Item significantly not as described": [
        {"network": "Visa",       "code": "13.3", "label": "Not as Described or Defective Merchandise"},
        {"network": "Mastercard", "code": "4853", "label": "Cardholder Dispute – Not as Described or Defective"},
    ],
    "Unauthorised transaction": [
        {"network": "Visa",       "code": "10.4", "label": "Other Fraud – Card-Absent Environment"},
        {"network": "Mastercard", "code": "4837", "label": "No Cardholder Authorization"},
    ],
    "Duplicate charge": [
        {"network": "Visa",       "code": "12.6", "label": "Duplicate Processing"},
        {"network": "Mastercard", "code": "4834", "label": "Duplicate Processing"},
    ],
    "Service not provided": [
        {"network": "Visa",       "code": "13.1", "label": "Merchandise/Services Not Received"},
        {"network": "Mastercard", "code": "4853", "label": "Cardholder Dispute – Services Not Provided"},
    ],
    "Credit not processed": [
        {"network": "Visa",       "code": "13.6", "label": "Credit Not Processed"},
        {"network": "Mastercard", "code": "4860", "label": "Credit Not Processed"},
    ],
    "Cancelled recurring transaction": [
        {"network": "Visa",       "code": "13.2", "label": "Cancelled Recurring Transaction"},
        {"network": "Mastercard", "code": "4841", "label": "Cancelled Recurring or Digital Goods Transaction"},
    ],
}

# --- CFPB-style company response values ---
COMPANY_RESPONSES = [
    "Closed with explanation",
    "Closed with monetary relief",
    "Closed with non-monetary relief",
    "Closed without relief",
    "In progress",
]

# --- 3DS ECI values (IEEE-CIS calibrated) ---
ECI_VALUES = {
    "fully_authenticated":     {"eci": "05", "label": "Full 3DS authentication"},
    "attempted":               {"eci": "06", "label": "Attempted authentication"},
    "non_3ds":                 {"eci": "07", "label": "Non-3DS channel"},
    "mastercard_auth":         {"eci": "02", "label": "Mastercard – fully authenticated"},
    "mastercard_attempt":      {"eci": "01", "label": "Mastercard – attempted"},
}

# --- Browser / device fields (Fraud eCommerce dataset) ---
BROWSERS   = ["Chrome", "Firefox", "Safari", "Edge", "Samsung Browser", "Opera", "Unknown"]
OS_TYPES   = ["Windows", "macOS", "iOS", "Android", "Linux"]
DEVICE_CATS= ["Desktop", "Mobile", "Tablet"]

# --- PaySim transaction types ---
PAYSIM_TYPES = ["CASH_IN", "CASH_OUT", "DEBIT", "PAYMENT", "TRANSFER"]

# --- Carriers + realistic delivery windows (Olist-calibrated) ---
CARRIERS = {
    "FedEx":       {"min_days": 1, "max_days": 5,  "late_prob": 0.08},
    "UPS":         {"min_days": 1, "max_days": 5,  "late_prob": 0.09},
    "DHL":         {"min_days": 2, "max_days": 7,  "late_prob": 0.12},
    "USPS":        {"min_days": 2, "max_days": 10, "late_prob": 0.18},
    "Royal Mail":  {"min_days": 2, "max_days": 8,  "late_prob": 0.15},
    "Aramex":      {"min_days": 3, "max_days": 10, "late_prob": 0.20},
}

DISPUTE_REASONS  = list(REASON_CODES.keys())
CARD_NETWORKS    = ["Visa", "Mastercard", "Amex", "Discover"]
CARD_TYPES       = ["Debit", "Credit"]
DISPUTE_STATUSES = [
    "Raised", "Evidence Gathering", "Under Review",
    "Specialist Review", "Resolution Progressed", "Closed – Won", "Closed – Lost",
]
CHANNELS = ["Email", "Secure Message", "Phone Transcript", "Chat Log"]


# ═══════════════════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

def uid():
    return str(uuid.uuid4())

def save(name, data):
    path = os.path.join(OUTPUT_DIR, f"{name}.json")
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"  ✓  {path}  ({len(data)} records)")

def iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")

def jitter(base, min_s, max_s):
    return base + timedelta(seconds=random.randint(min_s, max_s))

def lognormal_amount(mean_usd, std_usd, lo=1.0, hi=5000.0):
    """
    Log-normal amount calibrated to Chargebacks911 2026 data.
    Mean ~$84/dispute for consumer, up to $2500+ for electronics.
    """
    if HAS_NUMPY:
        sigma = math.sqrt(math.log(1 + (std_usd / mean_usd) ** 2))
        mu    = math.log(mean_usd) - sigma ** 2 / 2
        val   = np.random.lognormal(mu, sigma)
    else:
        val = random.gauss(mean_usd, std_usd)
    return round(max(lo, min(hi, val)), 2)

def txn_time(base_date):
    """
    Realistic intra-day transaction time (peak 10am-8pm, quiet 1-6am).
    Calibrated to PaySim step distribution (744 steps, 1h each).
    """
    hour_weights = [
        1, 1, 0.5, 0.5, 0.5, 0.5,   # 0-5  (quiet)
        2, 4, 6,   7,   8,   8,       # 6-11 (morning ramp)
        9, 9, 8,   8,   9,   10,      # 12-17 (lunch + afternoon)
        10,9, 7,   6,   4,   2,       # 18-23 (evening)
    ]
    hour = random.choices(range(24), weights=hour_weights)[0]
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return base_date.replace(hour=hour, minute=minute, second=second)


# ═══════════════════════════════════════════════════════════════════════════════
# 1. DISPUTES
# ═══════════════════════════════════════════════════════════════════════════════

def gen_dispute(idx, raised_at=None, reason=None, finale_inject=None,
                override_fields=None):
    """Build one dispute record."""
    if raised_at is None:
        raised_at = fake.date_time_between(start_date="-120d", end_date="-5d")
    if reason is None:
        reason = random.choice(DISPUTE_REASONS)

    cat_key  = random.choice(CATEGORY_KEYS)
    cat      = MERCHANT_CATEGORIES[cat_key]
    network  = random.choice(CARD_NETWORKS)

    # Realistic amount: log-normal from merchant category averages
    amt = lognormal_amount(cat["avg_txn"], cat["std"])

    # Chargebacks911: avg $84 per cardholder — pull outlier cases toward that
    if random.random() < 0.25:
        amt = lognormal_amount(84, 60)

    # Reason codes
    rc_options = REASON_CODES.get(reason, [])
    rc = next((r for r in rc_options if r["network"] == network), rc_options[0]) \
         if rc_options else {"code": "N/A", "label": reason, "network": network}

    # Deadline: Visa 120 days / MC 120 days from transaction date
    deadline = raised_at + timedelta(days=random.choice([30, 45, 60, 90, 120]))

    # Friendly fraud flag (40-80% per Chargebacks911)
    is_friendly_fraud = (reason in ["Item not received", "Item significantly not as described",
                                     "Credit not processed"]) and random.random() < 0.60

    status_idx = random.randint(0, len(DISPUTE_STATUSES) - 1)

    record = {
        "case_id":               uid(),
        "case_number":           f"DSP-{2025000 + idx:07d}",
        "raised_at":             iso(raised_at),
        "deadline":              iso(deadline),
        "status":                DISPUTE_STATUSES[status_idx],
        "dispute_reason":        reason,

        # Real reason codes (Visa / Mastercard)
        "reason_code":           rc["code"],
        "reason_code_label":     rc["label"],
        "reason_code_network":   rc["network"],

        "claim_amount":          amt,
        "currency":              random.choice(["USD", "USD", "USD", "GBP", "EUR", "CAD"]),
        "card_network":          network,
        "card_type":             random.choice(CARD_TYPES),

        # Merchant
        "merchant_category_key": cat_key,
        "mcc_code":              cat["mcc"],
        "mcc_description":       cat["label"],

        # IDs
        "customer_id":           uid(),
        "merchant_id":           uid(),

        # Fraud classification (Chargebacks911)
        "friendly_fraud":        is_friendly_fraud,
        "fraud_type":            "Friendly Fraud" if is_friendly_fraud else
                                 ("True Fraud" if reason == "Unauthorised transaction"
                                  else "Merchant Error"),

        # CFPB-style outcome fields
        "company_response":      random.choice(COMPANY_RESPONSES),
        "timely_response":       random.random() > 0.02,       # 98% timely (CFPB)
        "consumer_disputed":     random.random() < 0.20,

        # Merchant win rate (Chargebacks911: 43.8% of contested)
        "merchant_contested":    random.random() < 0.60,
        "merchant_win":          None,   # set at resolution

        "finale_inject":         finale_inject if finale_inject is not None
                                 else (random.random() < 0.10),
        "created_at":            iso(raised_at),
        "updated_at":            iso(NOW),
    }

    if override_fields:
        record.update(override_fields)

    # Set merchant_win for closed cases
    if record["status"].startswith("Closed") and record["merchant_contested"]:
        record["merchant_win"] = random.random() < 0.438

    return record


def gen_disputes(n):
    cases = []
    for i in range(n):
        cases.append(gen_dispute(i))
    return cases


# ═══════════════════════════════════════════════════════════════════════════════
# 2. TRANSACTIONS  (PaySim-calibrated: balance tracking, type, step)
# ═══════════════════════════════════════════════════════════════════════════════

def gen_transaction(case):
    raised   = datetime.fromisoformat(case["raised_at"].replace("Z", ""))
    # Dispute filed 1–45 days after transaction (realistic lag)
    txn_days_back = random.choices(
        range(1, 46),
        weights=[10, 9, 8, 8, 7, 7, 6, 6, 5, 5,   # 1-10
                 4, 4, 4, 3, 3, 3, 3, 3, 2, 2,     # 11-20
                 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,     # 21-30
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,     # 31-40
                 1, 1, 1, 1, 1],                    # 41-45
    )[0]
    txn_at   = txn_time(raised - timedelta(days=txn_days_back))

    # PaySim-style: determine type; fraud concentrates on CASH_OUT / TRANSFER
    if case["dispute_reason"] == "Unauthorised transaction":
        txn_type = random.choice(["CASH_OUT", "TRANSFER"])
    elif case["dispute_reason"] == "Cancelled recurring transaction":
        txn_type = "DEBIT"
    else:
        txn_type = random.choices(
            PAYSIM_TYPES,
            weights=[5, 20, 15, 50, 10]  # PAYMENT most common for retail
        )[0]

    # Balance tracking (PaySim style)
    old_balance = round(random.uniform(100, 8000), 2)
    new_balance = round(max(0, old_balance - case["claim_amount"]), 2)
    dest_old    = round(random.uniform(0, 5000), 2)
    dest_new    = round(dest_old + case["claim_amount"], 2)

    authorised  = case["dispute_reason"] != "Unauthorised transaction" or random.random() > 0.3
    settled     = authorised and random.random() > 0.04
    step        = txn_days_back * 24 + txn_at.hour   # PaySim step (hours elapsed)

    # 3DS / ECI (IEEE-CIS calibrated)
    eci_key = random.choices(
        list(ECI_VALUES.keys()),
        weights=[40, 30, 20, 5, 5]
    )[0]
    eci = ECI_VALUES[eci_key]

    # Fraud indicators
    is_fraud    = case["dispute_reason"] == "Unauthorised transaction"
    is_flagged  = is_fraud and case["claim_amount"] > 200000  # PaySim threshold

    # Duplicate transaction
    is_duplicate = case["dispute_reason"] == "Duplicate charge"

    merchant_name = fake.company()

    record = {
        "transaction_id":         uid(),
        "case_id":                case["case_id"],

        # PaySim fields
        "step":                   step,
        "type":                   txn_type,
        "amount":                 case["claim_amount"],
        "name_orig":              f"C{case['customer_id'][:8].replace('-','')}",
        "old_balance_orig":       old_balance,
        "new_balance_orig":       new_balance,
        "name_dest":              f"M{case['merchant_id'][:8].replace('-','')}",
        "old_balance_dest":       dest_old,
        "new_balance_dest":       dest_new,
        "is_fraud":               is_fraud,
        "is_flagged_fraud":       is_flagged,

        # Standard card fields
        "txn_reference":          f"TXN{random.randint(10**11, 10**12-1)}",
        "timestamp":              iso(txn_at),
        "currency":               case["currency"],
        "merchant_id":            case["merchant_id"],
        "merchant_name":          merchant_name,
        "merchant_category":      case["mcc_description"],
        "mcc_code":               case["mcc_code"],
        "merchant_city":          fake.city(),
        "merchant_state":         fake.state_abbr(),
        "merchant_country":       fake.country_code(),
        "merchant_zip":           fake.zipcode(),
        "card_network":           case["card_network"],
        "card_last4":             str(random.randint(1000, 9999)),
        "card_type":              case["card_type"],
        "channel":                random.choice(["Online", "In-Store", "MOTO", "Contactless", "Mobile App"]),

        # Auth
        "authorisation_code":     f"AUTH{random.randint(100000,999999)}" if authorised else None,
        "authorised":             authorised,
        "settled":                settled,
        "settlement_date":        iso(txn_at + timedelta(days=random.randint(1, 3))) if settled else None,
        "eci_indicator":          eci["eci"],
        "eci_label":              eci["label"],
        "cavv":                   uuid.uuid4().hex[:20].upper() if eci["eci"] in ("05","02") else None,
        "three_ds_version":       "2.2" if eci["eci"] in ("05","06","02","01") else None,

        # Zenodo digital payment fields
        "reference_number":       f"REF{random.randint(10**9,10**10-1)}",
        "capture_number":         f"CAP{random.randint(10**8,10**9-1)}",
        "receipt_number":         f"RCT-{random.randint(1000000,9999999)}",
        "journal_type":           random.choice(["DR", "CR"]),
        "channel_reference_number": f"CHR{random.randint(10**9,10**10-1)}",
        "is_verified":            authorised,
        "paying_at":              iso(txn_at),

        "is_duplicate":           is_duplicate,
        "reversal":               False,
        "reversal_reference":     None,
        "provenance":             "CORE_BANKING",
        "version":                1,
    }

    results = [record]

    if is_duplicate:
        dup = dict(record)
        dup["transaction_id"]      = uid()
        dup["txn_reference"]       = f"TXN{random.randint(10**11,10**12-1)}"
        dup["timestamp"]           = iso(txn_at + timedelta(minutes=random.randint(1, 45)))
        dup["authorisation_code"]  = f"AUTH{random.randint(100000,999999)}"
        dup["reference_number"]    = f"REF{random.randint(10**9,10**10-1)}"
        dup["capture_number"]      = f"CAP{random.randint(10**8,10**9-1)}"
        results.append(dup)

    return results


def gen_transactions(cases):
    all_txns = []
    for c in cases:
        all_txns.extend(gen_transaction(c))
    return all_txns


# ═══════════════════════════════════════════════════════════════════════════════
# 3. CUSTOMER STATEMENTS  (CFPB narrative style)
# ═══════════════════════════════════════════════════════════════════════════════

STMT_TEMPLATES = {
    "Item not received": (
        "On {order_date} I placed an order for {item} costing {currency} {amount} from {merchant} "
        "via their {channel}. The expected delivery was {delivery_date}. As of today, {days_since} days "
        "later, I have not received any goods or shipping notification. I contacted the merchant on "
        "{contact_date} and received no satisfactory resolution. I am requesting a full chargeback."
    ),
    "Item significantly not as described": (
        "I purchased {item} ({currency} {amount}) from {merchant} on {order_date}. Upon delivery on "
        "{delivery_date} I found the product to be materially different from the listing: {discrepancy}. "
        "The merchant has refused to accept a return. I am disputing this charge under 'not as described'."
    ),
    "Unauthorised transaction": (
        "I did not authorise the {currency} {amount} charge from {merchant} appearing on my statement "
        "dated {txn_date}. I had my card in my possession. My last legitimate use was at {last_legit}. "
        "I believe my card details were compromised. I request an immediate investigation and reversal."
    ),
    "Duplicate charge": (
        "I authorised a single payment of {currency} {amount} to {merchant} on {order_date}. "
        "My statement shows two identical charges on {txn_date} and {txn_date2}. Only one was "
        "authorised. Please reverse the duplicate."
    ),
    "Service not provided": (
        "I paid {currency} {amount} to {merchant} on {order_date} for {item}. Despite repeated "
        "follow-ups on {contact_date} and {contact_date2}, the service was never delivered. "
        "I request a full chargeback."
    ),
    "Credit not processed": (
        "I returned {item} to {merchant} on {delivery_date} with tracking number {tracking}. The "
        "merchant acknowledged receipt but the credit of {currency} {amount} has not appeared on my "
        "account after {days_since} days. Please apply the credit."
    ),
    "Cancelled recurring transaction": (
        "I cancelled my subscription with {merchant} by {cancel_method} on {cancel_date}, confirmed by "
        "reference {cancel_ref}. Despite this, a charge of {currency} {amount} was applied on {txn_date}. "
        "This is an unauthorised recurring charge post-cancellation."
    ),
}

DISCREPANCIES = [
    "the colour was entirely different from the listing photos",
    "the dimensions were 40% smaller than advertised",
    "the material was synthetic rather than the advertised genuine leather",
    "the item was a counterfeit with visible quality defects",
    "the product was a different model number with fewer features",
]

CANCEL_METHODS = ["phone call", "email", "online portal", "in-app cancellation", "written letter"]

def gen_customer_statement(case, txn):
    raised   = datetime.fromisoformat(case["raised_at"].replace("Z", ""))
    order_dt = raised - timedelta(days=random.randint(7, 40))
    delivery_dt = order_dt + timedelta(days=random.randint(3, 15))
    contact_dt  = raised - timedelta(days=random.randint(1, 7))
    contact_dt2 = contact_dt + timedelta(days=3)
    txn_dt   = datetime.fromisoformat(txn["timestamp"].replace("Z","")) if txn else raised - timedelta(days=5)
    days_since = (raised - delivery_dt).days

    narrative = STMT_TEMPLATES.get(
        case["dispute_reason"], STMT_TEMPLATES["Item not received"]
    ).format(
        order_date    = order_dt.strftime("%d %b %Y"),
        delivery_date = delivery_dt.strftime("%d %b %Y"),
        txn_date      = txn_dt.strftime("%d %b %Y"),
        txn_date2     = (txn_dt + timedelta(minutes=30)).strftime("%d %b %Y"),
        contact_date  = contact_dt.strftime("%d %b %Y"),
        contact_date2 = contact_dt2.strftime("%d %b %Y"),
        cancel_date   = (raised - timedelta(days=random.randint(5, 60))).strftime("%d %b %Y"),
        cancel_date2  = (raised - timedelta(days=3)).strftime("%d %b %Y"),
        cancel_method = random.choice(CANCEL_METHODS),
        cancel_ref    = f"CXL-{random.randint(100000,999999)}",
        item          = fake.catch_phrase(),
        merchant      = fake.company(),
        amount        = case["claim_amount"],
        currency      = case["currency"],
        channel       = random.choice(["website", "mobile app", "telephone order"]),
        discrepancy   = random.choice(DISCREPANCIES),
        days_since    = max(1, days_since),
        tracking      = f"1Z{random.randint(10**14,10**15-1)}",
        last_legit    = fake.company(),
    )

    return {
        "statement_id":    uid(),
        "case_id":         case["case_id"],
        "customer_id":     case["customer_id"],
        "submitted_at":    case["raised_at"],
        "channel":         random.choice(["Online Portal", "Phone", "Branch", "Mobile App"]),
        "dispute_reason":  case["dispute_reason"],
        "narrative":       narrative,
        "claimed_amount":  case["claim_amount"],
        "currency":        case["currency"],
        "attachments":     random.sample(
                               ["screenshot.png", "order_confirmation.pdf",
                                "email_thread.eml", "bank_statement.pdf",
                                "photo_of_item.jpg", "return_receipt.pdf"],
                               k=random.randint(0, 3)),
        # CFPB fields
        "consumer_consent_provided": True,
        "submitted_via":   random.choice(["Web", "Phone", "Referral", "Postal mail"]),
        "provenance":      "CUSTOMER_PORTAL",
        "version":         1,
        "superseded_by":   None,
    }


def gen_customer_statements(cases, transactions):
    txn_map = {}
    for t in transactions:
        if t["case_id"] not in txn_map:
            txn_map[t["case_id"]] = t
    return [gen_customer_statement(c, txn_map.get(c["case_id"])) for c in cases]


# ═══════════════════════════════════════════════════════════════════════════════
# 4. MERCHANT RECORDS
# ═══════════════════════════════════════════════════════════════════════════════

def gen_merchant_record(case):
    raised   = datetime.fromisoformat(case["raised_at"].replace("Z", ""))
    order_dt = raised - timedelta(days=random.randint(7, 40))
    fulfilled = case["dispute_reason"] not in ["Item not received", "Service not provided"]

    items = [{
        "sku":         f"SKU-{random.randint(1000,9999)}",
        "description": fake.catch_phrase(),
        "qty":         random.randint(1, 3),
        "unit_price":  round(case["claim_amount"] / random.randint(1, 3), 2),
        "category":    case["mcc_description"],
    }]

    refund_issued = case["dispute_reason"] == "Credit not processed" and random.random() > 0.4

    return {
        "merchant_record_id":  uid(),
        "case_id":             case["case_id"],
        "merchant_id":         case["merchant_id"],
        "merchant_name":       fake.company(),
        "merchant_category":   case["mcc_description"],
        "mcc_code":            case["mcc_code"],
        "order_id":            f"ORD-{random.randint(100000,999999)}",
        "order_date":          iso(order_dt),
        "order_status":        random.choice(
                                   ["Delivered", "Dispatched", "Processing",
                                    "Cancelled", "Refunded", "Returned"]),
        "items":               items,
        "subtotal":            case["claim_amount"],
        "tax_rate":            0.08,
        "tax_amount":          round(case["claim_amount"] * 0.08, 2),
        "total_charged":       round(case["claim_amount"] * 1.08, 2),
        "currency":            case["currency"],
        "fulfilled":           fulfilled,
        "fulfilment_date":     iso(order_dt + timedelta(days=random.randint(1, 3))) if fulfilled else None,
        "refund_issued":       refund_issued,
        "refund_amount":       case["claim_amount"] if refund_issued else None,
        "refund_reference":    f"REF-{random.randint(100000,999999)}" if refund_issued else None,
        "refund_date":         iso(raised - timedelta(days=random.randint(1, 5))) if refund_issued else None,
        "merchant_response":   random.choice([
            "Order delivered as per tracking records.",
            "Item dispatched; tracking number provided to customer.",
            "Refund already processed per RMA.",
            "Subscription cancelled post billing cycle; charge was valid.",
            "Customer signed for delivery.",
            "Goods matched product description at time of listing.",
        ]),
        "merchant_contested":  case["merchant_contested"],
        "received_at":         case["raised_at"],
        "provenance":          "MERCHANT_PORTAL",
        "version":             1,
        "superseded_by":       None,
    }


def gen_merchant_records(cases):
    return [gen_merchant_record(c) for c in cases]


# ═══════════════════════════════════════════════════════════════════════════════
# 5. RECEIPTS
# ═══════════════════════════════════════════════════════════════════════════════

def gen_receipts(cases, merchant_records):
    mr_map = {r["case_id"]: r for r in merchant_records}
    receipts = []
    for c in cases:
        mr   = mr_map.get(c["case_id"])
        raised = datetime.fromisoformat(c["raised_at"].replace("Z", ""))
        issued = raised - timedelta(days=random.randint(8, 40))
        receipts.append({
            "receipt_id":       uid(),
            "case_id":          c["case_id"],
            "order_id":         mr["order_id"] if mr else f"ORD-{random.randint(100000,999999)}",
            "merchant_id":      c["merchant_id"],
            "issued_at":        iso(issued),
            "receipt_number":   mr["items"][0] and f"RCT-{random.randint(1000000,9999999)}",
            "line_items":       mr["items"] if mr else [],
            "subtotal":         c["claim_amount"],
            "tax_rate":         0.08,
            "tax_amount":       round(c["claim_amount"] * 0.08, 2),
            "total":            round(c["claim_amount"] * 1.08, 2),
            "currency":         c["currency"],
            "payment_method":   f"{c['card_type']} {c['card_network']} ****{random.randint(1000,9999)}",
            "format":           random.choice(["PDF", "HTML", "Image"]),
            "hash_sha256":      uuid.uuid4().hex + uuid.uuid4().hex[:32],
            "provenance":       "MERCHANT_RECEIPT_SYSTEM",
            "version":          1,
        })
    return receipts


# ═══════════════════════════════════════════════════════════════════════════════
# 6. DELIVERY RECORDS  (Olist-calibrated timelines)
# ═══════════════════════════════════════════════════════════════════════════════

def gen_delivery_record(case, merchant_record):
    raised   = datetime.fromisoformat(case["raised_at"].replace("Z", ""))
    carrier_name = random.choice(list(CARRIERS.keys()))
    carrier  = CARRIERS[carrier_name]

    order_dt  = raised - timedelta(days=random.randint(10, 40))
    shipped_at = order_dt + timedelta(hours=random.randint(4, 48))
    transit_days = random.randint(carrier["min_days"], carrier["max_days"])
    expected  = shipped_at + timedelta(days=transit_days)

    # Olist-calibrated late probability
    late = random.random() < carrier["late_prob"]
    delay_days = random.randint(1, 7) if late else 0
    actual = expected + timedelta(days=delay_days)

    # For "Item not received" disputes: delivery often failed/lost
    if case["dispute_reason"] == "Item not received":
        dlv_status = random.choice(["Failed Delivery", "Lost", "In Transit", "Returned to Sender"])
        delivered  = False
    elif actual > raised:
        dlv_status = "In Transit"
        delivered  = False
    else:
        dlv_status = "Delivered"
        delivered  = True

    signature = fake.name() if delivered and random.random() > 0.35 else None
    pod_photo = f"pod_{uid()[:8]}.jpg" if delivered and random.random() > 0.4 else None

    events = [
        {"event": "Order Received",  "timestamp": iso(order_dt),                           "location": fake.city()},
        {"event": "Picked & Packed", "timestamp": iso(order_dt + timedelta(hours=6)),      "location": fake.city()},
        {"event": "Dispatched",      "timestamp": iso(shipped_at),                          "location": fake.city()},
        {"event": "In Transit",      "timestamp": iso(shipped_at + timedelta(days=1)),      "location": fake.city()},
    ]
    if delivered:
        events.append({"event": "Out for Delivery", "timestamp": iso(actual - timedelta(hours=3)), "location": fake.city()})
        events.append({"event": "Delivered",         "timestamp": iso(actual),                      "location": fake.city()})
    elif dlv_status == "Failed Delivery":
        events.append({"event": "Failed Delivery Attempt", "timestamp": iso(actual), "location": fake.city()})
        events.append({"event": "Return to Sender Initiated", "timestamp": iso(actual + timedelta(days=2)), "location": fake.city()})
    elif dlv_status == "Lost":
        events.append({"event": "Last Scan", "timestamp": iso(shipped_at + timedelta(days=2)), "location": fake.city()})

    return {
        "delivery_id":          uid(),
        "case_id":              case["case_id"],
        "order_id":             merchant_record["order_id"] if merchant_record else f"ORD-{random.randint(100000,999999)}",
        "carrier":              carrier_name,
        "tracking_number":      f"{random.choice(['1Z','JD','GM','LX'])}{random.randint(10**14,10**15-1)}",
        "service_level":        random.choice(["Standard", "Express", "Priority", "Economy"]),
        "shipped_at":           iso(shipped_at),
        "expected_by":          iso(expected),
        "actual_delivery_at":   iso(actual) if delivered else None,
        "arrived_late":         late,
        "delay_days":           delay_days,
        "status":               dlv_status,
        "delivered":            delivered,
        "delivery_address":     fake.address().replace("\n", ", "),
        "delivery_city":        fake.city(),
        "delivery_state":       fake.state_abbr(),
        "delivery_zip":         fake.zipcode(),
        "delivery_country":     fake.country_code(),
        "signature_obtained":   signature,
        "proof_of_delivery_url":pod_photo,
        "events":               events,
        "weight_kg":            round(random.uniform(0.1, 20), 2),
        "dimensions_cm":        f"{random.randint(5,60)}x{random.randint(5,40)}x{random.randint(2,30)}",
        "provenance":           "CARRIER_API",
        "version":              1,
    }


def gen_delivery_records(cases, merchant_records):
    mr_map = {r["case_id"]: r for r in merchant_records}
    return [gen_delivery_record(c, mr_map.get(c["case_id"])) for c in cases]


# ═══════════════════════════════════════════════════════════════════════════════
# 7. AUTHENTICATION EVENTS  (IEEE-CIS calibrated)
# ═══════════════════════════════════════════════════════════════════════════════

def gen_auth_event(case, txn):
    txn_ts = datetime.fromisoformat(txn["timestamp"].replace("Z","")) if txn \
             else datetime.fromisoformat(case["raised_at"].replace("Z","")) - timedelta(days=3)

    # Geo-mismatch: more likely for unauthorised transactions
    geo_mismatch = (case["dispute_reason"] == "Unauthorised transaction") and (random.random() > 0.45)
    customer_state = fake.state_abbr()
    txn_state = fake.state_abbr() if geo_mismatch else customer_state

    # Device / browser fields (Fraud eCommerce dataset)
    device_cat  = random.choice(DEVICE_CATS)
    browser     = random.choice(BROWSERS)
    os_type     = random.choice(OS_TYPES)
    device_id   = uuid.uuid4().hex[:16]
    ip          = fake.ipv4_public()

    # IP country mismatch (additional fraud signal)
    ip_country_mismatch = geo_mismatch and random.random() > 0.5

    auth_method = txn.get("eci_label", "Non-3DS channel") if txn else "PIN"
    success     = case["dispute_reason"] != "Unauthorised transaction" or random.random() > 0.55

    # Risk score (higher for unauthorised)
    base_risk   = 0.7 if case["dispute_reason"] == "Unauthorised transaction" else 0.15
    risk_score  = round(min(1.0, max(0.0, random.gauss(base_risk, 0.15))), 4)
    risk_decision = "DECLINE" if risk_score > 0.85 else ("REFER" if risk_score > 0.65 else "APPROVE")

    return {
        "auth_event_id":        uid(),
        "case_id":              case["case_id"],
        "transaction_id":       txn["transaction_id"] if txn else None,
        "event_type":           random.choice(["AUTHORISATION", "3DS_CHALLENGE",
                                               "PIN_VERIFY", "BIOMETRIC_VERIFY", "OTP_VERIFY"]),
        "timestamp":            iso(txn_ts),

        # 3DS (IEEE-CIS)
        "eci_indicator":        txn.get("eci_indicator") if txn else "07",
        "eci_label":            txn.get("eci_label") if txn else "Non-3DS channel",
        "three_ds_version":     txn.get("three_ds_version") if txn else None,
        "cavv":                 txn.get("cavv") if txn else None,
        "authentication_result":auth_method,
        "success":              success,
        "failure_reason":       None if success else random.choice(
                                    ["Wrong PIN", "3DS timeout", "Biometric mismatch",
                                     "OTP expired", "Card blocked"]),

        # Device / browser (Fraud eCommerce)
        "device_type":          device_cat,
        "device_id":            device_id,
        "browser":              browser,
        "os":                   os_type,
        "user_agent":           f"Mozilla/5.0 ({os_type}) {browser}/120.0",
        "screen_resolution":    random.choice(["1920x1080","1366x768","375x812","390x844","2560x1440"]),

        # Identity / geo
        "ip_address":           ip,
        "ip_country":           "US" if not ip_country_mismatch else fake.country_code(),
        "ip_country_mismatch":  ip_country_mismatch,
        "customer_state":       customer_state,
        "transaction_state":    txn_state,
        "geo_mismatch":         geo_mismatch,
        "customer_id":          case["customer_id"],
        "customer_email_domain":random.choice(["gmail.com","yahoo.com","outlook.com","hotmail.com",
                                               "icloud.com","proton.me"]),

        # Risk
        "risk_score":           risk_score,
        "risk_decision":        risk_decision,
        "velocity_last_1h":     random.randint(0, 5),
        "velocity_last_24h":    random.randint(0, 20),

        "provenance":           "AUTH_ENGINE",
        "version":              1,
    }


def gen_auth_events(cases, transactions):
    txn_map = {t["case_id"]: t for t in transactions if not t.get("is_duplicate")}
    return [gen_auth_event(c, txn_map.get(c["case_id"])) for c in cases]


# ═══════════════════════════════════════════════════════════════════════════════
# 8. CORRESPONDENCE
# ═══════════════════════════════════════════════════════════════════════════════

CORR_TEMPLATES = [
    {
        "direction": "BANK_TO_CUSTOMER",
        "subject":   "Dispute {case_number} received – next steps",
        "body": (
            "Dear {name},\n\nThank you for contacting us. We have registered dispute {case_number} "
            "for {currency} {amount} with {merchant}.\n\nWe will investigate and aim to provide an update "
            "within 5 business days. In the meantime provisional credit may be applied to your account "
            "per Regulation E guidelines.\n\nRef: {case_number}\nDisputes Team"
        ),
    },
    {
        "direction": "BANK_TO_MERCHANT",
        "subject":   "Retrieval Request – {case_number} (Reason {reason_code})",
        "body": (
            "Dear Merchant,\n\nWe are investigating dispute {case_number} under reason code {reason_code} "
            "({reason_label}).\n\nPlease provide within 10 calendar days: order confirmation, "
            "proof of delivery, signed receipts, and any correspondence with the cardholder.\n\n"
            "Failure to respond may result in automatic chargeback.\n\nDisputes Operations"
        ),
    },
    {
        "direction": "MERCHANT_TO_BANK",
        "subject":   "RE: Retrieval Request – {case_number}",
        "body": (
            "Please find attached our response to dispute {case_number}.\n\n"
            "Order {order_id} was fulfilled on {fulfil_date}. Delivery was confirmed by carrier "
            "with tracking reference {tracking}. We believe the dispute is not valid and "
            "request representment.\n\nMerchant Risk Team"
        ),
    },
    {
        "direction": "CUSTOMER_TO_BANK",
        "subject":   "Additional information – dispute {case_number}",
        "body": (
            "Hello,\n\nFurther to my dispute {case_number} I am providing the attached evidence.\n\n"
            "The tracking page still shows '{delivery_status}' and I have heard nothing from the merchant. "
            "Please expedite the investigation.\n\nRegards,\n{name}"
        ),
    },
    {
        "direction": "BANK_TO_CUSTOMER",
        "subject":   "Update on dispute {case_number}",
        "body": (
            "Dear {name},\n\nWe have received the merchant's response to dispute {case_number}. "
            "Our team is reviewing the evidence. We will update you within 3 business days.\n\n"
            "Disputes Team"
        ),
    },
]

def gen_correspondence(cases, merchant_records):
    mr_map = {r["case_id"]: r for r in merchant_records}
    corrs  = []
    for c in cases:
        mr     = mr_map.get(c["case_id"])
        raised = datetime.fromisoformat(c["raised_at"].replace("Z", ""))
        name   = fake.name()
        num    = random.randint(2, 5)
        selected = random.sample(CORR_TEMPLATES, min(num, len(CORR_TEMPLATES)))
        for idx, tmpl in enumerate(selected):
            sent = raised + timedelta(days=idx * random.randint(1, 4),
                                      hours=random.randint(0, 8))
            body = tmpl["body"].format(
                case_number      = c["case_number"],
                name             = name,
                currency         = c["currency"],
                amount           = c["claim_amount"],
                merchant         = mr["merchant_name"] if mr else fake.company(),
                reason_code      = c["reason_code"],
                reason_label     = c["reason_code_label"],
                order_id         = mr["order_id"] if mr else "N/A",
                fulfil_date      = (raised - timedelta(days=5)).strftime("%d %b %Y"),
                tracking         = f"1Z{random.randint(10**14,10**15-1)}",
                delivery_status  = random.choice(["In Transit", "No information available",
                                                  "Failed Delivery Attempt"]),
            )
            corrs.append({
                "correspondence_id": uid(),
                "case_id":           c["case_id"],
                "case_number":       c["case_number"],
                "channel":           random.choice(CHANNELS),
                "direction":         tmpl["direction"],
                "sent_at":           iso(sent),
                "from_party":        tmpl["direction"].split("_TO_")[0].title(),
                "to_party":          tmpl["direction"].split("_TO_")[1].title(),
                "subject":           tmpl["subject"].format(
                                         case_number=c["case_number"],
                                         reason_code=c["reason_code"]),
                "body":              body,
                "attachments":       random.sample(
                                         ["order_confirmation.pdf", "pod.jpg",
                                          "tracking_screenshot.png", "invoice.pdf",
                                          "merchant_response.pdf", "customer_photo.jpg"],
                                         k=random.randint(0, 2)),
                "read_at":           iso(sent + timedelta(hours=random.randint(1, 48))),
                "provenance":        "CORRESPONDENCE_SYSTEM",
                "version":           1,
                "superseded_by":     None,
            })
    return corrs


# ═══════════════════════════════════════════════════════════════════════════════
# 9. AUDIT TRAIL
# ═══════════════════════════════════════════════════════════════════════════════

AUDIT_ACTIONS = [
    ("Dispute raised by customer",            "HUMAN_ANALYST"),
    ("Transaction event retrieved",           "AI_AGENT"),
    ("Customer statement recorded",           "SYSTEM"),
    ("Merchant retrieval request sent",       "SYSTEM"),
    ("Authentication event retrieved",        "AI_AGENT"),
    ("Delivery record retrieved",             "AI_AGENT"),
    ("Evidence gap identified",               "AI_AGENT"),
    ("Contradiction detected",                "AI_AGENT"),
    ("Next-best-evidence selected",           "AI_AGENT"),
    ("Specialist review assigned",            "SYSTEM"),
    ("Human decision recorded",               "HUMAN_MANAGER"),
    ("Merchant response received",            "SYSTEM"),
    ("Evidence reconciled",                   "AI_AGENT"),
    ("Outcome recommendation prepared",       "AI_AGENT"),
    ("Case status updated",                   "HUMAN_ANALYST"),
    ("Resolution progressed",                 "HUMAN_MANAGER"),
    ("Audit checkpoint",                      "SYSTEM"),
]

def gen_audit_trail(cases):
    entries = []
    for c in cases:
        base = datetime.fromisoformat(c["raised_at"].replace("Z", ""))
        n    = random.randint(5, 14)
        for i in range(n):
            action_label, default_actor = AUDIT_ACTIONS[i % len(AUDIT_ACTIONS)]
            ts = base + timedelta(hours=i * random.randint(2, 18))
            entries.append({
                "audit_id":         uid(),
                "case_id":          c["case_id"],
                "case_number":      c["case_number"],
                "sequence":         i + 1,
                "timestamp":        iso(ts),
                "action":           action_label,
                "actor_type":       default_actor,
                "actor_id":         uid()[:8] if "HUMAN" in default_actor else f"agent-v2",
                "description":      f"{action_label} for case {c['case_number']}.",
                "entity_type":      random.choice(["DISPUTE", "TRANSACTION", "MERCHANT_RECORD",
                                                   "DELIVERY", "CORRESPONDENCE", "AUTH_EVENT"]),
                "entity_id":        uid(),
                "previous_state":   DISPUTE_STATUSES[max(0, i // 4 - 1)],
                "new_state":        DISPUTE_STATUSES[min(len(DISPUTE_STATUSES)-1, i // 4)],
                "ai_inference":     default_actor == "AI_AGENT",
                "human_approved":   "HUMAN" in default_actor,
                "source_of_record": random.choice(["RECORDED_FACT", "AI_INFERENCE",
                                                   "USER_INPUT", "AUTOMATED_ACTION",
                                                   "HUMAN_DECISION"]),
                "provenance":       "AUDIT_SERVICE",
            })
    return entries


# ═══════════════════════════════════════════════════════════════════════════════
# 10. FINALE INJECT  (5 contradiction types × multiple cases)
# ═══════════════════════════════════════════════════════════════════════════════

CONTRADICTION_TYPES = [
    {
        "type":              "DELIVERY_PROOF_CONTRADICTS_NOT_RECEIVED",
        "customer_claim":    "Customer stated item was never received and no delivery was attempted.",
        "merchant_rebuttal": "Merchant provides GPS-timestamped proof-of-delivery photo and carrier "
                             "signature log showing item was delivered and signed for by a household member.",
        "evidence_type":     "proof_of_delivery_photo",
        "impact":            "HIGH",
        "reassess_targets":  ["customer_statement", "delivery_record", "outcome_recommendation"],
        "applicable_reason": "Item not received",
    },
    {
        "type":              "CANCELLATION_AFTER_CHARGE_DATE",
        "customer_claim":    "Customer stated subscription was cancelled before the disputed charge.",
        "merchant_rebuttal": "Merchant submits system log showing cancellation request was received "
                             "AFTER the billing cycle had already processed.",
        "evidence_type":     "cancellation_timestamp_log",
        "impact":            "HIGH",
        "reassess_targets":  ["customer_statement", "correspondence", "outcome_recommendation"],
        "applicable_reason": "Cancelled recurring transaction",
    },
    {
        "type":              "ITEM_MATCHES_LISTING_AT_PURCHASE",
        "customer_claim":    "Customer claimed item received was significantly not as described.",
        "merchant_rebuttal": "Merchant provides timestamped product listing snapshot at time of purchase "
                             "with verified images matching the shipped item, plus third-party inspection report.",
        "evidence_type":     "product_listing_snapshot_with_inspection",
        "impact":            "MEDIUM",
        "reassess_targets":  ["customer_statement", "merchant_record", "outcome_recommendation"],
        "applicable_reason": "Item significantly not as described",
    },
    {
        "type":              "DEVICE_FINGERPRINT_MATCHES_CUSTOMER",
        "customer_claim":    "Customer claimed transaction was entirely unauthorised.",
        "merchant_rebuttal": "Merchant provides server-side session log showing the customer's registered "
                             "device fingerprint, billing address, and successful 3DS2 biometric verification.",
        "evidence_type":     "session_log_with_device_and_3ds_match",
        "impact":            "HIGH",
        "reassess_targets":  ["customer_statement", "auth_event", "transaction", "outcome_recommendation"],
        "applicable_reason": "Unauthorised transaction",
    },
    {
        "type":              "REFUND_ALREADY_POSTED_BEFORE_DISPUTE",
        "customer_claim":    "Customer stated no refund was received for the returned item.",
        "merchant_rebuttal": "Merchant provides bank ledger reference confirming refund was posted "
                             "to the card 3 days before the dispute was raised.",
        "evidence_type":     "merchant_refund_ledger",
        "impact":            "MEDIUM",
        "reassess_targets":  ["customer_statement", "merchant_record", "outcome_recommendation"],
        "applicable_reason": "Credit not processed",
    },
]

def build_inject(case, customer_statement, merchant_record):
    raised   = datetime.fromisoformat(case["raised_at"].replace("Z", ""))
    inject_at = raised + timedelta(days=random.randint(12, 30))

    reason    = case["dispute_reason"]
    ct_options = [ct for ct in CONTRADICTION_TYPES if ct["applicable_reason"] == reason]
    ct = random.choice(ct_options) if ct_options else random.choice(CONTRADICTION_TYPES)

    return {
        "inject_id":                uid(),
        "case_id":                  case["case_id"],
        "case_number":              case["case_number"],
        "received_at":              iso(inject_at),
        "arrived_late":             True,
        "business_days_after_raise":random.randint(8, 22),
        "case_status_at_arrival":   random.choice(["Under Review", "Specialist Review",
                                                   "Evidence Gathering"]),
        "submitted_by":             "MERCHANT",
        "merchant_id":              case["merchant_id"],

        "evidence_type":            ct["evidence_type"],
        "evidence_reference":       f"EVD-{uid()[:12].upper()}",
        "evidence_payload": {
            "file":         f"{ct['evidence_type']}_{uid()[:8]}.pdf",
            "hash_sha256":  uuid.uuid4().hex + uuid.uuid4().hex[:32],
            "description":  ct["merchant_rebuttal"],
            "verified":     False,
            "received_via": random.choice(["Merchant Portal", "Email Attachment",
                                           "Secure API Upload", "Fax"]),
        },

        "contradiction_type":       ct["type"],
        "original_customer_claim":  ct["customer_claim"],
        "merchant_rebuttal":        ct["merchant_rebuttal"],
        "impact_level":             ct["impact"],
        "applicable_dispute_reason":ct["applicable_reason"],
        "reason_code":              case["reason_code"],

        "reassess_targets":         ct["reassess_targets"],
        "conclusions_invalidated": [
            f"Outcome recommendation based on '{ct['customer_claim'][:80]}...' "
            "is now stale and must be re-evaluated."
        ],

        "required_agent_actions": [
            "Ingest new evidence into case evidence set (versioned)",
            "Mark prior conclusions referencing contradicted evidence as STALE",
            "Re-run evidence gap analysis against updated state",
            "Re-evaluate outcome recommendation with updated evidence weight",
            "Compute and store delta summary (what changed, why)",
            "Surface change delta to assigned human reviewer",
            "Append FINALE_INJECT event to audit trail with full provenance",
            "Trigger targeted re-evaluation (not full case restart)",
            "Set change_visible = true and reviewer_notified = true",
        ],

        # Agent state tracking (to be populated by the agent)
        "change_visible":           False,
        "reviewer_notified":        False,
        "delta_summary":            None,
        "stale_conclusions":        [],
        "reprocessing_status":      "PENDING",

        "provenance":               "MERCHANT_PORTAL_LATE_SUBMISSION",
        "version":                  1,
        "superseded_prior_version": {
            "merchant_record_id":   merchant_record["merchant_record_id"] if merchant_record else None,
            "version":              1,
        },
    }


def gen_finale_injects(cases, customer_statements, merchant_records):
    cs_map = {s["case_id"]: s for s in customer_statements}
    mr_map = {r["case_id"]: r for r in merchant_records}
    return [
        build_inject(c, cs_map.get(c["case_id"]), mr_map.get(c["case_id"]))
        for c in cases if c.get("finale_inject")
    ]


# ═══════════════════════════════════════════════════════════════════════════════
# 11. HAND-CRAFTED SHOWCASE CASES (for judge demos)
# ═══════════════════════════════════════════════════════════════════════════════

def gen_showcase_cases():
    """
    5 fully scripted, narratively coherent cases designed for live demos.
    Each has precise contradictions, exact timelines, and dramatic finale injects.
    """
    base_ts = NOW - timedelta(days=45)

    showcase = []

    # ── Case SC-001: GPS delivery photo surfaces after "not received" decision ──
    c1_id   = uid()
    c1_cust = uid()
    c1_merch= uid()
    c1 = {
        "case_id": c1_id, "case_number": "DSP-SC-001",
        "raised_at": iso(base_ts), "deadline": iso(base_ts + timedelta(days=120)),
        "status": "Specialist Review",
        "dispute_reason": "Item not received",
        "reason_code": "13.1", "reason_code_label": "Merchandise/Services Not Received",
        "reason_code_network": "Visa",
        "claim_amount": 289.99, "currency": "USD",
        "card_network": "Visa", "card_type": "Credit",
        "merchant_category_key": "electronics",
        "mcc_code": "5732", "mcc_description": "Electronics Stores",
        "customer_id": c1_cust, "merchant_id": c1_merch,
        "friendly_fraud": True, "fraud_type": "Friendly Fraud",
        "company_response": "In progress", "timely_response": True, "consumer_disputed": False,
        "merchant_contested": True, "merchant_win": None,
        "finale_inject": True,
        "created_at": iso(base_ts), "updated_at": iso(NOW),
        "_showcase": True, "_scenario": "GPS delivery photo vs not-received claim",
    }
    showcase.append(c1)

    # ── Case SC-002: 3DS biometric log vs "I never made this transaction" ──
    c2_id   = uid()
    c2_cust = uid()
    c2_merch= uid()
    c2 = {
        "case_id": c2_id, "case_number": "DSP-SC-002",
        "raised_at": iso(base_ts + timedelta(days=5)), "deadline": iso(base_ts + timedelta(days=125)),
        "status": "Under Review",
        "dispute_reason": "Unauthorised transaction",
        "reason_code": "10.4", "reason_code_label": "Other Fraud – Card-Absent Environment",
        "reason_code_network": "Visa",
        "claim_amount": 1249.00, "currency": "USD",
        "card_network": "Visa", "card_type": "Credit",
        "merchant_category_key": "travel",
        "mcc_code": "7011", "mcc_description": "Hotels & Lodging",
        "customer_id": c2_cust, "merchant_id": c2_merch,
        "friendly_fraud": False, "fraud_type": "True Fraud",
        "company_response": "In progress", "timely_response": True, "consumer_disputed": False,
        "merchant_contested": True, "merchant_win": None,
        "finale_inject": True,
        "created_at": iso(base_ts + timedelta(days=5)), "updated_at": iso(NOW),
        "_showcase": True, "_scenario": "Device fingerprint + 3DS biometric vs unauthorised claim",
    }
    showcase.append(c2)

    # ── Case SC-003: Cancellation log timestamp proves charge was legitimate ──
    c3_id   = uid()
    c3_cust = uid()
    c3_merch= uid()
    c3 = {
        "case_id": c3_id, "case_number": "DSP-SC-003",
        "raised_at": iso(base_ts + timedelta(days=10)), "deadline": iso(base_ts + timedelta(days=130)),
        "status": "Evidence Gathering",
        "dispute_reason": "Cancelled recurring transaction",
        "reason_code": "13.2", "reason_code_label": "Cancelled Recurring Transaction",
        "reason_code_network": "Visa",
        "claim_amount": 49.99, "currency": "USD",
        "card_network": "Mastercard", "card_type": "Debit",
        "merchant_category_key": "subscription",
        "mcc_code": "7372", "mcc_description": "Prepackaged Software/SaaS",
        "customer_id": c3_cust, "merchant_id": c3_merch,
        "friendly_fraud": True, "fraud_type": "Friendly Fraud",
        "company_response": "In progress", "timely_response": True, "consumer_disputed": True,
        "merchant_contested": True, "merchant_win": None,
        "finale_inject": True,
        "created_at": iso(base_ts + timedelta(days=10)), "updated_at": iso(NOW),
        "_showcase": True, "_scenario": "Cancellation timestamp proves subscription was active",
    }
    showcase.append(c3)

    # ── Case SC-004: Third-party inspection report matches listing ──
    c4_id   = uid()
    c4_cust = uid()
    c4_merch= uid()
    c4 = {
        "case_id": c4_id, "case_number": "DSP-SC-004",
        "raised_at": iso(base_ts + timedelta(days=15)), "deadline": iso(base_ts + timedelta(days=135)),
        "status": "Specialist Review",
        "dispute_reason": "Item significantly not as described",
        "reason_code": "13.3", "reason_code_label": "Not as Described or Defective Merchandise",
        "reason_code_network": "Visa",
        "claim_amount": 179.95, "currency": "USD",
        "card_network": "Visa", "card_type": "Credit",
        "merchant_category_key": "shopping",
        "mcc_code": "5999", "mcc_description": "Miscellaneous Retail",
        "customer_id": c4_cust, "merchant_id": c4_merch,
        "friendly_fraud": True, "fraud_type": "Friendly Fraud",
        "company_response": "In progress", "timely_response": True, "consumer_disputed": False,
        "merchant_contested": True, "merchant_win": None,
        "finale_inject": True,
        "created_at": iso(base_ts + timedelta(days=15)), "updated_at": iso(NOW),
        "_showcase": True, "_scenario": "Product inspection proves item matched listing",
    }
    showcase.append(c4)

    # ── Case SC-005: Refund ledger proves credit posted before dispute raised ──
    c5_id   = uid()
    c5_cust = uid()
    c5_merch= uid()
    c5 = {
        "case_id": c5_id, "case_number": "DSP-SC-005",
        "raised_at": iso(base_ts + timedelta(days=20)), "deadline": iso(base_ts + timedelta(days=140)),
        "status": "Under Review",
        "dispute_reason": "Credit not processed",
        "reason_code": "13.6", "reason_code_label": "Credit Not Processed",
        "reason_code_network": "Visa",
        "claim_amount": 94.50, "currency": "USD",
        "card_network": "Mastercard", "card_type": "Debit",
        "merchant_category_key": "personal_care",
        "mcc_code": "7297", "mcc_description": "Health & Beauty Spas",
        "customer_id": c5_cust, "merchant_id": c5_merch,
        "friendly_fraud": False, "fraud_type": "Merchant Error",
        "company_response": "In progress", "timely_response": True, "consumer_disputed": False,
        "merchant_contested": True, "merchant_win": None,
        "finale_inject": True,
        "created_at": iso(base_ts + timedelta(days=20)), "updated_at": iso(NOW),
        "_showcase": True, "_scenario": "Refund ledger shows credit posted before dispute",
    }
    showcase.append(c5)

    return showcase


# ═══════════════════════════════════════════════════════════════════════════════
# BUNDLE
# ═══════════════════════════════════════════════════════════════════════════════

def build_bundles(cases, transactions, statements, merchant_records,
                  receipts, deliveries, auth_events, correspondence,
                  audit_trail, finale_injects):

    def first(lst, key):
        m = {}
        for x in lst:
            m.setdefault(x[key], x)
        return m

    def many(lst, key):
        m = {}
        for x in lst:
            m.setdefault(x[key], []).append(x)
        return m

    txn_m  = first(transactions,    "case_id")
    stmt_m = first(statements,      "case_id")
    mr_m   = first(merchant_records,"case_id")
    rc_m   = first(receipts,        "case_id")
    dl_m   = first(deliveries,      "case_id")
    au_m   = first(auth_events,     "case_id")
    fi_m   = first(finale_injects,  "case_id")
    co_m   = many(correspondence,   "case_id")
    at_m   = many(audit_trail,      "case_id")

    bundles = []
    for c in cases:
        cid = c["case_id"]
        bundles.append({
            "dispute":            c,
            "transaction":        txn_m.get(cid),
            "customer_statement": stmt_m.get(cid),
            "merchant_record":    mr_m.get(cid),
            "receipt":            rc_m.get(cid),
            "delivery_record":    dl_m.get(cid),
            "auth_event":         au_m.get(cid),
            "correspondence":     co_m.get(cid, []),
            "audit_trail":        at_m.get(cid, []),
            "finale_inject":      fi_m.get(cid),
        })
    return bundles


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    print("\n🏗  Generating synthetic dispute data v2 (real-dataset calibrated) …\n")

    random_cases  = gen_disputes(NUM_RANDOM_CASES)
    showcase      = gen_showcase_cases()
    all_cases     = random_cases + showcase

    transactions  = gen_transactions(all_cases)
    statements    = gen_customer_statements(all_cases, transactions)
    merch_records = gen_merchant_records(all_cases)
    receipts      = gen_receipts(all_cases, merch_records)
    deliveries    = gen_delivery_records(all_cases, merch_records)
    auth_events   = gen_auth_events(all_cases, transactions)
    correspondence= gen_correspondence(all_cases, merch_records)
    audit_trail   = gen_audit_trail(all_cases)
    finale_injects= gen_finale_injects(all_cases, statements, merch_records)

    print("Saving entity files:")
    save("disputes",            all_cases)
    save("transactions",        transactions)
    save("customer_statements", statements)
    save("merchant_records",    merch_records)
    save("receipts",            receipts)
    save("delivery_records",    deliveries)
    save("auth_events",         auth_events)
    save("correspondence",      correspondence)
    save("audit_trail",         audit_trail)
    save("finale_injects",      finale_injects)

    print("\nBuilding master bundles …")
    bundles = build_bundles(all_cases, transactions, statements, merch_records,
                            receipts, deliveries, auth_events, correspondence,
                            audit_trail, finale_injects)
    save("dispute_cases_bundled", bundles)

    inject_n  = sum(1 for c in all_cases if c.get("finale_inject"))
    friendly_n= sum(1 for c in all_cases if c.get("friendly_fraud"))
    showcase_n= len(showcase)

    print(f"""
╔═══════════════════════════════════════════════════════════════╗
║  Synthetic Data v2 — Real-Dataset Calibrated                  ║
╠═══════════════════════════════════════════════════════════════╣
║  Total dispute cases        : {len(all_cases):<5}  ({NUM_RANDOM_CASES} random + {showcase_n} showcase)
║  Transactions (incl dupls)  : {len(transactions):<5}
║  Customer statements        : {len(statements):<5}
║  Merchant records           : {len(merch_records):<5}
║  Receipts                   : {len(receipts):<5}
║  Delivery records           : {len(deliveries):<5}
║  Authentication events      : {len(auth_events):<5}
║  Correspondence messages    : {len(correspondence):<5}
║  Audit trail entries        : {len(audit_trail):<5}
║  Finale inject cases        : {inject_n:<5}
║  Friendly fraud flagged     : {friendly_n:<5}  (~{round(friendly_n/len(all_cases)*100)}%)
╠═══════════════════════════════════════════════════════════════╣
║  Calibration sources                                          ║
║  • PaySim      — balance tracking, txn types, step           ║
║  • Sparknov    — merchant categories + amount distributions  ║
║  • IEEE-CIS    — 3DS ECI, device/browser, risk score         ║
║  • eCommerce   — device_id, ip, signup/purchase delta        ║
║  • Zenodo      — journal_type, channel_reference             ║
║  • CFPB        — company_response, timely_response           ║
║  • CB911 2026  — log-normal amounts, 43.8% merchant win      ║
║  • Visa/MC     — real chargeback reason codes                ║
╚═══════════════════════════════════════════════════════════════╝

Output  : ./{OUTPUT_DIR}/
Bundles : ./{OUTPUT_DIR}/dispute_cases_bundled.json
""")


if __name__ == "__main__":
    main()
