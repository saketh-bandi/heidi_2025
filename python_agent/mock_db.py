# mock_db.py
# AI-generated code section begins - GitHub Copilot assisted with creating comprehensive healthcare mock data for hackathon demo

# ==========================================
# 1. SPECIALIST REGISTRY - 5 Doctors per Specialty
# ==========================================

SPECIALIST_REGISTRY = {
    "cardiology": [
        {
            "name": "Dr. Emily Chen",
            "npi": "1457389201",
            "clinic": "Mercy Heart Institute",
            "rating": 4.9,
            "address": "1234 Medical Plaza Dr, San Francisco, CA 94115",
            "phone": "(415) 555-0123"
        },
        {
            "name": "Dr. Marcus Thorne",
            "npi": "1892039485",
            "clinic": "Sutter Cardiovascular Center",
            "rating": 4.2,
            "address": "5678 Health Blvd, Oakland, CA 94612",
            "phone": "(510) 555-0456"
        },
        {
            "name": "Dr. Jennifer Rodriguez",
            "npi": "1567234890",
            "clinic": "Pacific Heart Group",
            "rating": 4.7,
            "address": "9012 Cardio Way, San Jose, CA 95123",
            "phone": "(408) 555-0789"
        },
        {
            "name": "Dr. David Park",
            "npi": "1234567890",
            "clinic": "Golden Gate Cardiology",
            "rating": 4.8,
            "address": "2468 Cardiac Circle, Daly City, CA 94014",
            "phone": "(650) 555-0234"
        },
        {
            "name": "Dr. Lisa Martinez",
            "npi": "1345678901",
            "clinic": "Bay Area Heart Center",
            "rating": 4.6,
            "address": "1357 Rhythm Road, Fremont, CA 94536",
            "phone": "(510) 555-0567"
        }
    ],
    "dermatology": [
        {
            "name": "Dr. Sarah Lee",
            "npi": "1239048572",
            "clinic": "Bay Area Skin Health Institute",
            "rating": 4.8,
            "address": "3456 Derma Ave, Palo Alto, CA 94301",
            "phone": "(650) 555-0890"
        },
        {
            "name": "Dr. Kevin Patel",
            "npi": "1928374650",
            "clinic": "Valley Dermatology Associates",
            "rating": 4.5,
            "address": "7890 Skin Care Lane, Fremont, CA 94536",
            "phone": "(510) 555-0345"
        },
        {
            "name": "Dr. Michelle Williams",
            "npi": "1345678902",
            "clinic": "Advanced Dermatology Center",
            "rating": 4.6,
            "address": "2468 Beauty Blvd, Berkeley, CA 94704",
            "phone": "(510) 555-0678"
        },
        {
            "name": "Dr. Andrew Kim",
            "npi": "1456789013",
            "clinic": "Silicon Valley Skin Clinic",
            "rating": 4.4,
            "address": "3579 Complexion Court, Santa Clara, CA 95051",
            "phone": "(408) 555-0901"
        },
        {
            "name": "Dr. Rachel Thompson",
            "npi": "1567890124",
            "clinic": "Coastal Dermatology Group",
            "rating": 4.9,
            "address": "4680 Epidermis Way, Half Moon Bay, CA 94019",
            "phone": "(650) 555-0123"
        }
    ],
    "orthopedics": [
        {
            "name": "Dr. Brock Stone",
            "npi": "1122334455",
            "clinic": "Bay Joint & Spine Center",
            "rating": 4.7,
            "address": "1357 Bone Ave, San Mateo, CA 94403",
            "phone": "(650) 555-0456"
        },
        {
            "name": "Dr. Amanda Foster",
            "npi": "1987654321",
            "clinic": "Silicon Valley Orthopedics",
            "rating": 4.4,
            "address": "2468 Sports Medicine Dr, Santa Clara, CA 95051",
            "phone": "(408) 555-0789"
        },
        {
            "name": "Dr. Robert Kim",
            "npi": "1456789012",
            "clinic": "Peninsula Bone & Joint",
            "rating": 4.8,
            "address": "3691 Movement Way, Redwood City, CA 94063",
            "phone": "(650) 555-0234"
        },
        {
            "name": "Dr. Maria Gonzalez",
            "npi": "1678901235",
            "clinic": "Bay Area Ortho Associates",
            "rating": 4.5,
            "address": "4802 Skeletal Street, Hayward, CA 94541",
            "phone": "(510) 555-0567"
        },
        {
            "name": "Dr. James Wilson",
            "npi": "1789012346",
            "clinic": "Golden State Sports Medicine",
            "rating": 4.6,
            "address": "5913 Ligament Lane, San Rafael, CA 94901",
            "phone": "(415) 555-0890"
        }
    ],
    "pediatrics": [
        {
            "name": "Dr. Emma Johnson",
            "npi": "1890123457",
            "clinic": "Children's Health Bay Area",
            "rating": 4.9,
            "address": "1024 Rainbow Road, San Francisco, CA 94118",
            "phone": "(415) 555-0345"
        },
        {
            "name": "Dr. Michael Davis",
            "npi": "1901234568",
            "clinic": "Little Ones Pediatric Care",
            "rating": 4.7,
            "address": "2135 Playground Place, Oakland, CA 94610",
            "phone": "(510) 555-0678"
        },
        {
            "name": "Dr. Linda Chen",
            "npi": "1012345679",
            "clinic": "Sunshine Pediatrics",
            "rating": 4.8,
            "address": "3246 Teddy Bear Trail, Berkeley, CA 94705",
            "phone": "(510) 555-0901"
        },
        {
            "name": "Dr. Carlos Rodriguez",
            "npi": "1123456780",
            "clinic": "Happy Kids Medical Group",
            "rating": 4.5,
            "address": "4357 Lullaby Lane, San Jose, CA 95125",
            "phone": "(408) 555-0123"
        },
        {
            "name": "Dr. Jennifer Park",
            "npi": "1234567891",
            "clinic": "Growing Up Pediatric Center",
            "rating": 4.6,
            "address": "5468 Crayon Circle, Palo Alto, CA 94303",
            "phone": "(650) 555-0456"
        }
    ],
    "neurology": [
        {
            "name": "Dr. Alexandra Petrov",
            "npi": "1357924680",
            "clinic": "Bay Area Neurology Institute",
            "subspecialty": "Movement Disorders",
            "rating": 4.9,
            "address": "2400 Neurological Way, San Francisco, CA 94115",
            "phone": "(415) 555-0900",
            "years_experience": 18,
            "fellowship": "UCSF Movement Disorders Fellowship"
        },
        {
            "name": "Dr. Hassan Mohamed",
            "npi": "1468035791",
            "clinic": "Stanford Neurology Center",
            "subspecialty": "Epilepsy & Seizure Disorders",
            "rating": 4.8,
            "address": "3500 Brain Sciences Blvd, Palo Alto, CA 94304",
            "phone": "(650) 555-0800",
            "years_experience": 15,
            "fellowship": "Mayo Clinic Epilepsy Fellowship"
        },
        {
            "name": "Dr. Victoria Chang",
            "npi": "1579146802",
            "clinic": "Peninsula Neuroscience Group",
            "subspecialty": "Headache & Migraine",
            "rating": 4.7,
            "address": "4600 Synapse Street, Redwood City, CA 94063",
            "phone": "(650) 555-0700",
            "years_experience": 12,
            "fellowship": "Jefferson Headache Center Fellowship"
        },
        {
            "name": "Dr. Benjamin Torres",
            "npi": "1680257913",
            "clinic": "East Bay Neurology Associates",
            "subspecialty": "Stroke & Cerebrovascular Disease",
            "rating": 4.6,
            "address": "5700 Cortex Circle, Oakland, CA 94612",
            "phone": "(510) 555-0600",
            "years_experience": 20,
            "fellowship": "Johns Hopkins Stroke Fellowship"
        },
        {
            "name": "Dr. Rachel Kim-Singh",
            "npi": "1791369024",
            "clinic": "South Bay Comprehensive Neurology",
            "subspecialty": "Multiple Sclerosis & Demyelinating Disease",
            "rating": 4.8,
            "address": "6800 Myelin Drive, San Jose, CA 95123",
            "phone": "(408) 555-0500",
            "years_experience": 14,
            "fellowship": "Cleveland Clinic MS Fellowship"
        }
    ],
    "gastroenterology": [
        {
            "name": "Dr. Christopher Lee",
            "npi": "1802470135",
            "clinic": "Golden Gate Digestive Health",
            "subspecialty": "Inflammatory Bowel Disease",
            "rating": 4.9,
            "address": "7900 Digestive Lane, San Francisco, CA 94118",
            "phone": "(415) 555-0400",
            "years_experience": 16,
            "fellowship": "Mount Sinai IBD Fellowship"
        },
        {
            "name": "Dr. Priya Patel",
            "npi": "1913581246",
            "clinic": "Silicon Valley GI Center",
            "subspecialty": "Advanced Endoscopy",
            "rating": 4.7,
            "address": "8100 Endoscopy Way, Santa Clara, CA 95051",
            "phone": "(408) 555-0300",
            "years_experience": 13,
            "fellowship": "Mayo Clinic Advanced Endoscopy"
        },
        {
            "name": "Dr. Antonio Morales",
            "npi": "1024692357",
            "clinic": "Peninsula Gastroenterology Group",
            "subspecialty": "Hepatology & Liver Disease",
            "rating": 4.8,
            "address": "9200 Hepatic Avenue, Fremont, CA 94536",
            "phone": "(510) 555-0200",
            "years_experience": 19,
            "fellowship": "UCLA Hepatology Fellowship"
        },
        {
            "name": "Dr. Lisa Chen-Wong",
            "npi": "1135703468",
            "clinic": "Bay Area Motility Institute",
            "subspecialty": "GI Motility Disorders",
            "rating": 4.6,
            "address": "1030 Peristalsis Place, Berkeley, CA 94704",
            "phone": "(510) 555-0100",
            "years_experience": 11,
            "fellowship": "Northwestern Motility Fellowship"
        },
        {
            "name": "Dr. Samuel Rodriguez",
            "npi": "1246814579",
            "clinic": "Coastal Digestive Care",
            "subspecialty": "Pancreaticobiliary Disease",
            "rating": 4.7,
            "address": "1140 Pancreas Point, Half Moon Bay, CA 94019",
            "phone": "(650) 555-0050",
            "years_experience": 17,
            "fellowship": "Indiana University ERCP Fellowship"
        }
    ],
    "psychiatry": [
        {
            "name": "Dr. Amanda Foster-Gray",
            "npi": "1357925680",
            "clinic": "Bay Area Mental Health Institute",
            "subspecialty": "Adult Mood Disorders",
            "rating": 4.9,
            "address": "1250 Serenity Street, San Francisco, CA 94102",
            "phone": "(415) 555-0975",
            "years_experience": 22,
            "fellowship": "McLean Hospital Mood Disorders"
        },
        {
            "name": "Dr. Marcus Thompson",
            "npi": "1468036791",
            "clinic": "Peninsula Behavioral Health",
            "subspecialty": "Anxiety & Trauma Disorders",
            "rating": 4.8,
            "address": "1360 Mindfulness Way, Palo Alto, CA 94301",
            "phone": "(650) 555-0875",
            "years_experience": 18,
            "fellowship": "Emory PTSD Clinic Fellowship"
        },
        {
            "name": "Dr. Jennifer Liu-Martinez",
            "npi": "1579147802",
            "clinic": "East Bay Psychiatric Associates",
            "subspecialty": "Child & Adolescent Psychiatry",
            "rating": 4.7,
            "address": "1470 Youth Development Dr, Oakland, CA 94610",
            "phone": "(510) 555-0775",
            "years_experience": 15,
            "fellowship": "CHOP Child Psychiatry Fellowship"
        },
        {
            "name": "Dr. Robert Kim-Park",
            "npi": "1680258913",
            "clinic": "South Bay Mind & Wellness Center",
            "subspecialty": "Addiction Psychiatry",
            "rating": 4.6,
            "address": "1580 Recovery Road, San Jose, CA 95125",
            "phone": "(408) 555-0675",
            "years_experience": 14,
            "fellowship": "Yale Addiction Psychiatry"
        },
        {
            "name": "Dr. Catherine Wong",
            "npi": "1791370024",
            "clinic": "Mindful Health Solutions",
            "subspecialty": "Geriatric Psychiatry",
            "rating": 4.8,
            "address": "1690 Elder Care Circle, Daly City, CA 94014",
            "phone": "(650) 555-0575",
            "years_experience": 20,
            "fellowship": "Johns Hopkins Geriatric Psychiatry"
        }
    ]
}

# ==========================================
# 2. INSURANCE PLANS - Comprehensive coverage scenarios
# ==========================================

INSURANCE_PLANS = {
    "Blue Cross": {
        "covered_specialties": ["cardiology", "dermatology", "orthopedics", "pediatrics", "general"],
        "copay": "$25.00",
        "deductible": "$500",
        "network": "Preferred Provider Network",
        "plan_type": "Comprehensive PPO"
    },
    "Kaiser": {
        "covered_specialties": ["general", "pediatrics"],  # Kaiser is restrictive for specialists
        "copay": "$15.00",
        "deductible": "$0",
        "network": "HMO Network Only",
        "plan_type": "HMO"
    },
    "Medi-Cal": {
        "covered_specialties": ["cardiology", "orthopedics", "pediatrics", "general"],
        "copay": "$0.00",
        "deductible": "$0",
        "network": "State Approved Providers",
        "plan_type": "Government Insurance"
    },
    "High Deductible Plan": {
        "covered_specialties": ["general", "pediatrics"],  # Restrictive new plan
        "copay": "$100.00",
        "deductible": "$3000",
        "network": "Limited Provider Network",
        "plan_type": "High Deductible Health Plan (HDHP)"
    },
    "Aetna Premium": {
        "covered_specialties": ["cardiology", "dermatology", "orthopedics", "pediatrics", "general"],
        "copay": "$35.00",
        "deductible": "$750",
        "network": "National Provider Network",
        "plan_type": "Premium PPO"
    },
    "UnitedHealth Premium": {
        "covered_specialties": ["cardiology", "dermatology", "orthopedics", "pediatrics", "neurology", "gastroenterology", "psychiatry", "general"],
        "copay": "$40.00",
        "deductible": "$1000",
        "network": "National Preferred Network",
        "plan_type": "Premium PPO",
        "prior_auth_required": ["neurology", "gastroenterology", "psychiatry"],
        "annual_max": "$2,000,000"
    },
    "Cigna Select": {
        "covered_specialties": ["cardiology", "orthopedics", "pediatrics", "general"],
        "copay": "$30.00", 
        "deductible": "$500",
        "network": "Select Provider Network",
        "plan_type": "Select PPO",
        "prior_auth_required": ["cardiology"],
        "annual_max": "$1,000,000"
    },
    "Health Net Basic": {
        "covered_specialties": ["general", "pediatrics"],
        "copay": "$50.00",
        "deductible": "$2500",
        "network": "Basic Provider Network", 
        "plan_type": "Basic HMO",
        "prior_auth_required": ["pediatrics"],
        "annual_max": "$500,000"
    }
}

# ==========================================
# 3. PROCEDURE CODES (CPT) - 3 Realistic codes per specialty
# ==========================================

PROCEDURE_CODES = {
    "cardiology": [
        {"code": "99203", "description": "New patient office visit (detailed)", "cost": "$275"},
        {"code": "93000", "description": "Electrocardiogram (ECG/EKG)", "cost": "$125"},
        {"code": "93307", "description": "Echocardiography transthoracic", "cost": "$650"}
    ],
    "dermatology": [
        {"code": "99213", "description": "Established patient office visit", "cost": "$185"},
        {"code": "11100", "description": "Biopsy of skin lesion", "cost": "$295"},
        {"code": "17000", "description": "Destruction of skin lesion (cryotherapy)", "cost": "$225"}
    ],
    "orthopedics": [
        {"code": "99243", "description": "Office consultation orthopedic evaluation", "cost": "$320"},
        {"code": "73060", "description": "Radiologic examination, knee 2 views", "cost": "$145"},
        {"code": "20610", "description": "Arthrocentesis (joint injection)", "cost": "$285"}
    ],
    "pediatrics": [
        {"code": "99213", "description": "Pediatric office visit (established patient)", "cost": "$165"},
        {"code": "99391", "description": "Preventive medicine visit (well child)", "cost": "$195"},
        {"code": "90715", "description": "Pediatric vaccination administration", "cost": "$85"}
    ],
    "general": [
        {"code": "99213", "description": "Office visit established patient", "cost": "$175"},
        {"code": "99214", "description": "Office visit established patient (detailed)", "cost": "$235"},
        {"code": "99215", "description": "Office visit established patient (comprehensive)", "cost": "$295"}
    ],
    "default": [
        {"code": "99499", "description": "Unlisted evaluation and management service", "cost": "$300"},
        {"code": "99213", "description": "Office or other outpatient visit", "cost": "$200"},
        {"code": "99214", "description": "Office or other outpatient visit (detailed)", "cost": "$250"}
    ],
    "neurology": [
        {"code": "99204", "description": "New patient neurology consultation", "cost": "$425"},
        {"code": "95860", "description": "Needle electromyography (EMG)", "cost": "$385"},
        {"code": "95941", "description": "Continuous EEG monitoring", "cost": "$750"},
        {"code": "70553", "description": "Brain MRI with contrast", "cost": "$1250"},
        {"code": "64483", "description": "Injection, anesthetic agent; lumbar facet joint", "cost": "$495"}
    ],
    "gastroenterology": [
        {"code": "99204", "description": "New patient GI consultation", "cost": "$385"},
        {"code": "45380", "description": "Colonoscopy with biopsy", "cost": "$1125"},
        {"code": "43239", "description": "Upper endoscopy with biopsy", "cost": "$875"},
        {"code": "47562", "description": "Laparoscopic cholecystectomy", "cost": "$3250"},
        {"code": "76705", "description": "Abdominal ultrasound", "cost": "$325"}
    ],
    "psychiatry": [
        {"code": "99204", "description": "Initial psychiatric evaluation", "cost": "$350"},
        {"code": "99214", "description": "Psychotherapy session (45 min)", "cost": "$185"},
        {"code": "90834", "description": "Individual psychotherapy (45 min)", "cost": "$165"},
        {"code": "90837", "description": "Individual psychotherapy (60 min)", "cost": "$225"},
        {"code": "96116", "description": "Neurobehavioral status exam", "cost": "$285"}
    ]
}

# ==========================================
# 4. DIAGNOSIS CODES (ICD-10) - 3 Common codes per specialty
# ==========================================

DIAGNOSIS_CODES = {
    "cardiology": [
        {"code": "I25.10", "description": "Atherosclerotic heart disease of native coronary artery"},
        {"code": "I50.9", "description": "Heart failure, unspecified"},
        {"code": "I20.9", "description": "Angina pectoris, unspecified"}
    ],
    "dermatology": [
        {"code": "L30.9", "description": "Dermatitis, unspecified"},
        {"code": "L70.0", "description": "Acne vulgaris"},
        {"code": "L40.9", "description": "Psoriasis, unspecified"}
    ],
    "orthopedics": [
        {"code": "M25.561", "description": "Pain in right knee"},
        {"code": "M54.5", "description": "Low back pain"},
        {"code": "M75.30", "description": "Calcific tendinitis of shoulder, unspecified"}
    ],
    "pediatrics": [
        {"code": "Z00.121", "description": "Encounter for routine child health examination with abnormal findings"},
        {"code": "J06.9", "description": "Acute upper respiratory infection, unspecified"},
        {"code": "K59.00", "description": "Constipation, unspecified"}
    ],
    "general": [
        {"code": "Z00.00", "description": "Encounter for general adult medical examination without abnormal findings"},
        {"code": "R06.02", "description": "Shortness of breath"},
        {"code": "R50.9", "description": "Fever, unspecified"}
    ],
    "default": [
        {"code": "R69", "description": "Illness, unspecified"},
        {"code": "Z00.00", "description": "Encounter for general adult medical examination"},
        {"code": "R06.02", "description": "Shortness of breath"}
    ],
    "neurology": [
        {"code": "G93.1", "description": "Anoxic brain damage, not elsewhere classified"},
        {"code": "G40.909", "description": "Epilepsy, unspecified, not intractable, without status epilepticus"},
        {"code": "G43.909", "description": "Migraine, unspecified, not intractable, without status migrainosus"},
        {"code": "G35", "description": "Multiple sclerosis"},
        {"code": "G20", "description": "Parkinson's disease"}
    ],
    "gastroenterology": [
        {"code": "K50.90", "description": "Crohn's disease, unspecified, without complications"},
        {"code": "K51.90", "description": "Ulcerative colitis, unspecified, without complications"},
        {"code": "K21.9", "description": "Gastro-esophageal reflux disease without esophagitis"},
        {"code": "K80.20", "description": "Calculus of gallbladder without cholecystitis without obstruction"},
        {"code": "K70.30", "description": "Alcoholic cirrhosis of liver without ascites"}
    ],
    "psychiatry": [
        {"code": "F32.9", "description": "Major depressive disorder, single episode, unspecified"},
        {"code": "F41.1", "description": "Generalized anxiety disorder"},
        {"code": "F43.10", "description": "Post-traumatic stress disorder, unspecified"},
        {"code": "F84.0", "description": "Autistic disorder"},
        {"code": "F20.9", "description": "Schizophrenia, unspecified"}
    ]
}

# ==========================================
# 5. PATIENT DATABASE - 5 Diverse patients for testing
# ==========================================

PATIENTS = [
    {
        "name": "John Smith",
        "dob": "03/15/1975",
        "age": "48",
        "sex": "Male",
        "insurance_plan": "Blue Cross",
        "member_id": "BC123456789",
        "phone": "(415) 555-0001",
        "address": "123 Market St, San Francisco, CA 94102"
    },
    {
        "name": "Sarah Johnson", 
        "dob": "07/22/1988",
        "age": "35",
        "sex": "Female",
        "insurance_plan": "Kaiser",
        "member_id": "KP987654321",
        "phone": "(510) 555-0002",
        "address": "456 Oak Ave, Oakland, CA 94610"
    },
    {
        "name": "Michael Brown",
        "dob": "11/08/1965",
        "age": "58",
        "sex": "Male", 
        "insurance_plan": "Medi-Cal",
        "member_id": "MC555123456",
        "phone": "(408) 555-0003",
        "address": "789 Pine St, San Jose, CA 95112"
    },
    {
        "name": "Emily Davis",
        "dob": "05/14/1992",
        "age": "31",
        "sex": "Female",
        "insurance_plan": "High Deductible Plan",
        "member_id": "HDP789456123",
        "phone": "(650) 555-0004", 
        "address": "321 Elm Dr, Palo Alto, CA 94301"
    },
    {
        "name": "Robert Wilson",
        "dob": "09/30/1980",
        "age": "43",
        "sex": "Male",
        "insurance_plan": "Aetna Premium",
        "member_id": "AET456789012",
        "phone": "(415) 555-0005",
        "address": "654 Cedar Ln, Daly City, CA 94014"
    }
]

# ==========================================
# 12. ENHANCED PATIENT DATABASE - More diverse patients with clinical history
# ==========================================

# Adding more patients with detailed medical histories
ADDITIONAL_PATIENTS = [
    {
        "name": "Maria Gonzalez-Lopez",
        "dob": "12/03/1967",
        "age": "56",
        "sex": "Female",
        "insurance_plan": "UnitedHealth Premium",
        "member_id": "UHP789012345",
        "phone": "(408) 555-0006",
        "address": "987 Mission St, San Jose, CA 95112",
        "primary_language": "Spanish",
        "medical_history": ["Diabetes Type 2", "Hypertension", "Hyperlipidemia"],
        "allergies": ["Penicillin", "Shellfish"],
        "emergency_contact": "Carlos Gonzalez (Husband) - (408) 555-0007"
    },
    {
        "name": "David Kim-Chen",
        "dob": "04/18/1985",
        "age": "38",
        "sex": "Male",  
        "insurance_plan": "Cigna Select",
        "member_id": "CGN234567890",
        "phone": "(650) 555-0008",
        "address": "456 University Ave, Palo Alto, CA 94301",
        "primary_language": "English",
        "medical_history": ["Asthma", "Seasonal Allergies"],
        "allergies": ["Sulfa drugs"],
        "emergency_contact": "Jennifer Chen (Wife) - (650) 555-0009"
    },
    {
        "name": "Jennifer Washington",
        "dob": "08/25/1993",
        "age": "30",
        "sex": "Female",
        "insurance_plan": "Health Net Basic", 
        "member_id": "HNB345678901",
        "phone": "(510) 555-0010",
        "address": "123 Broadway, Oakland, CA 94607",
        "primary_language": "English",
        "medical_history": ["Depression", "Anxiety"],
        "allergies": ["NKDA"],
        "emergency_contact": "Marcus Washington (Brother) - (510) 555-0011"
    },
    {
        "name": "Ahmed Hassan",
        "dob": "06/12/1978",
        "age": "45",
        "sex": "Male",
        "insurance_plan": "Blue Cross",
        "member_id": "BC456789012",
        "phone": "(415) 555-0012", 
        "address": "789 Geary Blvd, San Francisco, CA 94118",
        "primary_language": "Arabic",
        "medical_history": ["Chronic Back Pain", "Sleep Apnea"],
        "allergies": ["Codeine"],
        "emergency_contact": "Fatima Hassan (Wife) - (415) 555-0013"
    },
    {
        "name": "Lisa Thompson-Park",
        "dob": "10/07/1972",
        "age": "51",
        "sex": "Female",
        "insurance_plan": "Aetna Premium",
        "member_id": "AET567890123",
        "phone": "(650) 555-0014",
        "address": "321 Forest Ave, Redwood City, CA 94063",  
        "primary_language": "English",
        "medical_history": ["Breast Cancer Survivor", "Osteoporosis"],
        "allergies": ["Latex", "Iodine"],
        "emergency_contact": "James Park (Husband) - (650) 555-0015"
    }
]

# Combine all patients into a single list for the system to use
PATIENTS.extend(ADDITIONAL_PATIENTS)

# ==========================================
# 13. CLINICAL URGENCY LEVELS - For triage and scheduling priority
# ==========================================

URGENCY_LEVELS = {
    "STAT": {
        "description": "Immediate attention required",
        "timeframe": "Within 24 hours",
        "examples": ["Chest pain", "Stroke symptoms", "Severe bleeding"]
    },
    "URGENT": {
        "description": "Urgent but not life-threatening",
        "timeframe": "Within 72 hours", 
        "examples": ["Severe pain", "High fever", "Difficulty breathing"]
    },
    "ROUTINE": {
        "description": "Standard scheduling priority",
        "timeframe": "Within 2-4 weeks",
        "examples": ["Follow-up visits", "Preventive care", "Chronic condition management"]
    },
    "ELECTIVE": {
        "description": "Non-urgent, patient preference timing",
        "timeframe": "Within 1-3 months",
        "examples": ["Cosmetic procedures", "Routine screenings", "Second opinions"]
    }
}

# ==========================================
# 14. ENHANCED COVERAGE MATRIX - Complete specialty coverage lookup
# ==========================================

# Updated coverage matrix with all new specialties and insurance plans
COVERAGE_MATRIX = {
    "Blue Cross": ["cardiology", "dermatology", "orthopedics", "pediatrics", "neurology", "gastroenterology", "psychiatry"],
    "Kaiser": ["pediatrics"],  # Shows restrictive coverage
    "Medi-Cal": ["cardiology", "orthopedics", "pediatrics"],
    "High Deductible Plan": ["pediatrics"],  # Very restrictive
    "Aetna Premium": ["cardiology", "dermatology", "orthopedics", "pediatrics", "neurology", "gastroenterology", "psychiatry"],
    "UnitedHealth Premium": ["cardiology", "dermatology", "orthopedics", "pediatrics", "neurology", "gastroenterology", "psychiatry"],
    "Cigna Select": ["cardiology", "orthopedics", "pediatrics"],
    "Health Net Basic": ["pediatrics"]
}

# ==========================================
# 15. APPOINTMENT SCHEDULING SLOTS - Realistic availability
# ==========================================

APPOINTMENT_AVAILABILITY = {
    "cardiology": {
        "next_available": "2025-02-15",
        "typical_wait": "3-4 weeks",
        "urgent_slots": "2025-01-30"
    },
    "dermatology": {
        "next_available": "2025-03-01", 
        "typical_wait": "6-8 weeks",
        "urgent_slots": "2025-02-10"
    },
    "orthopedics": {
        "next_available": "2025-02-20",
        "typical_wait": "4-5 weeks", 
        "urgent_slots": "2025-02-05"
    },
    "pediatrics": {
        "next_available": "2025-01-25",
        "typical_wait": "1-2 weeks",
        "urgent_slots": "2025-01-22"
    },
    "neurology": {
        "next_available": "2025-03-15",
        "typical_wait": "8-10 weeks",
        "urgent_slots": "2025-02-15"
    },
    "gastroenterology": {
        "next_available": "2025-03-10",
        "typical_wait": "6-8 weeks",
        "urgent_slots": "2025-02-20"
    },
    "psychiatry": {
        "next_available": "2025-04-01",
        "typical_wait": "10-12 weeks", 
        "urgent_slots": "2025-03-01"
    }
}

# ==========================================
# 16. ENHANCED DEMO SCENARIOS - Complete test matrix for hackathon
# ==========================================

DEMO_SCENARIOS = [
    {
        "name": "Successful Cardiology Referral",
        "patient": "John Smith",
        "specialty": "cardiology",
        "expected_outcome": "IN-NETWORK",
        "copay": "$25.00",
        "urgency": "ROUTINE",
        "notes": "Standard cardiac evaluation"
    },
    {
        "name": "Failed Dermatology Coverage",
        "patient": "Sarah Johnson", 
        "specialty": "dermatology",
        "expected_outcome": "OUT-OF-NETWORK",
        "copay": "100% Patient Responsibility",
        "urgency": "ROUTINE",
        "notes": "Kaiser HMO does not cover dermatology specialists"
    },
    {
        "name": "High Deductible Pediatrics",
        "patient": "Emily Davis",
        "specialty": "pediatrics", 
        "expected_outcome": "IN-NETWORK",
        "copay": "$100.00",
        "urgency": "ROUTINE",
        "notes": "High deductible plan with expensive copays"
    },
    {
        "name": "Medi-Cal Orthopedics Success",
        "patient": "Michael Brown",
        "specialty": "orthopedics",
        "expected_outcome": "IN-NETWORK", 
        "copay": "$0.00",
        "urgency": "URGENT",
        "notes": "Government insurance with full coverage"
    },
    {
        "name": "Premium Plan Full Coverage",
        "patient": "Robert Wilson",
        "specialty": "dermatology",
        "expected_outcome": "IN-NETWORK",
        "copay": "$35.00",
        "urgency": "ROUTINE",
        "notes": "Premium plan with comprehensive coverage"
    },
    {
        "name": "Neurology - Premium Coverage Success",
        "patient": "Maria Gonzalez-Lopez",
        "specialty": "neurology",
        "expected_outcome": "IN-NETWORK", 
        "copay": "$40.00",
        "urgency": "URGENT",
        "notes": "Migraine specialist referral with prior authorization"
    },
    {
        "name": "Gastroenterology - Coverage Denied",
        "patient": "Jennifer Washington",
        "specialty": "gastroenterology", 
        "expected_outcome": "OUT-OF-NETWORK",
        "copay": "100% Patient Responsibility",
        "urgency": "ROUTINE",
        "notes": "Basic plan does not cover GI specialists"
    },
    {
        "name": "Psychiatry - Mental Health Coverage",
        "patient": "David Kim-Chen",
        "specialty": "psychiatry",
        "expected_outcome": "OUT-OF-NETWORK",
        "copay": "100% Patient Responsibility", 
        "urgency": "ROUTINE",
        "notes": "Select plan excludes mental health specialists"
    },
    {
        "name": "Orthopedics - Chronic Pain Management",
        "patient": "Ahmed Hassan",
        "specialty": "orthopedics",
        "expected_outcome": "IN-NETWORK",
        "copay": "$25.00",
        "urgency": "URGENT", 
        "notes": "Back pain specialist for chronic condition"
    },
    {
        "name": "Dermatology - Cancer Survivor Follow-up",
        "patient": "Lisa Thompson-Park", 
        "specialty": "dermatology",
        "expected_outcome": "IN-NETWORK",
        "copay": "$35.00",
        "urgency": "ROUTINE",
        "notes": "Skin cancer screening for breast cancer survivor"
    }
]

# AI-generated code section ends