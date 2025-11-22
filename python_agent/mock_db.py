# mock_db.py
# AI-generated code section begins - GitHub Copilot assisted with creating comprehensive healthcare mock data

# 1. SPECIALIST REGISTRY - Rich doctor database with complete information
SPECIALIST_REGISTRY = {
    "cardiology": [
        {
            "name": "Dr. Emily Chen",
            "npi": "1457389201",
            "clinic": "Mercy Heart Institute",
            "rating": 4.9,
            "address": "1234 Medical Plaza Dr, San Francisco, CA 94115"
        },
        {
            "name": "Dr. Marcus Thorne",
            "npi": "1892039485",
            "clinic": "Sutter Cardiovascular Center",
            "rating": 4.2,
            "address": "5678 Health Blvd, Oakland, CA 94612"
        },
        {
            "name": "Dr. Jennifer Rodriguez",
            "npi": "1567234890",
            "clinic": "Pacific Heart Group",
            "rating": 4.7,
            "address": "9012 Cardio Way, San Jose, CA 95123"
        }
    ],
    "dermatology": [
        {
            "name": "Dr. Sarah Lee",
            "npi": "1239048572",
            "clinic": "Bay Area Skin Health Institute",
            "rating": 4.8,
            "address": "3456 Derma Ave, Palo Alto, CA 94301"
        },
        {
            "name": "Dr. Kevin Patel",
            "npi": "1928374650",
            "clinic": "Valley Dermatology Associates",
            "rating": 4.5,
            "address": "7890 Skin Care Lane, Fremont, CA 94536"
        },
        {
            "name": "Dr. Michelle Williams",
            "npi": "1345678901",
            "clinic": "Advanced Dermatology Center",
            "rating": 4.6,
            "address": "2468 Beauty Blvd, Berkeley, CA 94704"
        }
    ],
    "orthopedics": [
        {
            "name": "Dr. Brock Stone",
            "npi": "1122334455",
            "clinic": "Bay Joint & Spine Center",
            "rating": 4.7,
            "address": "1357 Bone Ave, San Mateo, CA 94403"
        },
        {
            "name": "Dr. Amanda Foster",
            "npi": "1987654321",
            "clinic": "Silicon Valley Orthopedics",
            "rating": 4.4,
            "address": "2468 Sports Medicine Dr, Santa Clara, CA 95051"
        },
        {
            "name": "Dr. Robert Kim",
            "npi": "1456789012",
            "clinic": "Peninsula Bone & Joint",
            "rating": 4.8,
            "address": "3691 Movement Way, Redwood City, CA 94063"
        }
    ],
    "neurology": [
        {
            "name": "Dr. Lisa Thompson",
            "npi": "1678901234",
            "clinic": "Northern California Neurology",
            "rating": 4.9,
            "address": "4567 Brain Ave, San Francisco, CA 94117"
        },
        {
            "name": "Dr. Michael Chang",
            "npi": "1789012345",
            "clinic": "Bay Area Neurological Institute",
            "rating": 4.3,
            "address": "8901 Neural Network Dr, Mountain View, CA 94041"
        },
        {
            "name": "Dr. Patricia Davis",
            "npi": "1890123456",
            "clinic": "Advanced Neuroscience Center",
            "rating": 4.6,
            "address": "1234 Cognitive Ct, Sunnyvale, CA 94087"
        }
    ]
}

# 2. INSURANCE PLANS - Comprehensive coverage rules
INSURANCE_PLANS = {
    "Blue Cross": {
        "covered_specialties": ["cardiology", "dermatology", "orthopedics", "neurology"],
        "copay": "$25.00",
        "deductible": "$500",
        "network": "Preferred Provider"
    },
    "Kaiser": {
        "covered_specialties": ["general_practice"],  # Kaiser is restrictive for specialists
        "copay": "$15.00",
        "deductible": "$0",
        "network": "HMO Network Only"
    },
    "Medi-Cal": {
        "covered_specialties": ["cardiology", "orthopedics", "neurology"],
        "copay": "$0.00",
        "deductible": "$0",
        "network": "State Approved Providers"
    }
}

# 3. PROCEDURE CODES - CPT codes mapped by specialty
PROCEDURE_CODES = {
    "cardiology": [
        {"code": "99244", "description": "Office consultation for cardiac evaluation", "cost": "$450"},
        {"code": "93000", "description": "Electrocardiogram (ECG/EKG)", "cost": "$150"},
        {"code": "93307", "description": "Echocardiography transthoracic", "cost": "$800"},
        {"code": "93458", "description": "Cardiac catheterization", "cost": "$2500"}
    ],
    "dermatology": [
        {"code": "99213", "description": "Office visit dermatological examination", "cost": "$200"},
        {"code": "11100", "description": "Biopsy of skin lesion", "cost": "$300"},
        {"code": "17000", "description": "Destruction of skin lesion", "cost": "$250"},
        {"code": "11403", "description": "Excision of skin lesion", "cost": "$400"}
    ],
    "orthopedics": [
        {"code": "99243", "description": "Office consultation orthopedic evaluation", "cost": "$350"},
        {"code": "73060", "description": "X-ray of knee", "cost": "$120"},
        {"code": "73721", "description": "MRI of joint", "cost": "$1200"},
        {"code": "29881", "description": "Arthroscopy knee with meniscectomy", "cost": "$3500"}
    ],
    "neurology": [
        {"code": "99245", "description": "Office consultation neurological evaluation", "cost": "$500"},
        {"code": "95860", "description": "Electromyography (EMG)", "cost": "$400"},
        {"code": "70553", "description": "MRI brain with contrast", "cost": "$2000"},
        {"code": "95116", "description": "EEG monitoring", "cost": "$600"}
    ],
    "default": [
        {"code": "99499", "description": "Unlisted evaluation and management service", "cost": "$300"},
        {"code": "99213", "description": "Office or other outpatient visit", "cost": "$200"},
        {"code": "99214", "description": "Office or other outpatient visit (detailed)", "cost": "$250"}
    ]
}

# 4. DIAGNOSIS CODES - ICD-10 codes mapped by specialty
DIAGNOSIS_CODES = {
    "cardiology": [
        {"code": "I25.10", "description": "Atherosclerotic heart disease"},
        {"code": "I50.9", "description": "Heart failure, unspecified"},
        {"code": "I20.9", "description": "Angina pectoris, unspecified"},
        {"code": "I48.91", "description": "Atrial fibrillation"}
    ],
    "dermatology": [
        {"code": "L30.9", "description": "Dermatitis, unspecified"},
        {"code": "C44.92", "description": "Skin malignancy"},
        {"code": "L70.0", "description": "Acne vulgaris"},
        {"code": "L40.9", "description": "Psoriasis, unspecified"}
    ],
    "orthopedics": [
        {"code": "M25.561", "description": "Pain in right knee"},
        {"code": "M54.5", "description": "Low back pain"},
        {"code": "M75.30", "description": "Rotator cuff tear"},
        {"code": "S72.001A", "description": "Fracture of femur"}
    ],
    "neurology": [
        {"code": "G43.909", "description": "Migraine, unspecified"},
        {"code": "G40.909", "description": "Epilepsy, unspecified"},
        {"code": "G35", "description": "Multiple sclerosis"},
        {"code": "F03.90", "description": "Dementia, unspecified"}
    ],
    "default": [
        {"code": "R69", "description": "Illness, unspecified"},
        {"code": "Z00.00", "description": "Encounter for general adult medical examination"},
        {"code": "R06.02", "description": "Shortness of breath"}
    ]
}

# AI-generated code section ends