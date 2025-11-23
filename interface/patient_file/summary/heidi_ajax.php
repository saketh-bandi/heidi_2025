<?php

/**
 * heidi_ajax.php
 * AJAX handler for Heidi API integration
 *
 * @package   OpenEMR
 * @link      http://www.open-emr.org
 * @author    Heidi Integration Team
 * @copyright Copyright (c) 2025
 * @license   https://github.com/openemr/openemr/blob/master/LICENSE GNU General Public License 3
 */

// AI-generated code START - GitHub Copilot
// Enable error logging for debugging
error_log("========================================");
error_log("[Heidi AJAX DEBUG] Step 1: Request received");
error_log("[Heidi AJAX DEBUG] Request URI: " . $_SERVER['REQUEST_URI']);
error_log("[Heidi AJAX DEBUG] Request Method: " . $_SERVER['REQUEST_METHOD']);
error_log("[Heidi AJAX DEBUG] Action: " . ($_GET['action'] ?? $_POST['action'] ?? 'NONE'));
error_log("[Heidi AJAX DEBUG] Patient ID: " . ($_GET['patient_id'] ?? 'NONE'));
error_log("[Heidi AJAX DEBUG] GET params: " . json_encode($_GET));
error_log("[Heidi AJAX DEBUG] POST params: " . json_encode($_POST));

// Set JSON header FIRST before any output
error_log("[Heidi AJAX DEBUG] Step 2: Setting JSON header");
header('Content-Type: application/json');

// Check if session is active before requiring globals.php
error_log("[Heidi AJAX DEBUG] Step 3: Checking PHP session");
if (!isset($_SESSION) || empty($_SESSION)) {
    error_log("[Heidi AJAX DEBUG] WARNING: No active PHP session before globals.php");
} else {
    error_log("[Heidi AJAX DEBUG] PHP session exists, session_id: " . session_id());
}

error_log("[Heidi AJAX DEBUG] Step 4: Loading globals.php");
require_once("../../globals.php");
error_log("[Heidi AJAX DEBUG] Step 5: globals.php loaded successfully");

use OpenEMR\Common\Csrf\CsrfUtils;
use OpenEMR\Services\HeidiApiService;

// Verify CSRF token
error_log("[Heidi AJAX DEBUG] Step 6: Verifying CSRF token");
$csrfToken = $_GET["csrf_token"] ?? $_POST["csrf_token"] ?? '';
error_log("[Heidi AJAX DEBUG] CSRF Token received: " . ($csrfToken ? substr($csrfToken, 0, 20) . "..." : "EMPTY"));

if (!CsrfUtils::verifyCsrfToken($csrfToken)) {
    error_log("[Heidi AJAX DEBUG] ERROR: CSRF token verification FAILED");
    http_response_code(403);
    echo json_encode([
        'success' => false,
        'error' => 'Invalid CSRF token - please refresh the page'
    ]);
    exit;
}

error_log("[Heidi AJAX DEBUG] ✓ CSRF token verified successfully");

$action = $_GET['action'] ?? $_POST['action'] ?? '';
error_log("[Heidi AJAX DEBUG] Step 7: Action determined: " . $action);

// Check if OpenEMR session is valid
error_log("[Heidi AJAX DEBUG] Step 8: Checking OpenEMR session");
if (!isset($_SESSION['site_id']) || empty($_SESSION['site_id'])) {
    error_log("[Heidi AJAX DEBUG] ERROR: OpenEMR session not initialized");
    error_log("[Heidi AJAX DEBUG] SESSION vars: " . json_encode(array_keys($_SESSION)));
    echo json_encode([
        'success' => false,
        'error' => 'OpenEMR session not active - please log in to OpenEMR'
    ]);
    exit;
}

error_log("[Heidi AJAX DEBUG] ✓ OpenEMR session active");
error_log("[Heidi AJAX DEBUG] Site ID: " . $_SESSION['site_id']);
error_log("[Heidi AJAX DEBUG] User ID: " . ($_SESSION['authUserID'] ?? 'N/A'));

error_log("[Heidi AJAX DEBUG] Step 9: Initializing HeidiApiService");
$heidiService = new HeidiApiService();
error_log("[Heidi AJAX DEBUG] ✓ HeidiApiService initialized");
// AI-generated code END

error_log("[Heidi AJAX DEBUG] Step 10: Entering switch statement for action: " . $action);

try {
    switch ($action) {
        case 'get_patient_session_data':
            error_log("[Heidi AJAX DEBUG] Step 11: Processing 'get_patient_session_data' action");
            // New simplified endpoint that returns all session data at once
            $patientId = $_GET['patient_id'] ?? 0;
            error_log("[Heidi AJAX DEBUG] Patient ID from request: " . $patientId);
            
            if (!$patientId) {
                error_log("[Heidi AJAX DEBUG] ERROR: Patient ID is missing or zero");
                throw new Exception('Patient ID is required');
            }
            
            error_log("[Heidi AJAX DEBUG] Step 12: Calling getPatientSessionData($patientId)");
            $data = $heidiService->getPatientSessionData($patientId);
            error_log("[Heidi AJAX DEBUG] Step 13: Received data from service");
            error_log("[Heidi AJAX DEBUG] Data keys: " . json_encode(array_keys($data)));
            error_log("[Heidi AJAX DEBUG] Data success: " . ($data['success'] ?? 'N/A'));
            error_log("[Heidi AJAX DEBUG] Data error: " . ($data['error'] ?? 'N/A'));
            error_log("[Heidi AJAX DEBUG] Step 14: Encoding response as JSON");
            $jsonResponse = json_encode($data);
            error_log("[Heidi AJAX DEBUG] JSON response length: " . strlen($jsonResponse));
            echo $jsonResponse;
            error_log("[Heidi AJAX DEBUG] ✓✓✓ Response sent successfully");
            error_log("========================================");
            break;
            
        case 'get_patient_sessions':
            $patientId = $_GET['patient_id'] ?? 0;
            if (!$patientId) {
                throw new Exception('Patient ID is required');
            }
            
            $sessions = $heidiService->getPatientSessions($patientId);
            echo json_encode([
                'success' => true,
                'sessions' => $sessions
            ]);
            break;
            
        case 'get_session':
            $sessionId = $_GET['session_id'] ?? '';
            if (!$sessionId) {
                throw new Exception('Session ID is required');
            }
            
            $session = $heidiService->getSession($sessionId);
            echo json_encode([
                'success' => true,
                'session' => $session
            ]);
            break;
            
        case 'get_session_transcript':
            $sessionId = $_GET['session_id'] ?? '';
            if (!$sessionId) {
                throw new Exception('Session ID is required');
            }
            
            $transcript = $heidiService->getSessionTranscript($sessionId);
            echo json_encode([
                'success' => true,
                'transcript' => $transcript
            ]);
            break;
            
        case 'get_session_notes':
            $sessionId = $_GET['session_id'] ?? '';
            if (!$sessionId) {
                throw new Exception('Session ID is required');
            }
            
            $notes = $heidiService->getSessionNotes($sessionId);
            echo json_encode([
                'success' => true,
                'notes' => $notes
            ]);
            break;
            
        case 'link_session':
            $patientId = $_POST['patient_id'] ?? 0;
            $sessionId = $_POST['session_id'] ?? '';
            
            if (!$patientId || !$sessionId) {
                throw new Exception('Patient ID and Session ID are required');
            }
            
            $result = $heidiService->linkSessionToPatient($patientId, $sessionId);
            echo json_encode([
                'success' => true,
                'message' => 'Session linked successfully'
            ]);
            break;
            
        case 'unlink_session':
            $patientId = $_POST['patient_id'] ?? 0;
            $sessionId = $_POST['session_id'] ?? '';
            
            if (!$patientId || !$sessionId) {
                throw new Exception('Patient ID and Session ID are required');
            }
            
            $result = $heidiService->unlinkSessionFromPatient($patientId, $sessionId);
            echo json_encode([
                'success' => true,
                'message' => 'Session unlinked successfully'
            ]);
            break;
            
        case 'get_available_sessions':
            $sessions = HeidiApiService::getAvailableSessionIds();
            echo json_encode([
                'success' => true,
                'sessions' => $sessions
            ]);
            break;
            
        default:
            throw new Exception('Invalid action');
    }
} catch (Exception $e) {
    http_response_code(400);
    echo json_encode([
        'success' => false,
        'error' => $e->getMessage()
    ]);
}
