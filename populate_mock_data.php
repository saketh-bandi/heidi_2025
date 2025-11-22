#!/usr/bin/env php
<?php
/**
 * AI-generated code - Script to populate OpenEMR with mock patient data
 * This script uses OpenEMR's fixture manager to install test patients
 */

// Bootstrap OpenEMR
require_once __DIR__ . '/vendor/autoload.php';

use OpenEMR\Tests\Fixtures\FixtureManager;
use OpenEMR\Common\Database\QueryUtils;

// Set up the environment
$_GET['site'] = 'default';
$ignoreAuth = true;

// Bootstrap globals
require_once __DIR__ . '/interface/globals.php';

echo "🏥 OpenEMR Mock Data Population Script\n";
echo "=====================================\n\n";

try {
    $fixtureManager = new FixtureManager();
    
    echo "📝 Installing patient fixtures...\n";
    $patientCount = $fixtureManager->installPatientFixtures();
    echo "✅ Installed $patientCount patient records\n\n";
    
    echo "📋 Installed Patients:\n";
    echo "-------------------\n";
    
    // Query the installed patients
    $sql = "SELECT pid, pubpid, fname, lname, DOB, sex, city, state, postal_code 
            FROM patient_data 
            WHERE pubpid LIKE 'test-fixture%' 
            ORDER BY pid 
            LIMIT 20";
    
    $result = sqlStatement($sql);
    $count = 0;
    
    while ($row = sqlFetchArray($result)) {
        $count++;
        echo sprintf(
            "%d. %s %s (ID: %s)\n" .
            "   DOB: %s | Sex: %s\n" .
            "   Location: %s, %s %s\n\n",
            $count,
            $row['fname'],
            $row['lname'],
            $row['pubpid'],
            $row['DOB'],
            $row['sex'],
            $row['city'],
            $row['state'],
            $row['postal_code']
        );
    }
    
    echo "\n✨ Success! Mock data has been populated.\n";
    echo "📊 Total patients installed: $count\n";
    echo "\n💡 You can now log in to OpenEMR and view these patients.\n";
    echo "🔐 Login at: http://localhost:8000\n";
    
} catch (Exception $e) {
    echo "❌ Error: " . $e->getMessage() . "\n";
    echo "Stack trace:\n" . $e->getTraceAsString() . "\n";
    exit(1);
}
