#!/usr/bin/env php
<?php
/**
 * AI-generated code - Script to populate OpenEMR with mock patient data
 * This script directly inserts mock patients into the database
 */

// Bootstrap OpenEMR
$_GET['site'] = 'default';
$ignoreAuth = true;

// Bootstrap globals  
require_once __DIR__ . '/interface/globals.php';

echo "🏥 OpenEMR Mock Data Population Script\n";
echo "=====================================\n\n";

// Mock patient data
$mock_patients = [
    [
        'fname' => 'John',
        'lname' => 'Smith',
        'DOB' => '1980-05-15',
        'sex' => 'Male',
        'street' => '123 Main St',
        'city' => 'Los Angeles',
        'state' => 'CA',
        'postal_code' => '90210',
        'phone_home' => '(310) 555-1234',
        'email' => 'john.smith@example.com',
        'ss' => '123-45-6789',
        'pubpid' => 'test-fixture-001'
    ],
    [
        'fname' => 'Jane',
        'lname' => 'Doe',
        'DOB' => '1992-08-22',
        'sex' => 'Female',
        'street' => '456 Oak Avenue',
        'city' => 'Beverly Hills',
        'state' => 'CA',
        'postal_code' => '90210',
        'phone_home' => '(310) 555-5678',
        'email' => 'jane.doe@example.com',
        'ss' => '234-56-7890',
        'pubpid' => 'test-fixture-002'
    ],
    [
        'fname' => 'Robert',
        'lname' => 'Johnson',
        'DOB' => '1975-03-10',
        'sex' => 'Male',
        'street' => '789 Pine Road',
        'city' => 'Santa Monica',
        'state' => 'CA',
        'postal_code' => '90405',
        'phone_home' => '(310) 555-9012',
        'email' => 'robert.johnson@example.com',
        'ss' => '345-67-8901',
        'pubpid' => 'test-fixture-003'
    ],
    [
        'fname' => 'Maria',
        'lname' => 'Garcia',
        'DOB' => '1988-11-30',
        'sex' => 'Female',
        'street' => '321 Elm Street',
        'city' => 'Pasadena',
        'state' => 'CA',
        'postal_code' => '91101',
        'phone_home' => '(626) 555-3456',
        'email' => 'maria.garcia@example.com',
        'ss' => '456-78-9012',
        'pubpid' => 'test-fixture-004'
    ],
    [
        'fname' => 'Michael',
        'lname' => 'Williams',
        'DOB' => '1965-07-18',
        'sex' => 'Male',
        'street' => '654 Maple Drive',
        'city' => 'Glendale',
        'state' => 'CA',
        'postal_code' => '91201',
        'phone_home' => '(818) 555-7890',
        'email' => 'michael.williams@example.com',
        'ss' => '567-89-0123',
        'pubpid' => 'test-fixture-005'
    ],
    [
        'fname' => 'Emily',
        'lname' => 'Brown',
        'DOB' => '1995-02-14',
        'sex' => 'Female',
        'street' => '987 Cedar Lane',
        'city' => 'Long Beach',
        'state' => 'CA',
        'postal_code' => '90802',
        'phone_home' => '(562) 555-2345',
        'email' => 'emily.brown@example.com',
        'ss' => '678-90-1234',
        'pubpid' => 'test-fixture-006'
    ],
    [
        'fname' => 'David',
        'lname' => 'Martinez',
        'DOB' => '1970-09-25',
        'sex' => 'Male',
        'street' => '246 Birch Court',
        'city' => 'Burbank',
        'state' => 'CA',
        'postal_code' => '91502',
        'phone_home' => '(818) 555-6789',
        'email' => 'david.martinez@example.com',
        'ss' => '789-01-2345',
        'pubpid' => 'test-fixture-007'
    ],
    [
        'fname' => 'Sarah',
        'lname' => 'Davis',
        'DOB' => '1983-12-05',
        'sex' => 'Female',
        'street' => '135 Willow Way',
        'city' => 'Torrance',
        'state' => 'CA',
        'postal_code' => '90503',
        'phone_home' => '(310) 555-0123',
        'email' => 'sarah.davis@example.com',
        'ss' => '890-12-3456',
        'pubpid' => 'test-fixture-008'
    ]
];

echo "📝 Creating mock patients...\n\n";

$count = 0;
foreach ($mock_patients as $patient) {
    try {
        // Get next PID
        $pidQuery = "SELECT IFNULL(MAX(pid), 0) + 1 AS next_pid FROM patient_data";
        $pidResult = sqlQuery($pidQuery);
        $pid = $pidResult['next_pid'];
        
        // Generate UUID
        $uuid = \OpenEMR\Common\Uuid\UuidRegistry::uuidToString(
            (new \OpenEMR\Common\Uuid\UuidRegistry(['table_name' => 'patient_data']))->createUuid()
        );
        
        // Insert patient
        $sql = "INSERT INTO patient_data (pid, uuid, pubpid, fname, lname, DOB, sex, street, city, state, postal_code, phone_home, email, ss, date) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NOW())";
        
        sqlStatement($sql, [
            $pid,
            $uuid,
            $patient['pubpid'],
            $patient['fname'],
            $patient['lname'],
            $patient['DOB'],
            $patient['sex'],
            $patient['street'],
            $patient['city'],
            $patient['state'],
            $patient['postal_code'],
            $patient['phone_home'],
            $patient['email'],
            $patient['ss']
        ]);
        
        $count++;
        echo sprintf(
            "✅ %d. %s %s (ID: %s, PID: %d)\n" .
            "   DOB: %s | Sex: %s\n" .
            "   Location: %s, %s %s\n\n",
            $count,
            $patient['fname'],
            $patient['lname'],
            $patient['pubpid'],
            $pid,
            $patient['DOB'],
            $patient['sex'],
            $patient['city'],
            $patient['state'],
            $patient['postal_code']
        );
        
    } catch (Exception $e) {
        echo "❌ Error creating patient {$patient['fname']} {$patient['lname']}: " . $e->getMessage() . "\n\n";
    }
}

echo "\n✨ Success! Mock data has been populated.\n";
echo "📊 Total patients created: $count\n";
echo "\n💡 You can now log in to OpenEMR and view these patients.\n";
echo "🔐 Login at: http://localhost:8000\n";
echo "👤 Username: QQN-admin-14\n";
