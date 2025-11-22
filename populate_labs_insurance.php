#!/usr/bin/env php
<?php
/**
 * AI-generated code - Script to populate OpenEMR patients with lab data and insurance
 * This script adds lab results and insurance information to existing test patients
 */

// Bootstrap OpenEMR
$_GET['site'] = 'default';
$ignoreAuth = true;

// Bootstrap globals  
require_once __DIR__ . '/interface/globals.php';

echo "🔬 OpenEMR Lab Data & Insurance Population Script\n";
echo "================================================\n\n";

// Get all test fixture patients
$patients_sql = "SELECT pid, fname, lname, DOB, sex FROM patient_data WHERE pubpid LIKE 'test-fixture-%' ORDER BY pid";
$patients_result = sqlStatement($patients_sql);

$lab_count = 0;
$insurance_count = 0;

// Common insurance providers
$insurance_providers = [
    ['name' => 'Blue Cross Blue Shield', 'plan' => 'PPO Gold', 'group' => 'GRP001', 'policy_type' => 'Primary'],
    ['name' => 'Aetna', 'plan' => 'HMO Standard', 'group' => 'GRP002', 'policy_type' => 'Primary'],
    ['name' => 'United Healthcare', 'plan' => 'PPO Silver', 'group' => 'GRP003', 'policy_type' => 'Primary'],
    ['name' => 'Cigna', 'plan' => 'EPO Bronze', 'group' => 'GRP004', 'policy_type' => 'Primary'],
    ['name' => 'Kaiser Permanente', 'plan' => 'HMO Plus', 'group' => 'GRP005', 'policy_type' => 'Primary'],
    ['name' => 'Medicare', 'plan' => 'Part A & B', 'group' => 'MED001', 'policy_type' => 'Primary'],
    ['name' => 'Medicaid', 'plan' => 'Standard', 'group' => 'MCD001', 'policy_type' => 'Primary']
];

// Lab test templates
$lab_tests = [
    [
        'test_name' => 'Complete Blood Count (CBC)',
        'loinc' => '58410-2',
        'results' => [
            ['name' => 'White Blood Cells', 'value' => '7.2', 'units' => 'K/uL', 'range' => '4.5-11.0'],
            ['name' => 'Red Blood Cells', 'value' => '4.8', 'units' => 'M/uL', 'range' => '4.5-5.9'],
            ['name' => 'Hemoglobin', 'value' => '14.5', 'units' => 'g/dL', 'range' => '13.5-17.5'],
            ['name' => 'Hematocrit', 'value' => '42.3', 'units' => '%', 'range' => '38.8-50.0'],
            ['name' => 'Platelets', 'value' => '250', 'units' => 'K/uL', 'range' => '150-400']
        ]
    ],
    [
        'test_name' => 'Basic Metabolic Panel',
        'loinc' => '24323-8',
        'results' => [
            ['name' => 'Glucose', 'value' => '95', 'units' => 'mg/dL', 'range' => '70-100'],
            ['name' => 'Sodium', 'value' => '140', 'units' => 'mmol/L', 'range' => '136-145'],
            ['name' => 'Potassium', 'value' => '4.2', 'units' => 'mmol/L', 'range' => '3.5-5.1'],
            ['name' => 'Chloride', 'value' => '102', 'units' => 'mmol/L', 'range' => '98-107'],
            ['name' => 'BUN', 'value' => '15', 'units' => 'mg/dL', 'range' => '7-20'],
            ['name' => 'Creatinine', 'value' => '0.9', 'units' => 'mg/dL', 'range' => '0.7-1.3']
        ]
    ],
    [
        'test_name' => 'Lipid Panel',
        'loinc' => '24331-1',
        'results' => [
            ['name' => 'Total Cholesterol', 'value' => '185', 'units' => 'mg/dL', 'range' => '<200'],
            ['name' => 'HDL Cholesterol', 'value' => '55', 'units' => 'mg/dL', 'range' => '>40'],
            ['name' => 'LDL Cholesterol', 'value' => '110', 'units' => 'mg/dL', 'range' => '<100'],
            ['name' => 'Triglycerides', 'value' => '120', 'units' => 'mg/dL', 'range' => '<150']
        ]
    ],
    [
        'test_name' => 'Liver Function Tests',
        'loinc' => '24325-3',
        'results' => [
            ['name' => 'ALT', 'value' => '28', 'units' => 'U/L', 'range' => '7-56'],
            ['name' => 'AST', 'value' => '25', 'units' => 'U/L', 'range' => '10-40'],
            ['name' => 'Alkaline Phosphatase', 'value' => '75', 'units' => 'U/L', 'range' => '44-147'],
            ['name' => 'Total Bilirubin', 'value' => '0.8', 'units' => 'mg/dL', 'range' => '0.1-1.2']
        ]
    ]
];

while ($patient = sqlFetchArray($patients_result)) {
    $pid = $patient['pid'];
    $fname = $patient['fname'];
    $lname = $patient['lname'];
    
    echo "👤 Processing {$fname} {$lname} (PID: {$pid})\n";
    
    // Add Insurance (check if not exists)
    $check_ins = "SELECT COUNT(*) as cnt FROM insurance_data WHERE pid = ? AND type = 'primary'";
    $ins_exists = sqlQuery($check_ins, [$pid]);
    
    if ($ins_exists['cnt'] == 0) {
        try {
            $insurance = $insurance_providers[array_rand($insurance_providers)];
            $policy_number = 'POL' . str_pad($pid, 8, '0', STR_PAD_LEFT);
            
            $ins_sql = "INSERT INTO insurance_data (
                pid, type, provider, plan_name, policy_number, group_number, 
                subscriber_fname, subscriber_lname, subscriber_relationship,
                subscriber_DOB, subscriber_sex, date
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NOW())";
            
            sqlStatement($ins_sql, [
                $pid,
                'primary',
                $insurance['name'],
                $insurance['plan'],
                $policy_number,
                $insurance['group'],
                $patient['fname'],
                $patient['lname'],
                'self',
                $patient['DOB'],
                $patient['sex']
            ]);
            
            $insurance_count++;
            echo "  ✅ Insurance: {$insurance['name']} - {$insurance['plan']} (Policy: {$policy_number})\n";
        } catch (Exception $e) {
            echo "  ❌ Error adding insurance: " . $e->getMessage() . "\n";
        }
    } else {
        echo "  ⏭️  Insurance already exists, skipping\n";
    }
    
    // Add Lab Results (1-2 random tests per patient)
    $num_tests = rand(1, 2);
    $selected_tests = array_rand($lab_tests, $num_tests);
    if (!is_array($selected_tests)) {
        $selected_tests = [$selected_tests];
    }
    
    foreach ($selected_tests as $test_idx) {
        $lab_test = $lab_tests[$test_idx];
        
        try {
            // Create procedure order
            $order_sql = "INSERT INTO procedure_order (
                patient_id, provider_id, date_ordered, order_status, 
                order_priority, order_diagnosis, date_collected
            ) VALUES (?, ?, NOW(), 'complete', 'normal', 'Routine screening', NOW())";
            
            $order_id = sqlInsert($order_sql, [$pid, 1]);
            
            // Create procedure order code
            $code_sql = "INSERT INTO procedure_order_code (
                procedure_order_id, procedure_code, procedure_name, 
                procedure_order_seq
            ) VALUES (?, ?, ?, ?)";
            
            sqlStatement($code_sql, [
                $order_id,
                $lab_test['loinc'],
                $lab_test['test_name'],
                1
            ]);
            
            // Create procedure report
            $report_sql = "INSERT INTO procedure_report (
                procedure_order_id, procedure_order_seq, date_collected,
                date_report, report_status, review_status
            ) VALUES (?, ?, NOW(), NOW(), 'final', 'reviewed')";
            
            $report_id = sqlInsert($report_sql, [$order_id, 1]);
            
            // Add results
            foreach ($lab_test['results'] as $idx => $result) {
                // Add some variation to results
                $value = $result['value'];
                if (is_numeric($value)) {
                    $variation = $value * (rand(90, 110) / 100);
                    $value = number_format($variation, 1);
                }
                
                $result_detail_sql = "INSERT INTO procedure_result (
                    procedure_report_id, result_code, result_text, result, units, `range`,
                    abnormal, result_status, date
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, NOW())";
                
                sqlStatement($result_detail_sql, [
                    $report_id,
                    'LOINC:' . $lab_test['loinc'],
                    $result['name'],
                    $value,
                    $result['units'],
                    $result['range'],
                    'N',
                    'final'
                ]);
            }
            
            $lab_count++;
            echo "  ✅ Lab: {$lab_test['test_name']} (" . count($lab_test['results']) . " results)\n";
            
        } catch (Exception $e) {
            echo "  ❌ Error adding lab: " . $e->getMessage() . "\n";
        }
    }
    
    echo "\n";
}

echo "✨ Data population complete!\n";
echo "📊 Summary:\n";
echo "  - Insurance policies added: {$insurance_count}\n";
echo "  - Lab tests added: {$lab_count}\n";
echo "\n💡 You can now view this data in OpenEMR:\n";
echo "  - Patient demographics → Insurance tab\n";
echo "  - Patient chart → Lab Results\n";
