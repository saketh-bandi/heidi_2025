# openemr_connector.py
# AI-generated code section begins - GitHub Copilot assisted with OpenEMR database integration

"""
OpenEMR Database Connector
Provides functions to fetch patient data and Heidi sessions from OpenEMR MySQL database
"""

import mysql.connector
from datetime import datetime, date
from typing import Optional, Dict, Any

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'openemr',
    'password': 'CHANGE_ME',
    'database': 'openemr'
}

# Insurance provider mapping: OpenEMR provider name → mock_db.py insurance plan name
INSURANCE_MAPPING = {
    'Kaiser Permanente': 'Kaiser',
    'Blue Cross Blue Shield': 'Blue Cross',
    'Blue Cross': 'Blue Cross',
    'Aetna': 'Aetna Premium',
    'UnitedHealth': 'UnitedHealth Premium',
    'UnitedHealthcare': 'UnitedHealth Premium',
    'Cigna': 'Cigna Select',
    'Health Net': 'Health Net Basic',
    'Medi-Cal': 'Medi-Cal',
    'Medicaid': 'Medi-Cal'
}

def get_db_connection():
    """
    Establish connection to OpenEMR MySQL database
    
    Returns:
        mysql.connector.connection.MySQLConnection: Database connection object
        None: If connection fails
    """
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        print(f"✅ Database connected: {DB_CONFIG['database']}@{DB_CONFIG['host']}")
        return connection
    except mysql.connector.Error as err:
        print(f"❌ Database connection error: {err}")
        return None

def map_insurance_provider(openemr_provider: str) -> str:
    """
    Map OpenEMR insurance provider name to mock_db.py insurance plan name
    
    Args:
        openemr_provider: Provider name from OpenEMR insurance_data table
    
    Returns:
        str: Mapped insurance plan name for mock_db.py
    """
    if not openemr_provider:
        return "High Deductible Plan"  # Default fallback
    
    # Try exact match first
    if openemr_provider in INSURANCE_MAPPING:
        return INSURANCE_MAPPING[openemr_provider]
    
    # Try partial match (case-insensitive)
    provider_lower = openemr_provider.lower()
    for openemr_name, mock_name in INSURANCE_MAPPING.items():
        if openemr_name.lower() in provider_lower or provider_lower in openemr_name.lower():
            return mock_name
    
    # Fallback: Use provider name as-is
    print(f"⚠️  Unknown insurance provider '{openemr_provider}', using as-is")
    return openemr_provider

def calculate_age(birth_date: date) -> int:
    """
    Calculate age from birth date
    
    Args:
        birth_date: Date of birth
    
    Returns:
        int: Age in years
    """
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def fetch_patient_data(pid: int) -> Optional[Dict[str, Any]]:
    """
    Fetch patient demographic and insurance data from OpenEMR database
    
    Args:
        pid: Patient ID
    
    Returns:
        dict: Patient data in format compatible with router.py
        {
            "name": "Emily Brown",
            "dob": "02/14/1995",
            "age": "30",
            "sex": "Female",
            "address": "987 Cedar Lane, Long Beach, CA",
            "phone": "(562) 555-2346",
            "insurance_plan": "Kaiser",
            "member_id": "POL00000006",
            "occupation": "Teacher"
        }
        None: If patient not found or error occurs
    """
    connection = get_db_connection()
    if not connection:
        return None
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        # Query patient data with insurance information (LEFT JOIN to handle patients without insurance)
        query = """
            SELECT 
                p.pid,
                p.fname,
                p.lname,
                p.DOB,
                p.sex,
                p.street,
                p.city,
                p.state,
                p.phone_cell,
                p.occupation,
                i.provider AS insurance_provider,
                i.plan_name,
                i.policy_number
            FROM patient_data p
            LEFT JOIN insurance_data i ON p.pid = i.pid AND i.type = 'primary'
            WHERE p.pid = %s
        """
        
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        
        if not result:
            print(f"❌ Patient not found: PID {pid}")
            return None
        
        # Format address
        address = f"{result['street']}, {result['city']}, {result['state']}"
        
        # Calculate age from DOB
        age = calculate_age(result['DOB']) if result['DOB'] else "Unknown"
        
        # Format DOB as MM/DD/YYYY
        dob_formatted = result['DOB'].strftime("%m/%d/%Y") if result['DOB'] else "Unknown"
        
        # Map insurance provider
        insurance_plan = map_insurance_provider(result['insurance_provider'])
        
        # Format patient data
        patient_data = {
            "name": f"{result['fname']} {result['lname']}",
            "dob": dob_formatted,
            "age": str(age),
            "sex": result['sex'] or "Unknown",
            "address": address,
            "phone": result['phone_cell'] or "Unknown",
            "insurance_plan": insurance_plan,
            "member_id": result['policy_number'] or "Unknown",
            "occupation": result['occupation'] or "Unknown",
            "pid": result['pid']
        }
        
        print(f"✅ Patient data fetched: {patient_data['name']} (PID {pid})")
        return patient_data
        
    except mysql.connector.Error as err:
        print(f"❌ Database error fetching patient {pid}: {err}")
        return None
    finally:
        cursor.close()
        connection.close()

def fetch_heidi_session(session_id: int) -> Optional[Dict[str, Any]]:
    """
    Fetch Heidi session data from OpenEMR database
    
    Args:
        session_id: Heidi session ID
    
    Returns:
        dict: Session data
        {
            "id": 101,
            "pid": 6,
            "transcript": "Patient presents with...",
            "consult_note": "AI clinical note...",
            "session_name": "Chest Pain Consultation",
            "duration": 930,  # seconds
            "session_date": "2024-01-15 14:30:00"
        }
        None: If session not found or error occurs
    """
    connection = get_db_connection()
    if not connection:
        return None
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        query = """
            SELECT 
                id,
                pid,
                heidi_session_id,
                transcript,
                consult_note,
                consult_note_heading,
                session_name,
                duration,
                session_date
            FROM heidi_sessions
            WHERE id = %s
        """
        
        cursor.execute(query, (session_id,))
        result = cursor.fetchone()
        
        if not result:
            print(f"❌ Heidi session not found: ID {session_id}")
            return None
        
        # Format session data
        session_data = {
            "id": result['id'],
            "pid": result['pid'],
            "heidi_session_id": result['heidi_session_id'],
            "transcript": result['transcript'] or "",
            "consult_note": result['consult_note'] or "",
            "consult_note_heading": result['consult_note_heading'] or "",
            "session_name": result['session_name'] or "Untitled Session",
            "duration": result['duration'] or 0,
            "session_date": result['session_date'].strftime("%Y-%m-%d %H:%M:%S") if result['session_date'] else "Unknown"
        }
        
        print(f"✅ Heidi session fetched: {session_data['session_name']} (ID {session_id}, PID {result['pid']})")
        return session_data
        
    except mysql.connector.Error as err:
        print(f"❌ Database error fetching session {session_id}: {err}")
        return None
    finally:
        cursor.close()
        connection.close()

def test_connection():
    """
    Test database connection and print connection status
    """
    print("🧪 Testing OpenEMR database connection...")
    connection = get_db_connection()
    if connection:
        print("✅ Connection test successful!")
        connection.close()
        return True
    else:
        print("❌ Connection test failed!")
        return False

# AI-generated code section ends

if __name__ == "__main__":
    # Test the connector
    print("=" * 60)
    print("🏥 OpenEMR Database Connector - Test Mode")
    print("=" * 60)
    
    # Test connection
    if not test_connection():
        print("\n❌ Database connection failed. Check your MySQL configuration.")
        exit(1)
    
    print("\n" + "=" * 60)
    print("Testing patient data fetch...")
    print("=" * 60)
    
    # Test fetching patient data (PID 6 - Emily Brown)
    patient = fetch_patient_data(6)
    if patient:
        print("\n📋 Patient Data:")
        for key, value in patient.items():
            print(f"   {key}: {value}")
    
    print("\n" + "=" * 60)
    print("Testing Heidi session fetch...")
    print("=" * 60)
    
    # Test fetching Heidi session (need to get a valid session ID first)
    from mysql.connector import connect
    conn = connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM heidi_sessions WHERE pid = 6 LIMIT 1")
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if result:
        session_id = result[0]
        session = fetch_heidi_session(session_id)
        if session:
            print(f"\n📝 Heidi Session Data:")
            print(f"   ID: {session['id']}")
            print(f"   Session Name: {session['session_name']}")
            print(f"   Patient ID: {session['pid']}")
            print(f"   Session Date: {session['session_date']}")
            print(f"   Duration: {session['duration']} seconds")
            print(f"   Transcript Length: {len(session['transcript'])} characters")
            print(f"   Consult Note Length: {len(session['consult_note'])} characters")
    else:
        print("⚠️  No Heidi sessions found for PID 6")
    
    print("\n" + "=" * 60)
    print("✅ Connector test complete!")
    print("=" * 60)
