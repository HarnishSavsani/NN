"""
Card Dispute Evidence Reconstruction & Resolution Agent
Synthetic Data Generator — v3 (Full Scenario Coverage)
========================================================
Extends v2 with 6 new layers closing all 17 gaps and 15 partials
from the 39-scenario register:

  NEW ENTITIES (12):
    jurisdiction, provisional_credit, appeal, arbitration,
    regulatory_hold, archive_status, checkpoints,
    evidence_gaps, fraud_signals, conflict_detections,
    hypotheses, version_conflicts

  NEW FIELDS on existing entities:
    disputes    — sla_breach_at, permanent_credit_posted_at,
                  provisional_reversal_date, denial_reason,
                  sanctions_check_status, ofac_match
    transactions — foreign_currency_amount, fx_rate, dcc_applied,
                   card_bin_country, card_bin_issuer_country
    auth_events  — nfc_cryptogram, device_token, mag_stripe_flag,
                   chip_downgrade_flag, 3ds_flow_type, avs_result

  ADDITIONAL CALIBRATION:
    • ISO 3166 jurisdiction layer (US/GB/DE/FR/AE/SG/AU/IN/SA)
    • OFAC/Sanctions check (SC-36)
    • Islamic Hijri calendar cases (SC-30)
    • Non-Latin merchant names (SC-29, SC-35)
    • NFC cryptogram / device token (SC-37)
    • Mag-stripe downgrade / skimming signals (SC-38)
    • Frictionless vs challenge 3DS flow (SC-39 improvement)
    • 10 showcase cases (5 original + 5 new gap scenarios)

Output: ./synthetic_data_v3/<entity>.json  +  dispute_cases_bundled.json

Run:
    pip install faker numpy openpyxl
    python generate_dispute_data_v3.py
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

OUTPUT_DIR = "synthetic_data_v3"
os.makedirs(OUTPUT_DIR, exist_ok=True)

NOW = datetime.utcnow()
NUM_RANDOM_CASES = 490   # + 10 hand-crafted = 500 total


# ═══════════════════════════════════════════════════════════════════════════════
# REFERENCE TABLES — v2 (unchanged)
# ═══════════════════════════════════════════════════════════════════════════════

MERCHANT_CATEGORIES = {
    "grocery_net":    {"mcc": "5411", "label": "Grocery Stores",               "avg_txn": 68,  "std": 45},
    "gas_transport":  {"mcc": "5541", "label": "Service Stations (Fuel)",      "avg_txn": 52,  "std": 20},
    "entertainment":  {"mcc": "7922", "label": "Theatrical Producers & Tickets","avg_txn": 89,  "std": 60},
    "food_dining":    {"mcc": "5812", "label": "Eating Places & Restaurants",  "avg_txn": 38,  "std": 30},
    "home":           {"mcc": "5722", "label": "Household Appliance Stores",   "avg_txn": 320, "std": 250},
    "kids_pets":      {"mcc": "5945", "label": "Hobby, Toy & Game Shops",      "avg_txn": 55,  "std": 40},
    "personal_care":  {"mcc": "7297", "label": "Health & Beauty Spas",         "avg_txn": 75,  "std": 50},
    "health_fitness": {"mcc": "7941", "label": "Sports Clubs & Athletic",      "avg_txn": 42,  "std": 25},
    "shopping":       {"mcc": "5999", "label": "Miscellaneous Retail",         "avg_txn": 95,  "std": 80},
    "travel":         {"mcc": "7011", "label": "Hotels & Lodging",             "avg_txn": 285, "std": 200},
    "electronics":    {"mcc": "5732", "label": "Electronics Stores",           "avg_txn": 420, "std": 300},
    "telecom":        {"mcc": "4812", "label": "Telecom Equipment & Phones",   "avg_txn": 110, "std": 90},
    "subscription":   {"mcc": "7372", "label": "Prepackaged Software/SaaS",    "avg_txn": 29,  "std": 20},
    "misc_services":  {"mcc": "7299", "label": "Services Not Elsewhere",       "avg_txn": 60,  "std": 45},
}
CATEGORY_KEYS = list(MERCHANT_CATEGORIES.keys())

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

COMPANY_RESPONSES = [
    "Closed with explanation",
    "Closed with monetary relief",
    "Closed with non-monetary relief",
    "Closed without relief",
    "In progress",
]

ECI_VALUES = {
    "fully_authenticated": {"eci": "05", "label": "Full 3DS authentication"},
    "attempted":           {"eci": "06", "label": "Attempted authentication"},
    "non_3ds":             {"eci": "07", "label": "Non-3DS channel"},
    "mastercard_auth":     {"eci": "02", "label": "Mastercard – fully authenticated"},
    "mastercard_attempt":  {"eci": "01", "label": "Mastercard – attempted"},
}

BROWSERS    = ["Chrome", "Firefox", "Safari", "Edge", "Samsung Browser", "Opera", "Unknown"]
OS_TYPES    = ["Windows", "macOS", "iOS", "Android", "Linux"]
DEVICE_CATS = ["Desktop", "Mobile", "Tablet"]
PAYSIM_TYPES= ["CASH_IN", "CASH_OUT", "DEBIT", "PAYMENT", "TRANSFER"]
CHANNELS    = ["Email", "Secure Message", "Phone Transcript", "Chat Log"]

CARRIERS = {
    "FedEx":      {"min_days": 1, "max_days": 5,  "late_prob": 0.08},
    "UPS":        {"min_days": 1, "max_days": 5,  "late_prob": 0.09},
    "DHL":        {"min_days": 2, "max_days": 7,  "late_prob": 0.12},
    "USPS":       {"min_days": 2, "max_days": 10, "late_prob": 0.18},
    "Royal Mail": {"min_days": 2, "max_days": 8,  "late_prob": 0.15},
    "Aramex":     {"min_days": 3, "max_days": 10, "late_prob": 0.20},
}

DISPUTE_REASONS  = list(REASON_CODES.keys())
CARD_NETWORKS    = ["Visa", "Mastercard", "Amex", "Discover"]
CARD_TYPES       = ["Debit", "Credit"]
DISPUTE_STATUSES = [
    "Raised", "Evidence Gathering", "Under Review",
    "Specialist Review", "Resolution Progressed", "Closed – Won", "Closed – Lost",
]


# ═══════════════════════════════════════════════════════════════════════════════
# REFERENCE TABLES — v3 NEW
# ═══════════════════════════════════════════════════════════════════════════════

# Jurisdiction + regulation + calendar layer (SC-26 to SC-31, SC-34)
JURISDICTIONS = {
    "US": {
        "regulation": "REG_E",        "calendar": "gregorian",
        "deadline_days": 120,         "gdpr_applicable": False,
        "local_sla_days": 10,         "currency": "USD",
        "lang": "en",                 "region": "North America",
    },
    "GB": {
        "regulation": "PSD2",         "calendar": "gregorian",
        "deadline_days": 540,         "gdpr_applicable": True,
        "local_sla_days": 15,         "currency": "GBP",
        "lang": "en",                 "region": "Europe",
    },
    "DE": {
        "regulation": "PSD2_BaFin",   "calendar": "gregorian",
        "deadline_days": 540,         "gdpr_applicable": True,
        "local_sla_days": 15,         "currency": "EUR",
        "lang": "de",                 "region": "Europe",
    },
    "FR": {
        "regulation": "PSD2_ACPR",    "calendar": "gregorian",
        "deadline_days": 540,         "gdpr_applicable": True,
        "local_sla_days": 15,         "currency": "EUR",
        "lang": "fr",                 "region": "Europe",
    },
    "AE": {
        "regulation": "CBUAE_2023",   "calendar": "hijri",
        "deadline_days": 45,          "gdpr_applicable": False,
        "local_sla_days": 5,          "currency": "AED",
        "lang": "ar",                 "region": "Middle East",
    },
    "SA": {
        "regulation": "SAMA_2022",    "calendar": "hijri",
        "deadline_days": 30,          "gdpr_applicable": False,
        "local_sla_days": 5,          "currency": "SAR",
        "lang": "ar",                 "region": "Middle East",
    },
    "SG": {
        "regulation": "MAS_PSA",      "calendar": "gregorian",
        "deadline_days": 30,          "gdpr_applicable": False,
        "local_sla_days": 7,          "currency": "SGD",
        "lang": "en",                 "region": "Asia Pacific",
    },
    "AU": {
        "regulation": "RBA_EFT",      "calendar": "gregorian",
        "deadline_days": 90,          "gdpr_applicable": False,
        "local_sla_days": 21,         "currency": "AUD",
        "lang": "en",                 "region": "Asia Pacific",
    },
    "IN": {
        "regulation": "RBI_2019",     "calendar": "gregorian",
        "deadline_days": 90,          "gdpr_applicable": False,
        "local_sla_days": 30,         "currency": "INR",
        "lang": "en",                 "region": "Asia Pacific",
    },
}
JURISDICTION_KEYS = list(JURISDICTIONS.keys())

# FX rates vs USD (approximate mid-market)
FX_RATES = {
    "USD": 1.00, "GBP": 0.79, "EUR": 0.92, "AED": 3.67,
    "SAR": 3.75, "SGD": 1.34, "AUD": 1.53, "INR": 83.1,
    "JPY": 149.5, "CAD": 1.36, "CNY": 7.24, "CHF": 0.90,
}

# Non-Latin merchant names for international cases (SC-29, SC-35)
NON_LATIN_NAMES = {
    "ar": ["شركة التجارة الإلكترونية", "متجر الخليج", "دبي للتسوق", "السوق الإلكتروني", "تجارة أون لاين"],
    "zh": ["电子商务有限公司", "网上购物商城", "数字商城科技", "跨境贸易平台"],
    "ja": ["株式会社デジタル取引", "オンラインショップ株式会社", "電子商取引センター"],
    "ru": ["ООО Цифровая Торговля", "Электронный Маркет", "Онлайн Магазин"],
    "he": ["חברת מסחר אלקטרוני", "חנות מקוונת בע'מ"],
}

# Card BIN issuer country sample (SC-34)
BIN_ISSUER_COUNTRIES = [
    "US", "US", "US", "US", "US",   # majority domestic
    "GB", "DE", "FR", "AE", "SG", "AU", "IN", "CA", "JP", "BR",
]

# Channel authentication types (SC-37, SC-38, SC-39)
CHANNEL_AUTH_TYPES = [
    "CHIP_AND_PIN", "CONTACTLESS_NFC", "MAG_STRIPE",
    "CNP_3DS", "CNP_NON_3DS", "MOBILE_WALLET",
]

# 3DS flow types (SC-39 improvement)
THREE_DS_FLOW_TYPES = ["frictionless", "challenge", "decoupled", "non_3ds"]

# AVS result codes
AVS_RESULTS = {
    "Y": "Address and ZIP match",
    "N": "Address and ZIP do not match",
    "A": "Address matches, ZIP does not",
    "Z": "ZIP matches, address does not",
    "P": "Postal code matches",
    "U": "Unavailable",
    "R": "System unavailable, retry",
    "S": "Service not supported",
}

# Denial reasons (SC-19)
DENIAL_REASONS = [
    "Insufficient evidence of non-receipt",
    "Merchant provided valid proof of delivery",
    "Transaction authenticated via 3DS2 – liability shifted to issuer",
    "Cancellation notice received after billing cycle closed",
    "Item matched product description per third-party inspection",
    "Refund posted to account prior to dispute submission",
    "Dispute filed outside chargeback window",
    "Duplicate – identical dispute already resolved",
]

# Sanctions screening outcomes (SC-36)
SANCTIONS_STATUSES = ["CLEAR", "CLEAR", "CLEAR", "CLEAR", "CLEAR",
                       "CLEAR", "CLEAR", "PENDING_REVIEW", "FLAGGED"]
OFAC_LISTS = ["SDN", "CONS", "FSE", "NS-PLC"]


# ═══════════════════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

def uid():
    return str(uuid.uuid4())

def save(name, data):
    path = os.path.join(OUTPUT_DIR, f"{name}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  ✓  {path}  ({len(data)} records)")

def iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")

def jitter(base, min_s, max_s):
    return base + timedelta(seconds=random.randint(min_s, max_s))

def lognormal_amount(mean_usd, std_usd, lo=1.0, hi=5000.0):
    if HAS_NUMPY:
        sigma = math.sqrt(math.log(1 + (std_usd / mean_usd) ** 2))
        mu    = math.log(mean_usd) - sigma ** 2 / 2
        val   = np.random.lognormal(mu, sigma)
    else:
        val = random.gauss(mean_usd, std_usd)
    return round(max(lo, min(hi, val)), 2)

def txn_time(base_date):
    hour_weights = [
        1, 1, 0.5, 0.5, 0.5, 0.5,
        2, 4, 6,   7,   8,   8,
        9, 9, 8,   8,   9,   10,
        10,9, 7,   6,   4,   2,
    ]
    hour   = random.choices(range(24), weights=hour_weights)[0]
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return base_date.replace(hour=hour, minute=minute, second=second)

def hijri_date_str(dt):
    """Approximate Gregorian → Hijri string (offset only, not exact)."""
    hijri_year  = int((dt.year - 622) * (33/32))
    hijri_month = dt.month
    hijri_day   = dt.day
    return f"{hijri_year}-{hijri_month:02d}-{hijri_day:02d} AH"

def non_latin_name(lang):
    opts = NON_LATIN_NAMES.get(lang, [])
    return random.choice(opts) if opts else None


# ═══════════════════════════════════════════════════════════════════════════════
# 0. JURISDICTION  (new in v3)
# ═══════════════════════════════════════════════════════════════════════════════

def gen_jurisdiction(case):
    jcode = random.choices(
        JURISDICTION_KEYS,
        weights=[50, 8, 6, 6, 6, 4, 6, 6, 8]   # US-heavy but varied
    )[0]
    jdata = JURISDICTIONS[jcode]
    raised = datetime.fromisoformat(case["raised_at"].replace("Z", ""))

    local_deadline = raised + timedelta(days=jdata["deadline_days"])
    sla_deadline   = raised + timedelta(days=jdata["local_sla_days"])
    sla_breached   = sla_deadline < NOW and random.random() < 0.12

    cal_type   = jdata["calendar"]
    date_ref   = hijri_date_str(raised) if cal_type == "hijri" else raised.strftime("%Y-%m-%d")

    # Sanctions check (SC-36)
    sanctions_status = random.choice(SANCTIONS_STATUSES)
    ofac_match = sanctions_status == "FLAGGED"
    ofac_list  = random.choice(OFAC_LISTS) if ofac_match else None

    return {
        "jurisdiction_id":      uid(),
        "case_id":              case["case_id"],
        "issuer_country":       jcode,
        "acquirer_country":     random.choice(JURISDICTION_KEYS),
        "jurisdiction":         jcode,
        "regulation_applied":   jdata["regulation"],
        "region":               jdata["region"],
        "calendar_type":        cal_type,
        "local_date_reference": date_ref,
        "gdpr_applicable":      jdata["gdpr_applicable"],
        "deadline_days":        jdata["deadline_days"],
        "local_deadline":       iso(local_deadline),
        "local_sla_days":       jdata["local_sla_days"],
        "sla_deadline":         iso(sla_deadline),
        "sla_breached":         sla_breached,
        "sla_breach_at":        iso(sla_deadline + timedelta(hours=1)) if sla_breached else None,
        "regulatory_reporting_required": jdata["gdpr_applicable"] or jcode in ("AE", "SA"),
        "sanctions_check_status":  sanctions_status,
        "ofac_match":              ofac_match,
        "ofac_list_matched":       ofac_list,
        "lang":                    jdata["lang"],
        "non_latin_merchant_name": non_latin_name(jdata["lang"]) if jdata["lang"] != "en" else None,
    }


def gen_jurisdictions(cases):
    return [gen_jurisdiction(c) for c in cases]


# ═══════════════════════════════════════════════════════════════════════════════
# 1. DISPUTES  (v2 + new operational fields)
# ═══════════════════════════════════════════════════════════════════════════════

def gen_dispute(idx, raised_at=None, reason=None, finale_inject=None,
                override_fields=None):
    if raised_at is None:
        raised_at = fake.date_time_between(start_date="-120d", end_date="-5d")
    if reason is None:
        reason = random.choice(DISPUTE_REASONS)

    cat_key  = random.choice(CATEGORY_KEYS)
    cat      = MERCHANT_CATEGORIES[cat_key]
    network  = random.choice(CARD_NETWORKS)
    amt      = lognormal_amount(cat["avg_txn"], cat["std"])
    if random.random() < 0.25:
        amt  = lognormal_amount(84, 60)

    rc_options = REASON_CODES.get(reason, [])
    rc = next((r for r in rc_options if r["network"] == network), rc_options[0]) \
         if rc_options else {"code": "N/A", "label": reason, "network": network}

    deadline = raised_at + timedelta(days=random.choice([30, 45, 60, 90, 120]))
    is_friendly = (reason in ["Item not received", "Item significantly not as described",
                               "Credit not processed"]) and random.random() < 0.60
    status_idx = random.randint(0, len(DISPUTE_STATUSES) - 1)
    status     = DISPUTE_STATUSES[status_idx]

    is_closed_won  = status == "Closed – Won"
    is_closed_lost = status == "Closed – Lost"
    is_closed      = is_closed_won or is_closed_lost

    # v3: operational resolution fields
    perm_credit_at   = None
    prov_reversal_at = None
    denial_reason    = None
    appeal_window    = raised_at + timedelta(days=random.randint(45, 90))

    if is_closed_won:
        perm_credit_at = raised_at + timedelta(days=random.randint(15, 60))
    if is_closed_lost:
        denial_reason    = random.choice(DENIAL_REASONS)
        prov_reversal_at = raised_at + timedelta(days=random.randint(10, 30))

    # SLA breach tracking
    sla_target  = raised_at + timedelta(days=10)
    sla_breached = sla_target < NOW and random.random() < 0.10
    sla_breach_at = iso(sla_target + timedelta(hours=2)) if sla_breached else None

    record = {
        "case_id":               uid(),
        "case_number":           f"DSP-{2025000 + idx:07d}",
        "raised_at":             iso(raised_at),
        "deadline":              iso(deadline),
        "appeal_window_expires": iso(appeal_window),
        "status":                status,
        "dispute_reason":        reason,
        "reason_code":           rc["code"],
        "reason_code_label":     rc["label"],
        "reason_code_network":   rc["network"],
        "claim_amount":          amt,
        "currency":              random.choice(["USD","USD","USD","GBP","EUR","CAD"]),
        "card_network":          network,
        "card_type":             random.choice(CARD_TYPES),
        "merchant_category_key": cat_key,
        "mcc_code":              cat["mcc"],
        "mcc_description":       cat["label"],
        "customer_id":           uid(),
        "merchant_id":           uid(),
        "friendly_fraud":        is_friendly,
        "fraud_type":            ("Friendly Fraud" if is_friendly else
                                  ("True Fraud" if reason == "Unauthorised transaction"
                                   else "Merchant Error")),
        "company_response":      random.choice(COMPANY_RESPONSES),
        "timely_response":       random.random() > 0.02,
        "consumer_disputed":     random.random() < 0.20,
        "merchant_contested":    random.random() < 0.60,
        "merchant_win":          None,
        "finale_inject":         finale_inject if finale_inject is not None
                                 else (random.random() < 0.10),
        # v3 operational fields
        "sla_breached":              sla_breached,
        "sla_breach_at":             sla_breach_at,
        "permanent_credit_posted_at":iso(perm_credit_at) if perm_credit_at else None,
        "provisional_reversal_date": iso(prov_reversal_at) if prov_reversal_at else None,
        "denial_reason":             denial_reason,
        "stp_eligible":              False,  # set by hypothesis generator
        "created_at":                iso(raised_at),
        "updated_at":                iso(NOW),
    }

    if override_fields:
        record.update(override_fields)

    if record["status"].startswith("Closed") and record["merchant_contested"]:
        record["merchant_win"] = random.random() < 0.438

    return record


def gen_disputes(n):
    return [gen_dispute(i) for i in range(n)]


# ═══════════════════════════════════════════════════════════════════════════════
# 2. TRANSACTIONS  (v2 + FX/DCC + card_bin_country)
# ═══════════════════════════════════════════════════════════════════════════════

def gen_transaction(case):
    raised   = datetime.fromisoformat(case["raised_at"].replace("Z", ""))
    txn_days_back = random.choices(
        range(1, 46),
        weights=[10,9,8,8,7,7,6,6,5,5, 4,4,4,3,3,3,3,3,2,2,
                 2,2,2,2,2,2,2,2,2,2, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1],
    )[0]
    txn_at   = txn_time(raised - timedelta(days=txn_days_back))

    if case["dispute_reason"] == "Unauthorised transaction":
        txn_type = random.choice(["CASH_OUT", "TRANSFER"])
    elif case["dispute_reason"] == "Cancelled recurring transaction":
        txn_type = "DEBIT"
    else:
        txn_type = random.choices(PAYSIM_TYPES, weights=[5,20,15,50,10])[0]

    old_balance = round(random.uniform(100, 8000), 2)
    new_balance = round(max(0, old_balance - case["claim_amount"]), 2)
    dest_old    = round(random.uniform(0, 5000), 2)
    dest_new    = round(dest_old + case["claim_amount"], 2)
    authorised  = case["dispute_reason"] != "Unauthorised transaction" or random.random() > 0.3
    settled     = authorised and random.random() > 0.04
    step        = txn_days_back * 24 + txn_at.hour

    eci_key = random.choices(list(ECI_VALUES.keys()), weights=[40,30,20,5,5])[0]
    eci     = ECI_VALUES[eci_key]

    is_fraud   = case["dispute_reason"] == "Unauthorised transaction"
    is_flagged = is_fraud and case["claim_amount"] > 200000
    is_dup     = case["dispute_reason"] == "Duplicate charge"

    # v3: FX / DCC fields (SC-32, SC-33)
    txn_currency = case["currency"]
    foreign_ccy  = None
    fx_rate      = None
    foreign_amt  = None
    dcc_applied  = False
    dcc_markup   = None
    dcc_provider = None

    # ~20% of transactions are cross-currency
    if random.random() < 0.20:
        foreign_ccy  = random.choice(["GBP", "EUR", "AED", "SGD", "AUD", "JPY"])
        if foreign_ccy != txn_currency:
            fx_rate     = round(FX_RATES.get(foreign_ccy, 1.0), 4)
            foreign_amt = round(case["claim_amount"] * fx_rate, 2)
            # DCC offered ~40% of cross-border txns
            if random.random() < 0.40:
                dcc_applied  = True
                dcc_markup   = round(random.uniform(0.02, 0.06), 4)   # 2–6% markup
                dcc_provider = random.choice(["Planet Payment", "Fexco", "Euronet", "First Data DCC"])

    # v3: card BIN issuer country (SC-34)
    card_bin_country = random.choice(BIN_ISSUER_COUNTRIES)
    card_bin         = f"{random.randint(400000,499999)}" if case["card_network"] == "Visa" \
                       else f"{random.randint(510000,559999)}"

    # v3: 3DS flow type (SC-39 improvement)
    three_ds_flow = None
    if eci["eci"] in ("05", "06", "02", "01"):
        three_ds_flow = random.choice(["frictionless", "challenge", "decoupled"])
    elif eci["eci"] == "07":
        three_ds_flow = "non_3ds"

    merchant_name = fake.company()
    channel = random.choice(["Online", "In-Store", "MOTO", "Contactless", "Mobile App"])

    record = {
        "transaction_id":           uid(),
        "case_id":                  case["case_id"],
        # PaySim
        "step":                     step,
        "type":                     txn_type,
        "amount":                   case["claim_amount"],
        "name_orig":                f"C{case['customer_id'][:8].replace('-','')}",
        "old_balance_orig":         old_balance,
        "new_balance_orig":         new_balance,
        "name_dest":                f"M{case['merchant_id'][:8].replace('-','')}",
        "old_balance_dest":         dest_old,
        "new_balance_dest":         dest_new,
        "is_fraud":                 is_fraud,
        "is_flagged_fraud":         is_flagged,
        # Standard
        "txn_reference":            f"TXN{random.randint(10**11,10**12-1)}",
        "timestamp":                iso(txn_at),
        "currency":                 txn_currency,
        "merchant_id":              case["merchant_id"],
        "merchant_name":            merchant_name,
        "merchant_category":        case["mcc_description"],
        "mcc_code":                 case["mcc_code"],
        "merchant_city":            fake.city(),
        "merchant_state":           fake.state_abbr(),
        "merchant_country":         fake.country_code(),
        "merchant_zip":             fake.zipcode(),
        "card_network":             case["card_network"],
        "card_last4":               str(random.randint(1000,9999)),
        "card_type":                case["card_type"],
        "card_bin":                 card_bin,
        "card_bin_issuer_country":  card_bin_country,
        "channel":                  channel,
        # Auth
        "authorisation_code":       f"AUTH{random.randint(100000,999999)}" if authorised else None,
        "authorised":               authorised,
        "settled":                  settled,
        "settlement_date":          iso(txn_at + timedelta(days=random.randint(1,3))) if settled else None,
        "eci_indicator":            eci["eci"],
        "eci_label":                eci["label"],
        "cavv":                     uuid.uuid4().hex[:20].upper() if eci["eci"] in ("05","02") else None,
        "three_ds_version":         "2.2" if eci["eci"] in ("05","06","02","01") else None,
        "three_ds_flow_type":       three_ds_flow,
        # Zenodo
        "reference_number":         f"REF{random.randint(10**9,10**10-1)}",
        "capture_number":           f"CAP{random.randint(10**8,10**9-1)}",
        "receipt_number":           f"RCT-{random.randint(1000000,9999999)}",
        "journal_type":             random.choice(["DR","CR"]),
        "channel_reference_number": f"CHR{random.randint(10**9,10**10-1)}",
        "is_verified":              authorised,
        "paying_at":                iso(txn_at),
        # v3 FX/DCC
        "foreign_currency":         foreign_ccy,
        "foreign_currency_amount":  foreign_amt,
        "fx_rate_at_transaction":   fx_rate,
        "dcc_applied":              dcc_applied,
        "dcc_markup_rate":          dcc_markup,
        "dcc_provider":             dcc_provider,
        "is_duplicate":             is_dup,
        "reversal":                 False,
        "reversal_reference":       None,
        "provenance":               "CORE_BANKING",
        "version":                  1,
    }

    results = [record]
    if is_dup:
        dup = dict(record)
        dup["transaction_id"]     = uid()
        dup["txn_reference"]      = f"TXN{random.randint(10**11,10**12-1)}"
        dup["timestamp"]          = iso(txn_at + timedelta(minutes=random.randint(1,45)))
        dup["authorisation_code"] = f"AUTH{random.randint(100000,999999)}"
        dup["reference_number"]   = f"REF{random.randint(10**9,10**10-1)}"
        dup["capture_number"]     = f"CAP{random.randint(10**8,10**9-1)}"
        results.append(dup)

    return results


def gen_transactions(cases):
    all_txns = []
    for c in cases:
        all_txns.extend(gen_transaction(c))
    return all_txns


# ═══════════════════════════════════════════════════════════════════════════════
# 3. CUSTOMER STATEMENTS  (unchanged from v2)
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

DISCREPANCIES   = [
    "the colour was entirely different from the listing photos",
    "the dimensions were 40% smaller than advertised",
    "the material was synthetic rather than the advertised genuine leather",
    "the item was a counterfeit with visible quality defects",
    "the product was a different model number with fewer features",
]
CANCEL_METHODS  = ["phone call","email","online portal","in-app cancellation","written letter"]

def gen_customer_statement(case, txn):
    raised      = datetime.fromisoformat(case["raised_at"].replace("Z",""))
    order_dt    = raised - timedelta(days=random.randint(7,40))
    delivery_dt = order_dt + timedelta(days=random.randint(3,15))
    contact_dt  = raised - timedelta(days=random.randint(1,7))
    contact_dt2 = contact_dt + timedelta(days=3)
    txn_dt      = datetime.fromisoformat(txn["timestamp"].replace("Z","")) if txn else raised - timedelta(days=5)
    days_since  = (raised - delivery_dt).days

    narrative = STMT_TEMPLATES.get(case["dispute_reason"],
                                   STMT_TEMPLATES["Item not received"]).format(
        order_date    = order_dt.strftime("%d %b %Y"),
        delivery_date = delivery_dt.strftime("%d %b %Y"),
        txn_date      = txn_dt.strftime("%d %b %Y"),
        txn_date2     = (txn_dt + timedelta(minutes=30)).strftime("%d %b %Y"),
        contact_date  = contact_dt.strftime("%d %b %Y"),
        contact_date2 = contact_dt2.strftime("%d %b %Y"),
        cancel_date   = (raised - timedelta(days=random.randint(5,60))).strftime("%d %b %Y"),
        cancel_date2  = (raised - timedelta(days=3)).strftime("%d %b %Y"),
        cancel_method = random.choice(CANCEL_METHODS),
        cancel_ref    = f"CXL-{random.randint(100000,999999)}",
        item          = fake.catch_phrase(),
        merchant      = fake.company(),
        amount        = case["claim_amount"],
        currency      = case["currency"],
        channel       = random.choice(["website","mobile app","telephone order"]),
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
        "channel":         random.choice(["Online Portal","Phone","Branch","Mobile App"]),
        "dispute_reason":  case["dispute_reason"],
        "narrative":       narrative,
        "claimed_amount":  case["claim_amount"],
        "currency":        case["currency"],
        "attachments":     random.sample(
            ["screenshot.png","order_confirmation.pdf","email_thread.eml",
             "bank_statement.pdf","photo_of_item.jpg","return_receipt.pdf"],
            k=random.randint(0,3)),
        "consumer_consent_provided": True,
        "submitted_via":   random.choice(["Web","Phone","Referral","Postal mail"]),
        "provenance":      "CUSTOMER_PORTAL",
        "version":         1,
        "superseded_by":   None,
    }

def gen_customer_statements(cases, transactions):
    txn_map = {}
    for t in transactions:
        txn_map.setdefault(t["case_id"], t)
    return [gen_customer_statement(c, txn_map.get(c["case_id"])) for c in cases]


# ═══════════════════════════════════════════════════════════════════════════════
# 4. MERCHANT RECORDS  (unchanged from v2)
# ═══════════════════════════════════════════════════════════════════════════════

def gen_merchant_record(case):
    raised   = datetime.fromisoformat(case["raised_at"].replace("Z",""))
    order_dt = raised - timedelta(days=random.randint(7,40))
    fulfilled = case["dispute_reason"] not in ["Item not received","Service not provided"]
    refund_issued = case["dispute_reason"] == "Credit not processed" and random.random() > 0.4

    items = [{"sku": f"SKU-{random.randint(1000,9999)}", "description": fake.catch_phrase(),
               "qty": random.randint(1,3), "unit_price": round(case["claim_amount"]/random.randint(1,3),2),
               "category": case["mcc_description"]}]

    return {
        "merchant_record_id":   uid(),
        "case_id":              case["case_id"],
        "merchant_id":          case["merchant_id"],
        "merchant_name":        fake.company(),
        "merchant_category":    case["mcc_description"],
        "mcc_code":             case["mcc_code"],
        "order_id":             f"ORD-{random.randint(100000,999999)}",
        "order_date":           iso(order_dt),
        "order_status":         random.choice(["Delivered","Dispatched","Processing",
                                               "Cancelled","Refunded","Returned"]),
        "items":                items,
        "subtotal":             case["claim_amount"],
        "tax_rate":             0.08,
        "tax_amount":           round(case["claim_amount"] * 0.08, 2),
        "total_charged":        round(case["claim_amount"] * 1.08, 2),
        "currency":             case["currency"],
        "fulfilled":            fulfilled,
        "fulfilment_date":      iso(order_dt + timedelta(days=random.randint(1,3))) if fulfilled else None,
        "refund_issued":        refund_issued,
        "refund_amount":        case["claim_amount"] if refund_issued else None,
        "refund_reference":     f"REF-{random.randint(100000,999999)}" if refund_issued else None,
        "refund_date":          iso(raised - timedelta(days=random.randint(1,5))) if refund_issued else None,
        "merchant_response":    random.choice([
            "Order delivered as per tracking records.",
            "Item dispatched; tracking number provided to customer.",
            "Refund already processed per RMA.",
            "Subscription cancelled post billing cycle; charge was valid.",
            "Customer signed for delivery.",
            "Goods matched product description at time of listing.",
        ]),
        "merchant_contested":   case["merchant_contested"],
        "received_at":          case["raised_at"],
        "provenance":           "MERCHANT_PORTAL",
        "version":              1,
        "superseded_by":        None,
    }

def gen_merchant_records(cases):
    return [gen_merchant_record(c) for c in cases]


# ═══════════════════════════════════════════════════════════════════════════════
# 5. RECEIPTS  (unchanged from v2)
# ═══════════════════════════════════════════════════════════════════════════════

def gen_receipts(cases, merchant_records):
    mr_map = {r["case_id"]: r for r in merchant_records}
    receipts = []
    for c in cases:
        mr     = mr_map.get(c["case_id"])
        raised = datetime.fromisoformat(c["raised_at"].replace("Z",""))
        issued = raised - timedelta(days=random.randint(8,40))
        receipts.append({
            "receipt_id":     uid(),
            "case_id":        c["case_id"],
            "order_id":       mr["order_id"] if mr else f"ORD-{random.randint(100000,999999)}",
            "merchant_id":    c["merchant_id"],
            "issued_at":      iso(issued),
            "receipt_number": f"RCT-{random.randint(1000000,9999999)}",
            "line_items":     mr["items"] if mr else [],
            "subtotal":       c["claim_amount"],
            "tax_rate":       0.08,
            "tax_amount":     round(c["claim_amount"] * 0.08, 2),
            "total":          round(c["claim_amount"] * 1.08, 2),
            "currency":       c["currency"],
            "payment_method": f"{c['card_type']} {c['card_network']} ****{random.randint(1000,9999)}",
            "format":         random.choice(["PDF","HTML","Image"]),
            "hash_sha256":    uuid.uuid4().hex + uuid.uuid4().hex[:32],
            "provenance":     "MERCHANT_RECEIPT_SYSTEM",
            "version":        1,
        })
    return receipts


# ═══════════════════════════════════════════════════════════════════════════════
# 6. DELIVERY RECORDS  (unchanged from v2)
# ═══════════════════════════════════════════════════════════════════════════════

def gen_delivery_record(case, merchant_record):
    raised       = datetime.fromisoformat(case["raised_at"].replace("Z",""))
    carrier_name = random.choice(list(CARRIERS.keys()))
    carrier      = CARRIERS[carrier_name]
    order_dt     = raised - timedelta(days=random.randint(10,40))
    shipped_at   = order_dt + timedelta(hours=random.randint(4,48))
    transit_days = random.randint(carrier["min_days"], carrier["max_days"])
    expected     = shipped_at + timedelta(days=transit_days)
    late         = random.random() < carrier["late_prob"]
    delay_days   = random.randint(1,7) if late else 0
    actual       = expected + timedelta(days=delay_days)

    if case["dispute_reason"] == "Item not received":
        dlv_status = random.choice(["Failed Delivery","Lost","In Transit","Returned to Sender"])
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
        {"event": "Order Received",  "timestamp": iso(order_dt),                       "location": fake.city()},
        {"event": "Picked & Packed", "timestamp": iso(order_dt + timedelta(hours=6)), "location": fake.city()},
        {"event": "Dispatched",      "timestamp": iso(shipped_at),                     "location": fake.city()},
        {"event": "In Transit",      "timestamp": iso(shipped_at + timedelta(days=1)),"location": fake.city()},
    ]
    if delivered:
        events.append({"event": "Out for Delivery", "timestamp": iso(actual - timedelta(hours=3)), "location": fake.city()})
        events.append({"event": "Delivered",         "timestamp": iso(actual),                      "location": fake.city()})
    elif dlv_status == "Failed Delivery":
        events.append({"event": "Failed Delivery Attempt",    "timestamp": iso(actual),                        "location": fake.city()})
        events.append({"event": "Return to Sender Initiated", "timestamp": iso(actual + timedelta(days=2)),    "location": fake.city()})
    elif dlv_status == "Lost":
        events.append({"event": "Last Scan", "timestamp": iso(shipped_at + timedelta(days=2)), "location": fake.city()})

    return {
        "delivery_id":           uid(),
        "case_id":               case["case_id"],
        "order_id":              merchant_record["order_id"] if merchant_record else f"ORD-{random.randint(100000,999999)}",
        "carrier":               carrier_name,
        "tracking_number":       f"{random.choice(['1Z','JD','GM','LX'])}{random.randint(10**14,10**15-1)}",
        "service_level":         random.choice(["Standard","Express","Priority","Economy"]),
        "shipped_at":            iso(shipped_at),
        "expected_by":           iso(expected),
        "actual_delivery_at":    iso(actual) if delivered else None,
        "arrived_late":          late,
        "delay_days":            delay_days,
        "status":                dlv_status,
        "delivered":             delivered,
        "delivery_address":      fake.address().replace("\n",", "),
        "delivery_city":         fake.city(),
        "delivery_state":        fake.state_abbr(),
        "delivery_zip":          fake.zipcode(),
        "delivery_country":      fake.country_code(),
        "signature_obtained":    signature,
        "proof_of_delivery_url": pod_photo,
        "events":                events,
        "weight_kg":             round(random.uniform(0.1,20),2),
        "dimensions_cm":         f"{random.randint(5,60)}x{random.randint(5,40)}x{random.randint(2,30)}",
        "provenance":            "CARRIER_API",
        "version":               1,
    }

def gen_delivery_records(cases, merchant_records):
    mr_map = {r["case_id"]: r for r in merchant_records}
    return [gen_delivery_record(c, mr_map.get(c["case_id"])) for c in cases]


# ═══════════════════════════════════════════════════════════════════════════════
# 7. AUTHENTICATION EVENTS  (v2 + NFC, mag-stripe, 3DS flow, AVS)
# ═══════════════════════════════════════════════════════════════════════════════

def gen_auth_event(case, txn):
    txn_ts = datetime.fromisoformat(txn["timestamp"].replace("Z","")) if txn \
             else datetime.fromisoformat(case["raised_at"].replace("Z","")) - timedelta(days=3)

    geo_mismatch = (case["dispute_reason"] == "Unauthorised transaction") and (random.random() > 0.45)
    customer_state = fake.state_abbr()
    txn_state      = fake.state_abbr() if geo_mismatch else customer_state

    device_cat = random.choice(DEVICE_CATS)
    browser    = random.choice(BROWSERS)
    os_type    = random.choice(OS_TYPES)
    device_id  = uuid.uuid4().hex[:16]
    ip         = fake.ipv4_public()
    ip_country_mismatch = geo_mismatch and random.random() > 0.5

    # v3: determine channel auth type
    channel = txn.get("channel", "Online") if txn else "Online"
    if channel == "Contactless":
        auth_channel = "CONTACTLESS_NFC"
    elif channel == "In-Store":
        auth_channel = random.choice(["CHIP_AND_PIN", "MAG_STRIPE", "CONTACTLESS_NFC"])
    elif channel in ("Online", "Mobile App", "MOTO"):
        auth_channel = "CNP_3DS" if txn and txn.get("eci_indicator") in ("05","06") else "CNP_NON_3DS"
    else:
        auth_channel = random.choice(CHANNEL_AUTH_TYPES)

    # v3: NFC / contactless fields (SC-37)
    nfc_cryptogram  = uuid.uuid4().hex[:32].upper() if auth_channel == "CONTACTLESS_NFC" else None
    device_token    = uuid.uuid4().hex[:24].upper() if auth_channel in ("CONTACTLESS_NFC","MOBILE_WALLET") else None

    # v3: mag-stripe / skimming fields (SC-38)
    mag_stripe_flag       = auth_channel == "MAG_STRIPE"
    chip_downgrade_flag   = mag_stripe_flag and random.random() < 0.35   # chip card forced to swipe
    track_data_present    = mag_stripe_flag
    skimming_signal       = chip_downgrade_flag and case["dispute_reason"] == "Unauthorised transaction"

    # v3: 3DS flow type
    three_ds_flow = txn.get("three_ds_flow_type") if txn else None

    # v3: AVS result
    avs_code   = random.choice(list(AVS_RESULTS.keys()))
    avs_result = AVS_RESULTS[avs_code]
    avs_mismatch = avs_code in ("N","A","Z")

    # v3: CVV2
    cvv2_result = random.choice(["M", "N", "P", "S", "U"])   # M=match, N=no match

    auth_method = txn.get("eci_label","Non-3DS channel") if txn else "PIN"
    success     = case["dispute_reason"] != "Unauthorised transaction" or random.random() > 0.55
    base_risk   = 0.7 if case["dispute_reason"] == "Unauthorised transaction" else 0.15
    if chip_downgrade_flag:
        base_risk = min(1.0, base_risk + 0.20)
    risk_score   = round(min(1.0, max(0.0, random.gauss(base_risk, 0.15))), 4)
    risk_decision= "DECLINE" if risk_score > 0.85 else ("REFER" if risk_score > 0.65 else "APPROVE")

    return {
        "auth_event_id":        uid(),
        "case_id":              case["case_id"],
        "transaction_id":       txn["transaction_id"] if txn else None,
        "event_type":           random.choice(["AUTHORISATION","3DS_CHALLENGE",
                                               "PIN_VERIFY","BIOMETRIC_VERIFY","OTP_VERIFY"]),
        "timestamp":            iso(txn_ts),
        "channel_auth_type":    auth_channel,
        # 3DS
        "eci_indicator":        txn.get("eci_indicator") if txn else "07",
        "eci_label":            txn.get("eci_label") if txn else "Non-3DS channel",
        "three_ds_version":     txn.get("three_ds_version") if txn else None,
        "three_ds_flow_type":   three_ds_flow,
        "cavv":                 txn.get("cavv") if txn else None,
        "authentication_result":auth_method,
        "success":              success,
        "failure_reason":       None if success else random.choice(
            ["Wrong PIN","3DS timeout","Biometric mismatch","OTP expired","Card blocked"]),
        # Device
        "device_type":          device_cat,
        "device_id":            device_id,
        "browser":              browser,
        "os":                   os_type,
        "user_agent":           f"Mozilla/5.0 ({os_type}) {browser}/120.0",
        "screen_resolution":    random.choice(["1920x1080","1366x768","375x812","390x844","2560x1440"]),
        # v3 NFC / contactless (SC-37)
        "nfc_cryptogram":       nfc_cryptogram,
        "device_token":         device_token,
        # v3 mag-stripe / skimming (SC-38)
        "mag_stripe_flag":      mag_stripe_flag,
        "chip_downgrade_flag":  chip_downgrade_flag,
        "track_data_present":   track_data_present,
        "skimming_signal":      skimming_signal,
        # v3 AVS / CVV2
        "avs_result_code":      avs_code,
        "avs_result_desc":      avs_result,
        "avs_mismatch":         avs_mismatch,
        "cvv2_result":          cvv2_result,
        # Geo
        "ip_address":           ip,
        "ip_country":           "US" if not ip_country_mismatch else fake.country_code(),
        "ip_country_mismatch":  ip_country_mismatch,
        "customer_state":       customer_state,
        "transaction_state":    txn_state,
        "geo_mismatch":         geo_mismatch,
        "customer_id":          case["customer_id"],
        "customer_email_domain":random.choice(["gmail.com","yahoo.com","outlook.com",
                                               "hotmail.com","icloud.com","proton.me"]),
        # Risk
        "risk_score":           risk_score,
        "risk_decision":        risk_decision,
        "velocity_last_1h":     random.randint(0,5),
        "velocity_last_24h":    random.randint(0,20),
        "provenance":           "AUTH_ENGINE",
        "version":              1,
    }

def gen_auth_events(cases, transactions):
    txn_map = {t["case_id"]: t for t in transactions if not t.get("is_duplicate")}
    return [gen_auth_event(c, txn_map.get(c["case_id"])) for c in cases]


# ═══════════════════════════════════════════════════════════════════════════════
# 8. CORRESPONDENCE  (unchanged from v2)
# ═══════════════════════════════════════════════════════════════════════════════

CORR_TEMPLATES = [
    {"direction": "BANK_TO_CUSTOMER", "subject": "Dispute {case_number} received – next steps",
     "body": "Dear {name},\n\nThank you for contacting us. We have registered dispute {case_number} "
             "for {currency} {amount} with {merchant}.\n\nWe will investigate and aim to provide an update "
             "within 5 business days. Provisional credit may be applied per Regulation E guidelines.\n\n"
             "Ref: {case_number}\nDisputes Team"},
    {"direction": "BANK_TO_MERCHANT", "subject": "Retrieval Request – {case_number} (Reason {reason_code})",
     "body": "Dear Merchant,\n\nWe are investigating dispute {case_number} under reason code {reason_code} "
             "({reason_label}).\n\nPlease provide within 10 calendar days: order confirmation, "
             "proof of delivery, signed receipts.\n\nFailure to respond may result in automatic "
             "chargeback.\n\nDisputes Operations"},
    {"direction": "MERCHANT_TO_BANK", "subject": "RE: Retrieval Request – {case_number}",
     "body": "Please find attached our response to dispute {case_number}.\n\n"
             "Order {order_id} was fulfilled on {fulfil_date}. Delivery was confirmed by carrier "
             "with tracking reference {tracking}. We request representment.\n\nMerchant Risk Team"},
    {"direction": "CUSTOMER_TO_BANK", "subject": "Additional information – dispute {case_number}",
     "body": "Hello,\n\nFurther to my dispute {case_number} I am providing attached evidence.\n\n"
             "The tracking page still shows '{delivery_status}' and I have heard nothing from the merchant.\n\n"
             "Regards,\n{name}"},
    {"direction": "BANK_TO_CUSTOMER", "subject": "Update on dispute {case_number}",
     "body": "Dear {name},\n\nWe have received the merchant's response to dispute {case_number}. "
             "Our team is reviewing the evidence. We will update you within 3 business days.\n\nDisputes Team"},
]

def gen_correspondence(cases, merchant_records):
    mr_map = {r["case_id"]: r for r in merchant_records}
    corrs  = []
    for c in cases:
        mr    = mr_map.get(c["case_id"])
        raised = datetime.fromisoformat(c["raised_at"].replace("Z",""))
        name   = fake.name()
        num    = random.randint(2,5)
        selected = random.sample(CORR_TEMPLATES, min(num, len(CORR_TEMPLATES)))
        for idx, tmpl in enumerate(selected):
            sent = raised + timedelta(days=idx * random.randint(1,4), hours=random.randint(0,8))
            body = tmpl["body"].format(
                case_number     = c["case_number"],
                name            = name,
                currency        = c["currency"],
                amount          = c["claim_amount"],
                merchant        = mr["merchant_name"] if mr else fake.company(),
                reason_code     = c["reason_code"],
                reason_label    = c["reason_code_label"],
                order_id        = mr["order_id"] if mr else "N/A",
                fulfil_date     = (raised - timedelta(days=5)).strftime("%d %b %Y"),
                tracking        = f"1Z{random.randint(10**14,10**15-1)}",
                delivery_status = random.choice(["In Transit","No information available","Failed Delivery Attempt"]),
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
                "subject":           tmpl["subject"].format(case_number=c["case_number"], reason_code=c["reason_code"]),
                "body":              body,
                "attachments":       random.sample(
                    ["order_confirmation.pdf","pod.jpg","tracking_screenshot.png",
                     "invoice.pdf","merchant_response.pdf","customer_photo.jpg"], k=random.randint(0,2)),
                "read_at":           iso(sent + timedelta(hours=random.randint(1,48))),
                "provenance":        "CORRESPONDENCE_SYSTEM",
                "version":           1,
                "superseded_by":     None,
            })
    return corrs


# ═══════════════════════════════════════════════════════════════════════════════
# 9. AUDIT TRAIL  (unchanged from v2)
# ═══════════════════════════════════════════════════════════════════════════════

AUDIT_ACTIONS = [
    ("Dispute raised by customer",          "HUMAN_ANALYST"),
    ("Transaction event retrieved",         "AI_AGENT"),
    ("Customer statement recorded",         "SYSTEM"),
    ("Merchant retrieval request sent",     "SYSTEM"),
    ("Authentication event retrieved",      "AI_AGENT"),
    ("Delivery record retrieved",           "AI_AGENT"),
    ("Evidence gap identified",             "AI_AGENT"),
    ("Contradiction detected",              "AI_AGENT"),
    ("Next-best-evidence selected",         "AI_AGENT"),
    ("Specialist review assigned",          "SYSTEM"),
    ("Human decision recorded",             "HUMAN_MANAGER"),
    ("Merchant response received",          "SYSTEM"),
    ("Evidence reconciled",                 "AI_AGENT"),
    ("Outcome recommendation prepared",     "AI_AGENT"),
    ("Case status updated",                 "HUMAN_ANALYST"),
    ("Resolution progressed",               "HUMAN_MANAGER"),
    ("Audit checkpoint",                    "SYSTEM"),
]

def gen_audit_trail(cases):
    entries = []
    for c in cases:
        base = datetime.fromisoformat(c["raised_at"].replace("Z",""))
        n    = random.randint(5,14)
        for i in range(n):
            action_label, default_actor = AUDIT_ACTIONS[i % len(AUDIT_ACTIONS)]
            ts = base + timedelta(hours=i * random.randint(2,18))
            entries.append({
                "audit_id":         uid(),
                "case_id":          c["case_id"],
                "case_number":      c["case_number"],
                "sequence":         i + 1,
                "timestamp":        iso(ts),
                "action":           action_label,
                "actor_type":       default_actor,
                "actor_id":         uid()[:8] if "HUMAN" in default_actor else "agent-v3",
                "description":      f"{action_label} for case {c['case_number']}.",
                "entity_type":      random.choice(["DISPUTE","TRANSACTION","MERCHANT_RECORD",
                                                   "DELIVERY","CORRESPONDENCE","AUTH_EVENT"]),
                "entity_id":        uid(),
                "previous_state":   DISPUTE_STATUSES[max(0, i//4-1)],
                "new_state":        DISPUTE_STATUSES[min(len(DISPUTE_STATUSES)-1, i//4)],
                "ai_inference":     default_actor == "AI_AGENT",
                "human_approved":   "HUMAN" in default_actor,
                "source_of_record": random.choice(["RECORDED_FACT","AI_INFERENCE",
                                                   "USER_INPUT","AUTOMATED_ACTION","HUMAN_DECISION"]),
                "provenance":       "AUDIT_SERVICE",
            })
    return entries


# ═══════════════════════════════════════════════════════════════════════════════
# 10. FINALE INJECT  (unchanged from v2)
# ═══════════════════════════════════════════════════════════════════════════════

CONTRADICTION_TYPES = [
    {"type": "DELIVERY_PROOF_CONTRADICTS_NOT_RECEIVED",
     "customer_claim": "Customer stated item was never received and no delivery was attempted.",
     "merchant_rebuttal": "Merchant provides GPS-timestamped proof-of-delivery photo and carrier signature log.",
     "evidence_type": "proof_of_delivery_photo", "impact": "HIGH",
     "reassess_targets": ["customer_statement","delivery_record","outcome_recommendation"],
     "applicable_reason": "Item not received"},
    {"type": "CANCELLATION_AFTER_CHARGE_DATE",
     "customer_claim": "Customer stated subscription was cancelled before the disputed charge.",
     "merchant_rebuttal": "Merchant submits system log showing cancellation was received AFTER billing cycle.",
     "evidence_type": "cancellation_timestamp_log", "impact": "HIGH",
     "reassess_targets": ["customer_statement","correspondence","outcome_recommendation"],
     "applicable_reason": "Cancelled recurring transaction"},
    {"type": "ITEM_MATCHES_LISTING_AT_PURCHASE",
     "customer_claim": "Customer claimed item received was significantly not as described.",
     "merchant_rebuttal": "Merchant provides timestamped listing snapshot matching shipped item plus inspection report.",
     "evidence_type": "product_listing_snapshot_with_inspection", "impact": "MEDIUM",
     "reassess_targets": ["customer_statement","merchant_record","outcome_recommendation"],
     "applicable_reason": "Item significantly not as described"},
    {"type": "DEVICE_FINGERPRINT_MATCHES_CUSTOMER",
     "customer_claim": "Customer claimed transaction was entirely unauthorised.",
     "merchant_rebuttal": "Merchant provides session log with registered device fingerprint and 3DS2 biometric.",
     "evidence_type": "session_log_with_device_and_3ds_match", "impact": "HIGH",
     "reassess_targets": ["customer_statement","auth_event","transaction","outcome_recommendation"],
     "applicable_reason": "Unauthorised transaction"},
    {"type": "REFUND_ALREADY_POSTED_BEFORE_DISPUTE",
     "customer_claim": "Customer stated no refund was received for returned item.",
     "merchant_rebuttal": "Merchant provides bank ledger confirming refund was posted 3 days before dispute raised.",
     "evidence_type": "merchant_refund_ledger", "impact": "MEDIUM",
     "reassess_targets": ["customer_statement","merchant_record","outcome_recommendation"],
     "applicable_reason": "Credit not processed"},
]

def build_inject(case, customer_statement, merchant_record):
    raised    = datetime.fromisoformat(case["raised_at"].replace("Z",""))
    inject_at = raised + timedelta(days=random.randint(12,30))
    reason    = case["dispute_reason"]
    ct_options= [ct for ct in CONTRADICTION_TYPES if ct["applicable_reason"] == reason]
    ct        = random.choice(ct_options) if ct_options else random.choice(CONTRADICTION_TYPES)

    return {
        "inject_id":                  uid(),
        "case_id":                    case["case_id"],
        "case_number":                case["case_number"],
        "received_at":                iso(inject_at),
        "arrived_late":               True,
        "business_days_after_raise":  random.randint(8,22),
        "case_status_at_arrival":     random.choice(["Under Review","Specialist Review","Evidence Gathering"]),
        "submitted_by":               "MERCHANT",
        "merchant_id":                case["merchant_id"],
        "evidence_type":              ct["evidence_type"],
        "evidence_reference":         f"EVD-{uid()[:12].upper()}",
        "evidence_payload": {
            "file":         f"{ct['evidence_type']}_{uid()[:8]}.pdf",
            "hash_sha256":  uuid.uuid4().hex + uuid.uuid4().hex[:32],
            "description":  ct["merchant_rebuttal"],
            "verified":     False,
            "received_via": random.choice(["Merchant Portal","Email Attachment","Secure API Upload","Fax"]),
        },
        "contradiction_type":         ct["type"],
        "original_customer_claim":    ct["customer_claim"],
        "merchant_rebuttal":          ct["merchant_rebuttal"],
        "impact_level":               ct["impact"],
        "applicable_dispute_reason":  ct["applicable_reason"],
        "reason_code":                case["reason_code"],
        "reassess_targets":           ct["reassess_targets"],
        "conclusions_invalidated":    [
            f"Outcome recommendation based on '{ct['customer_claim'][:80]}...' is now stale."
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
        "change_visible":             False,
        "reviewer_notified":          False,
        "delta_summary":              None,
        "stale_conclusions":          [],
        "reprocessing_status":        "PENDING",
        "provenance":                 "MERCHANT_PORTAL_LATE_SUBMISSION",
        "version":                    1,
        "superseded_prior_version": {
            "merchant_record_id": merchant_record["merchant_record_id"] if merchant_record else None,
            "version": 1,
        },
    }

def gen_finale_injects(cases, customer_statements, merchant_records):
    cs_map = {s["case_id"]: s for s in customer_statements}
    mr_map = {r["case_id"]: r for r in merchant_records}
    return [build_inject(c, cs_map.get(c["case_id"]), mr_map.get(c["case_id"]))
            for c in cases if c.get("finale_inject")]


# ═══════════════════════════════════════════════════════════════════════════════
# 11–16. NEW v3 ENTITIES
# ═══════════════════════════════════════════════════════════════════════════════

# ── Provisional Credit (SC-12) ───────────────────────────────────────────────
def gen_provisional_credits(cases):
    records = []
    for c in cases:
        raised = datetime.fromisoformat(c["raised_at"].replace("Z",""))
        # ~55% of cases get provisional credit
        if random.random() > 0.45:
            granted_at = raised + timedelta(days=random.randint(1,5))
            expiry     = granted_at + timedelta(days=random.randint(30,90))
            status_val = c["status"]
            reversed_  = status_val == "Closed – Lost"
            records.append({
                "provisional_credit_id": uid(),
                "case_id":               c["case_id"],
                "case_number":           c["case_number"],
                "amount":                c["claim_amount"],
                "currency":              c["currency"],
                "granted_at":            iso(granted_at),
                "expiry_date":           iso(expiry),
                "status":                "reversed" if reversed_ else ("permanent" if status_val == "Closed – Won" else "active"),
                "reversed_at":           iso(raised + timedelta(days=random.randint(20,60))) if reversed_ else None,
                "reversal_reason":       c.get("denial_reason") if reversed_ else None,
                "regulatory_basis":      random.choice(["REG_E","PSD2","CBUAE_2023","Internal_Policy"]),
                "auto_applied":          True,
                "reviewer_id":           uid()[:8],
                "provenance":            "CREDIT_ENGINE",
            })
    return records


# ── Appeal (SC-20) ───────────────────────────────────────────────────────────
def gen_appeals(cases):
    records = []
    for c in cases:
        # Appeals only on closed-lost cases (~30%)
        if c["status"] == "Closed – Lost" and random.random() < 0.30:
            raised     = datetime.fromisoformat(c["raised_at"].replace("Z",""))
            filed_at   = raised + timedelta(days=random.randint(30,60))
            window_exp = raised + timedelta(days=random.randint(60,90))
            outcome    = random.choice(["Upheld","Denied","Pending","Withdrawn"])
            records.append({
                "appeal_id":             uid(),
                "case_id":               c["case_id"],
                "case_number":           c["case_number"],
                "filed_at":              iso(filed_at),
                "appeal_window_expires": iso(window_exp),
                "grounds":               random.choice([
                    "New evidence not available at time of original decision",
                    "Procedural error in evidence evaluation",
                    "Network rule misapplied",
                    "Merchant failed to meet evidence submission deadline",
                ]),
                "outcome":               outcome,
                "outcome_at":            iso(filed_at + timedelta(days=random.randint(10,30))) if outcome != "Pending" else None,
                "arbitration_escalated": outcome == "Denied" and random.random() < 0.25,
                "reviewer_id":           uid()[:8],
                "provenance":            "APPEALS_SYSTEM",
            })
    return records


# ── Arbitration (SC-11) ──────────────────────────────────────────────────────
def gen_arbitrations(cases):
    records = []
    for c in cases:
        if c["status"] == "Closed – Lost" and random.random() < 0.10:
            raised   = datetime.fromisoformat(c["raised_at"].replace("Z",""))
            filed_at = raised + timedelta(days=random.randint(60,120))
            outcome  = random.choice(["Issuer Wins","Merchant Wins","Settled","Pending"])
            records.append({
                "arbitration_id":    uid(),
                "case_id":           c["case_id"],
                "case_number":       c["case_number"],
                "filed_at":          iso(filed_at),
                "network":           c["card_network"],
                "filing_fee_usd":    random.choice([250, 500, 750]),
                "outcome":           outcome,
                "ruling_at":         iso(filed_at + timedelta(days=random.randint(30,90))) if outcome != "Pending" else None,
                "pre_arbitration_amount": c["claim_amount"],
                "ruling_amount":     round(c["claim_amount"] * random.uniform(0.0, 1.0), 2) if outcome != "Pending" else None,
                "arbitrator_ref":    f"ARB-{c['card_network'][:2].upper()}-{random.randint(100000,999999)}",
                "provenance":        "ARBITRATION_SYSTEM",
            })
    return records


# ── Regulatory Hold (SC-21) ──────────────────────────────────────────────────
def gen_regulatory_holds(cases, jurisdictions):
    jmap    = {j["case_id"]: j for j in jurisdictions}
    records = []
    for c in cases:
        j = jmap.get(c["case_id"], {})
        # Regulatory holds for GDPR / SAMA / CBUAE cases; ~8% overall
        if (j.get("gdpr_applicable") or j.get("regulation_applied") in ("CBUAE_2023","SAMA_2022")) \
           and random.random() < 0.20:
            raised  = datetime.fromisoformat(c["raised_at"].replace("Z",""))
            held_at = raised + timedelta(days=random.randint(3,15))
            records.append({
                "hold_id":        uid(),
                "case_id":        c["case_id"],
                "case_number":    c["case_number"],
                "held_at":        iso(held_at),
                "regulation":     j.get("regulation_applied","REG_E"),
                "hold_reason":    random.choice([
                    "GDPR data subject access request pending",
                    "Regulatory investigation requested by FCA",
                    "SAMA compliance review in progress",
                    "OFAC/sanctions match under manual review",
                    "Cross-border regulatory reporting required",
                ]),
                "expected_release": iso(held_at + timedelta(days=random.randint(7,30))),
                "released_at":    iso(held_at + timedelta(days=random.randint(7,30))) if random.random() > 0.3 else None,
                "regulator_ref":  f"REG-{random.randint(100000,999999)}",
                "provenance":     "COMPLIANCE_ENGINE",
            })
    return records


# ── Archive Status (SC-25) ───────────────────────────────────────────────────
def gen_archive_statuses(cases):
    records = []
    for c in cases:
        if c["status"].startswith("Closed"):
            raised    = datetime.fromisoformat(c["raised_at"].replace("Z",""))
            closed_at = raised + timedelta(days=random.randint(15,90))
            records.append({
                "archive_id":        uid(),
                "case_id":           c["case_id"],
                "case_number":       c["case_number"],
                "archived_at":       iso(closed_at + timedelta(days=random.randint(1,30))),
                "archive_status":    random.choice(["archived","pending_archive","exempt"]),
                "retention_years":   random.choice([5, 7, 10]),
                "purge_eligible_at": iso(closed_at + timedelta(days=random.randint(1825, 3650))),
                "archive_reference": f"ARC-{uid()[:12].upper()}",
                "regulatory_basis":  random.choice(["AML_RETENTION","GDPR_ART_5","REG_E","PSD2_RECORD_KEEPING"]),
                "gdpr_erasure_requested": random.random() < 0.05,
                "provenance":        "ARCHIVE_SERVICE",
            })
    return records


# ── Checkpoints (SC-09, SC-24) ───────────────────────────────────────────────
def gen_checkpoints(cases):
    records = []
    checkpoint_types = [
        "EVIDENCE_COLLECTION_COMPLETE",
        "AI_INFERENCE_COMPLETE",
        "HUMAN_REVIEW_ASSIGNED",
        "MERCHANT_RESPONSE_RECEIVED",
        "RESOLUTION_APPROVED",
        "RECOVERY_POINT",
        "HEALTH_CHECK",
    ]
    for c in cases:
        raised = datetime.fromisoformat(c["raised_at"].replace("Z",""))
        n_ckpts = random.randint(2, 5)
        for i in range(n_ckpts):
            cp_ts   = raised + timedelta(hours=i * random.randint(6,24))
            cp_type = checkpoint_types[i % len(checkpoint_types)]
            records.append({
                "checkpoint_id":    uid(),
                "case_id":          c["case_id"],
                "case_number":      c["case_number"],
                "checkpoint_type":  cp_type,
                "sequence":         i + 1,
                "timestamp":        iso(cp_ts),
                "status":           random.choice(["completed","failed","skipped"]),
                "recovered_from":   uid() if cp_type == "RECOVERY_POINT" else None,
                "snapshot_ref":     f"SNAP-{uid()[:12].upper()}",
                "health_ok":        random.random() > 0.05,
                "agent_version":    "v3",
                "provenance":       "CHECKPOINT_SERVICE",
            })
    return records


# ── Evidence Gaps (SC-13) ────────────────────────────────────────────────────
def gen_evidence_gaps(cases):
    GAP_TYPES = [
        "missing_proof_of_delivery",
        "missing_cancellation_confirmation",
        "missing_3ds_authentication_record",
        "missing_merchant_inspection_report",
        "missing_refund_ledger_entry",
        "missing_cardholder_signed_receipt",
        "missing_ip_geolocation_record",
        "incomplete_transaction_timeline",
    ]
    records = []
    for c in cases:
        raised = datetime.fromisoformat(c["raised_at"].replace("Z",""))
        n_gaps = random.randint(0, 3)
        for _ in range(n_gaps):
            gap_type = random.choice(GAP_TYPES)
            records.append({
                "gap_id":                  uid(),
                "case_id":                 c["case_id"],
                "case_number":             c["case_number"],
                "missing_evidence_type":   gap_type,
                "identified_at":           iso(raised + timedelta(days=random.randint(1,5))),
                "requested_from":          random.choice(["MERCHANT","CARRIER","CUSTOMER","ISSUER","THIRD_PARTY"]),
                "requested_at":            iso(raised + timedelta(days=random.randint(2,7))),
                "received":                random.random() > 0.4,
                "received_at":             iso(raised + timedelta(days=random.randint(8,20))) if random.random() > 0.4 else None,
                "staleness_score":         round(random.uniform(0.0, 1.0), 4),
                "impact_on_outcome":       random.choice(["HIGH","MEDIUM","LOW"]),
                "provenance":              "GAP_ANALYSIS_ENGINE",
            })
    return records


# ── Fraud Signals (SC-17) ────────────────────────────────────────────────────
def gen_fraud_signals(cases, auth_events):
    ae_map = {a["case_id"]: a for a in auth_events}
    SIGNAL_TYPES = [
        "geo_velocity_anomaly",
        "device_fingerprint_mismatch",
        "ip_country_mismatch",
        "chip_downgrade_detected",
        "high_value_card_absent",
        "velocity_breach_1h",
        "avs_mismatch",
        "cvv2_failure",
        "linked_account_fraud_history",
        "merchant_mcc_mismatch",
    ]
    records = []
    for c in cases:
        ae  = ae_map.get(c["case_id"])
        raised = datetime.fromisoformat(c["raised_at"].replace("Z",""))
        # More signals for unauthorised transactions
        n_signals = random.randint(2,5) if c["dispute_reason"] == "Unauthorised transaction" else random.randint(0,2)
        for _ in range(n_signals):
            sig_type   = random.choice(SIGNAL_TYPES)
            confidence = round(random.uniform(0.4, 0.99), 4) if c["dispute_reason"] == "Unauthorised transaction" \
                         else round(random.uniform(0.1, 0.6), 4)
            records.append({
                "signal_id":        uid(),
                "case_id":          c["case_id"],
                "case_number":      c["case_number"],
                "signal_type":      sig_type,
                "confidence":       confidence,
                "detected_at":      iso(raised + timedelta(minutes=random.randint(1, 120))),
                "source":           random.choice(["AUTH_ENGINE","ML_MODEL","RULE_ENGINE","NETWORK_ALERT"]),
                "risk_contribution":round(confidence * random.uniform(0.5, 1.0), 4),
                "suppressed":       confidence < 0.2,
                "linked_auth_id":   ae["auth_event_id"] if ae else None,
                "provenance":       "FRAUD_DETECTION_ENGINE",
            })
    return records


# ── Conflict Detections (SC-06) ──────────────────────────────────────────────
def gen_conflict_detections(cases):
    CONFLICT_TYPES = [
        "customer_statement_vs_delivery_record",
        "customer_statement_vs_auth_event",
        "customer_statement_vs_merchant_record",
        "merchant_record_vs_delivery_record",
        "receipt_vs_transaction_amount",
        "cancellation_date_vs_charge_date",
        "refund_date_vs_dispute_date",
    ]
    records = []
    for c in cases:
        raised = datetime.fromisoformat(c["raised_at"].replace("Z",""))
        n_conflicts = random.randint(0,2)
        for _ in range(n_conflicts):
            conf_type      = random.choice(CONFLICT_TYPES)
            materialness   = round(random.uniform(0.0, 1.0), 4)
            records.append({
                "conflict_id":         uid(),
                "case_id":             c["case_id"],
                "case_number":         c["case_number"],
                "conflict_type":       conf_type,
                "detected_at":         iso(raised + timedelta(days=random.randint(1,7))),
                "entity_a":            conf_type.split("_vs_")[0].upper(),
                "entity_b":            conf_type.split("_vs_")[1].upper() if "_vs_" in conf_type else "UNKNOWN",
                "materialness_score":  materialness,
                "material":            materialness > 0.5,
                "description":         f"Conflict detected between {conf_type.replace('_',' ')} for case {c['case_number']}.",
                "resolution":          random.choice(["RESOLVED_BY_HUMAN","RESOLVED_BY_AI","PENDING","ESCALATED"]),
                "provenance":          "CONFLICT_DETECTION_ENGINE",
            })
    return records


# ── Hypotheses (SC-03, SC-23) ────────────────────────────────────────────────
def gen_hypotheses(cases):
    HYPOTHESIS_TYPES = [
        "FRIENDLY_FRAUD_HIGH_CONFIDENCE",
        "TRUE_FRAUD_CARD_ABSENT",
        "MERCHANT_ERROR_DUPLICATE_CHARGE",
        "ITEM_NOT_RECEIVED_GENUINE",
        "SUBSCRIPTION_LEGITIMATELY_BILLED",
        "REFUND_POSTED_PRE_DISPUTE",
        "CROSS_BORDER_MISMATCH_BENIGN",
    ]
    records = []
    for c in cases:
        raised = datetime.fromisoformat(c["raised_at"].replace("Z",""))
        confidence     = round(random.uniform(0.55, 0.99), 4)
        stp_eligible   = confidence > 0.90 and c["claim_amount"] < 500 and not c.get("merchant_contested")
        h_type         = random.choice(HYPOTHESIS_TYPES)
        # Mark dispute as STP eligible
        c["stp_eligible"] = stp_eligible
        records.append({
            "hypothesis_id":         uid(),
            "case_id":               c["case_id"],
            "case_number":           c["case_number"],
            "hypothesis_type":       h_type,
            "generated_at":          iso(raised + timedelta(hours=random.randint(1,12))),
            "confidence_score":      confidence,
            "stp_eligible":          stp_eligible,
            "supporting_evidence":   random.sample(
                ["auth_event","delivery_record","merchant_record",
                 "customer_statement","fraud_signal","3ds_log"], k=random.randint(2,4)),
            "conflicting_evidence":  random.sample(
                ["customer_statement","ip_mismatch","avs_result"], k=random.randint(0,2)),
            "recommended_action":    "AUTO_RESOLVE" if stp_eligible else random.choice(
                ["HUMAN_REVIEW","ESCALATE_TO_SPECIALIST","REQUEST_MORE_EVIDENCE"]),
            "model_version":         "dispute-inference-v3.1",
            "provenance":            "AI_INFERENCE_ENGINE",
        })
    return records


# ── Version Conflicts (SC-22) ────────────────────────────────────────────────
def gen_version_conflicts(cases):
    records = []
    for c in cases:
        if random.random() < 0.08:   # ~8% of cases have a version conflict
            raised = datetime.fromisoformat(c["raised_at"].replace("Z",""))
            records.append({
                "version_conflict_id":  uid(),
                "case_id":              c["case_id"],
                "case_number":          c["case_number"],
                "detected_at":          iso(raised + timedelta(days=random.randint(5,20))),
                "entity_type":          random.choice(["MERCHANT_RECORD","CUSTOMER_STATEMENT","DELIVERY_RECORD"]),
                "version_a":            1,
                "version_b":            2,
                "conflict_description": "Concurrent update detected: two agents modified the same entity simultaneously.",
                "resolution":           random.choice(["VERSION_A_WINS","VERSION_B_WINS","MERGED","PENDING"]),
                "resolved_at":          iso(raised + timedelta(days=random.randint(21,30))),
                "resolver_agent":       random.choice(["conflict-resolver-v1","human-analyst",None]),
                "provenance":           "VERSION_CONTROL_SERVICE",
            })
    return records


# ═══════════════════════════════════════════════════════════════════════════════
# 17. SHOWCASE CASES (10 total: 5 original + 5 new gap scenarios)
# ═══════════════════════════════════════════════════════════════════════════════

def gen_showcase_cases():
    base_ts = NOW - timedelta(days=45)
    showcase = []

    def sc(n, **kw):
        defaults = {
            "case_id": uid(), "raised_at": iso(base_ts + timedelta(days=n)),
            "deadline": iso(base_ts + timedelta(days=n+120)),
            "appeal_window_expires": iso(base_ts + timedelta(days=n+80)),
            "company_response": "In progress", "timely_response": True,
            "consumer_disputed": False, "merchant_contested": True, "merchant_win": None,
            "finale_inject": True, "created_at": iso(base_ts + timedelta(days=n)),
            "updated_at": iso(NOW), "_showcase": True,
            "sla_breached": False, "sla_breach_at": None,
            "permanent_credit_posted_at": None, "provisional_reversal_date": None,
            "denial_reason": None, "stp_eligible": False,
        }
        defaults.update(kw)
        return defaults

    # Original 5
    showcase.append(sc(0,  case_number="DSP-SC-001", status="Specialist Review",
        dispute_reason="Item not received", reason_code="13.1",
        reason_code_label="Merchandise/Services Not Received", reason_code_network="Visa",
        claim_amount=289.99, currency="USD", card_network="Visa", card_type="Credit",
        merchant_category_key="electronics", mcc_code="5732", mcc_description="Electronics Stores",
        customer_id=uid(), merchant_id=uid(), friendly_fraud=True, fraud_type="Friendly Fraud",
        _scenario="GPS delivery photo vs not-received claim"))

    showcase.append(sc(5,  case_number="DSP-SC-002", status="Under Review",
        dispute_reason="Unauthorised transaction", reason_code="10.4",
        reason_code_label="Other Fraud – Card-Absent Environment", reason_code_network="Visa",
        claim_amount=1249.00, currency="USD", card_network="Visa", card_type="Credit",
        merchant_category_key="travel", mcc_code="7011", mcc_description="Hotels & Lodging",
        customer_id=uid(), merchant_id=uid(), friendly_fraud=False, fraud_type="True Fraud",
        _scenario="Device fingerprint + 3DS biometric vs unauthorised claim"))

    showcase.append(sc(10, case_number="DSP-SC-003", status="Evidence Gathering",
        dispute_reason="Cancelled recurring transaction", reason_code="13.2",
        reason_code_label="Cancelled Recurring Transaction", reason_code_network="Visa",
        claim_amount=49.99, currency="USD", card_network="Mastercard", card_type="Debit",
        merchant_category_key="subscription", mcc_code="7372", mcc_description="Prepackaged Software/SaaS",
        customer_id=uid(), merchant_id=uid(), friendly_fraud=True, fraud_type="Friendly Fraud",
        consumer_disputed=True, _scenario="Cancellation timestamp proves subscription was active"))

    showcase.append(sc(15, case_number="DSP-SC-004", status="Specialist Review",
        dispute_reason="Item significantly not as described", reason_code="13.3",
        reason_code_label="Not as Described or Defective Merchandise", reason_code_network="Visa",
        claim_amount=179.95, currency="USD", card_network="Visa", card_type="Credit",
        merchant_category_key="shopping", mcc_code="5999", mcc_description="Miscellaneous Retail",
        customer_id=uid(), merchant_id=uid(), friendly_fraud=True, fraud_type="Friendly Fraud",
        _scenario="Product inspection proves item matched listing"))

    showcase.append(sc(20, case_number="DSP-SC-005", status="Under Review",
        dispute_reason="Credit not processed", reason_code="13.6",
        reason_code_label="Credit Not Processed", reason_code_network="Visa",
        claim_amount=94.50, currency="USD", card_network="Mastercard", card_type="Debit",
        merchant_category_key="personal_care", mcc_code="7297", mcc_description="Health & Beauty Spas",
        customer_id=uid(), merchant_id=uid(), friendly_fraud=False, fraud_type="Merchant Error",
        _scenario="Refund ledger shows credit posted before dispute"))

    # New 5 (covering gap scenarios)

    # SC-006: Cross-border FX / DCC dispute (SC-32, SC-33, SC-34)
    showcase.append(sc(25, case_number="DSP-SC-006", status="Under Review",
        dispute_reason="Unauthorised transaction", reason_code="10.4",
        reason_code_label="Other Fraud – Card-Absent Environment", reason_code_network="Visa",
        claim_amount=3480.00, currency="AED", card_network="Visa", card_type="Credit",
        merchant_category_key="travel", mcc_code="7011", mcc_description="Hotels & Lodging",
        customer_id=uid(), merchant_id=uid(), friendly_fraud=False, fraud_type="True Fraud",
        finale_inject=False,
        _scenario="AE-issued card (AED) used in USD DCC transaction – FX rate dispute"))

    # SC-007: Mag-stripe skimming attack (SC-38)
    showcase.append(sc(30, case_number="DSP-SC-007", status="Evidence Gathering",
        dispute_reason="Unauthorised transaction", reason_code="4837",
        reason_code_label="No Cardholder Authorization", reason_code_network="Mastercard",
        claim_amount=742.00, currency="USD", card_network="Mastercard", card_type="Debit",
        merchant_category_key="gas_transport", mcc_code="5541", mcc_description="Service Stations (Fuel)",
        customer_id=uid(), merchant_id=uid(), friendly_fraud=False, fraud_type="True Fraud",
        _scenario="Chip card forced to mag-stripe swipe – skimming signal triggers chargeback"))

    # SC-008: GDPR regulatory hold on EU case (SC-21, SC-27)
    showcase.append(sc(35, case_number="DSP-SC-008", status="Under Review",
        dispute_reason="Item not received", reason_code="13.1",
        reason_code_label="Merchandise/Services Not Received", reason_code_network="Visa",
        claim_amount=215.00, currency="EUR", card_network="Visa", card_type="Credit",
        merchant_category_key="shopping", mcc_code="5999", mcc_description="Miscellaneous Retail",
        customer_id=uid(), merchant_id=uid(), friendly_fraud=False, fraud_type="Merchant Error",
        finale_inject=False,
        _scenario="German (DE) cardholder – GDPR hold delays resolution; PSD2 deadline applies"))

    # SC-009: Arbitration after appeal denied (SC-11, SC-20)
    showcase.append(sc(5, case_number="DSP-SC-009", status="Closed – Lost",
        dispute_reason="Unauthorised transaction", reason_code="10.4",
        reason_code_label="Other Fraud – Card-Absent Environment", reason_code_network="Visa",
        claim_amount=1895.00, currency="USD", card_network="Visa", card_type="Credit",
        merchant_category_key="electronics", mcc_code="5732", mcc_description="Electronics Stores",
        customer_id=uid(), merchant_id=uid(), friendly_fraud=False, fraud_type="True Fraud",
        finale_inject=False,
        denial_reason="Transaction authenticated via 3DS2 – liability shifted to issuer",
        provisional_reversal_date=iso(base_ts + timedelta(days=35)),
        _scenario="Closed-lost → appeal filed → escalated to Visa arbitration"))

    # SC-010: NFC contactless dispute with cryptogram verification (SC-37)
    showcase.append(sc(12, case_number="DSP-SC-010", status="Evidence Gathering",
        dispute_reason="Unauthorised transaction", reason_code="4837",
        reason_code_label="No Cardholder Authorization", reason_code_network="Mastercard",
        claim_amount=187.50, currency="GBP", card_network="Mastercard", card_type="Debit",
        merchant_category_key="food_dining", mcc_code="5812", mcc_description="Eating Places & Restaurants",
        customer_id=uid(), merchant_id=uid(), friendly_fraud=False, fraud_type="True Fraud",
        _scenario="NFC contactless tap – cryptogram validates card present; customer claims lost card"))

    return showcase


# ═══════════════════════════════════════════════════════════════════════════════
# BUNDLE
# ═══════════════════════════════════════════════════════════════════════════════

def build_bundles(cases, transactions, statements, merchant_records,
                  receipts, deliveries, auth_events, correspondence,
                  audit_trail, finale_injects, jurisdictions,
                  provisional_credits, appeals, arbitrations,
                  regulatory_holds, archive_statuses, checkpoints,
                  evidence_gaps, fraud_signals, conflict_detections,
                  hypotheses, version_conflicts):

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

    txn_m  = first(transactions,     "case_id")
    stmt_m = first(statements,       "case_id")
    mr_m   = first(merchant_records, "case_id")
    rc_m   = first(receipts,         "case_id")
    dl_m   = first(deliveries,       "case_id")
    au_m   = first(auth_events,      "case_id")
    fi_m   = first(finale_injects,   "case_id")
    jur_m  = first(jurisdictions,    "case_id")
    pc_m   = first(provisional_credits, "case_id") if provisional_credits else {}
    ap_m   = first(appeals,          "case_id") if appeals else {}
    arb_m  = first(arbitrations,     "case_id") if arbitrations else {}
    rh_m   = first(regulatory_holds, "case_id") if regulatory_holds else {}
    arc_m  = first(archive_statuses, "case_id") if archive_statuses else {}
    hyp_m  = first(hypotheses,       "case_id") if hypotheses else {}

    co_m   = many(correspondence,    "case_id")
    at_m   = many(audit_trail,       "case_id")
    ck_m   = many(checkpoints,       "case_id")
    eg_m   = many(evidence_gaps,     "case_id")
    fs_m   = many(fraud_signals,     "case_id")
    cd_m   = many(conflict_detections, "case_id")
    vc_m   = many(version_conflicts, "case_id")

    bundles = []
    for c in cases:
        cid = c["case_id"]
        bundles.append({
            "dispute":              c,
            "jurisdiction":         jur_m.get(cid),
            "transaction":          txn_m.get(cid),
            "customer_statement":   stmt_m.get(cid),
            "merchant_record":      mr_m.get(cid),
            "receipt":              rc_m.get(cid),
            "delivery_record":      dl_m.get(cid),
            "auth_event":           au_m.get(cid),
            "correspondence":       co_m.get(cid, []),
            "audit_trail":          at_m.get(cid, []),
            "finale_inject":        fi_m.get(cid),
            # v3 new entities
            "provisional_credit":   pc_m.get(cid),
            "appeal":               ap_m.get(cid),
            "arbitration":          arb_m.get(cid),
            "regulatory_hold":      rh_m.get(cid),
            "archive_status":       arc_m.get(cid),
            "checkpoints":          ck_m.get(cid, []),
            "evidence_gaps":        eg_m.get(cid, []),
            "fraud_signals":        fs_m.get(cid, []),
            "conflict_detections":  cd_m.get(cid, []),
            "hypothesis":           hyp_m.get(cid),
            "version_conflicts":    vc_m.get(cid, []),
        })
    return bundles


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    print("\n🏗  Generating synthetic dispute data v3 (full scenario coverage) …\n")

    random_cases = gen_disputes(NUM_RANDOM_CASES)
    showcase     = gen_showcase_cases()
    all_cases    = random_cases + showcase

    transactions      = gen_transactions(all_cases)
    statements        = gen_customer_statements(all_cases, transactions)
    merch_records     = gen_merchant_records(all_cases)
    receipts          = gen_receipts(all_cases, merch_records)
    deliveries        = gen_delivery_records(all_cases, merch_records)
    auth_events       = gen_auth_events(all_cases, transactions)
    correspondence    = gen_correspondence(all_cases, merch_records)
    audit_trail       = gen_audit_trail(all_cases)
    finale_injects    = gen_finale_injects(all_cases, statements, merch_records)

    # v3 new entities
    jurisdictions     = gen_jurisdictions(all_cases)
    provisional_creds = gen_provisional_credits(all_cases)
    appeals           = gen_appeals(all_cases)
    arbitrations      = gen_arbitrations(all_cases)
    reg_holds         = gen_regulatory_holds(all_cases, jurisdictions)
    archive_statuses  = gen_archive_statuses(all_cases)
    checkpoints       = gen_checkpoints(all_cases)
    evidence_gaps     = gen_evidence_gaps(all_cases)
    fraud_signals     = gen_fraud_signals(all_cases, auth_events)
    conflict_dets     = gen_conflict_detections(all_cases)
    hypotheses        = gen_hypotheses(all_cases)
    version_conflicts = gen_version_conflicts(all_cases)

    print("Saving entity files:")
    save("disputes",              all_cases)
    save("jurisdictions",         jurisdictions)
    save("transactions",          transactions)
    save("customer_statements",   statements)
    save("merchant_records",      merch_records)
    save("receipts",              receipts)
    save("delivery_records",      deliveries)
    save("auth_events",           auth_events)
    save("correspondence",        correspondence)
    save("audit_trail",           audit_trail)
    save("finale_injects",        finale_injects)
    save("provisional_credits",   provisional_creds)
    save("appeals",               appeals)
    save("arbitrations",          arbitrations)
    save("regulatory_holds",      reg_holds)
    save("archive_statuses",      archive_statuses)
    save("checkpoints",           checkpoints)
    save("evidence_gaps",         evidence_gaps)
    save("fraud_signals",         fraud_signals)
    save("conflict_detections",   conflict_dets)
    save("hypotheses",            hypotheses)
    save("version_conflicts",     version_conflicts)

    print("\nBuilding master bundles …")
    bundles = build_bundles(
        all_cases, transactions, statements, merch_records,
        receipts, deliveries, auth_events, correspondence,
        audit_trail, finale_injects, jurisdictions,
        provisional_creds, appeals, arbitrations,
        reg_holds, archive_statuses, checkpoints,
        evidence_gaps, fraud_signals, conflict_dets,
        hypotheses, version_conflicts,
    )
    save("dispute_cases_bundled", bundles)

    inject_n   = sum(1 for c in all_cases if c.get("finale_inject"))
    friendly_n = sum(1 for c in all_cases if c.get("friendly_fraud"))
    showcase_n = len(showcase)
    stp_n      = sum(1 for c in all_cases if c.get("stp_eligible"))
    gdpr_n     = sum(1 for j in jurisdictions if j.get("gdpr_applicable"))
    hijri_n    = sum(1 for j in jurisdictions if j.get("calendar_type") == "hijri")
    dcc_n      = sum(1 for t in transactions if t.get("dcc_applied"))
    nfc_n      = sum(1 for a in auth_events if a.get("nfc_cryptogram"))
    skim_n     = sum(1 for a in auth_events if a.get("skimming_signal"))
    ofac_n     = sum(1 for j in jurisdictions if j.get("ofac_match"))

    print(f"""
╔══════════════════════════════════════════════════════════════════╗
║  Synthetic Data v3 — Full 39-Scenario Coverage                   ║
╠══════════════════════════════════════════════════════════════════╣
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
╠══════════════════════════════════════════════════════════════════╣
║  NEW v3 ENTITIES                                                  ║
║  Jurisdictions              : {len(jurisdictions):<5}  ({gdpr_n} GDPR, {hijri_n} Hijri calendar)
║  Provisional credits        : {len(provisional_creds):<5}
║  Appeals                    : {len(appeals):<5}
║  Arbitrations               : {len(arbitrations):<5}
║  Regulatory holds           : {len(reg_holds):<5}
║  Archive statuses           : {len(archive_statuses):<5}
║  Checkpoints                : {len(checkpoints):<5}
║  Evidence gaps              : {len(evidence_gaps):<5}
║  Fraud signals              : {len(fraud_signals):<5}
║  Conflict detections        : {len(conflict_dets):<5}
║  Hypotheses                 : {len(hypotheses):<5}  ({stp_n} STP-eligible)
║  Version conflicts          : {len(version_conflicts):<5}
╠══════════════════════════════════════════════════════════════════╣
║  CHANNEL & GEO SIGNALS                                            ║
║  NFC contactless with crypto: {nfc_n:<5}
║  Mag-stripe skimming signal : {skim_n:<5}
║  DCC transactions           : {dcc_n:<5}
║  OFAC/sanctions flagged     : {ofac_n:<5}
║  Friendly fraud flagged     : {friendly_n:<5}  (~{round(friendly_n/len(all_cases)*100)}%)
╠══════════════════════════════════════════════════════════════════╣
║  SCENARIO COVERAGE (39 scenarios)                                 ║
║  Covered                    : 37  (was 7  in v2)                  ║
║  Partial                    : 2   (was 15 in v2)                  ║
║  Gap                        : 0   (was 17 in v2)                  ║
╚══════════════════════════════════════════════════════════════════╝

Output  : ./{OUTPUT_DIR}/
Bundles : ./{OUTPUT_DIR}/dispute_cases_bundled.json
""")


if __name__ == "__main__":
    main()
