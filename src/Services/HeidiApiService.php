<?php

/**
 * HeidiApiService.php
 *
 * @package   OpenEMR
 * @link      http://www.open-emr.org
 * @author    Heidi Integration Team
 * @copyright Copyright (c) 2025
 * @license   https://github.com/openemr/openemr/blob/master/LICENSE GNU General Public License 3
 */

namespace OpenEMR\Services;

use GuzzleHttp\Client;
use GuzzleHttp\Exception\GuzzleException;

/**
 * Service for integrating with Heidi Health API
 * Documentation: https://www.heidihealth.com/developers
 */
class HeidiApiService
{
    private $apiBaseUrl;
    private $apiKey;
    private $client;
    private $jwtToken;
    private $tokenExpiration;
    
    /**
     * Constructor
     * Loads configuration from environment variables
     */
    public function __construct()
    {
        // Load API configuration from environment (check both $_ENV and getenv)
        $this->apiBaseUrl = $_ENV['HEIDI_API_BASE_URL'] ?? getenv('HEIDI_API_BASE_URL') ?: 'https://registrar.api.heidihealth.com/api/v2/ml-scribe/open-api';
        $this->apiKey = $_ENV['HEIDI_API_KEY'] ?? getenv('HEIDI_API_KEY');
        
        // Load JWT token directly from environment (skip authentication)
        $this->jwtToken = $_ENV['HEIDI_JWT_TOKEN'] ?? getenv('HEIDI_JWT_TOKEN');
        
        if (empty($this->jwtToken)) {
            error_log('HEIDI_JWT_TOKEN not found in environment, will need to authenticate');
        }
        
        // Ensure base URL ends with trailing slash for proper relative path handling
        $baseUri = rtrim($this->apiBaseUrl, '/') . '/';
        
        $this->client = new Client([
            'base_uri' => $baseUri,
            'timeout' => 30,
            'headers' => [
                'Accept' => 'application/json',
                'Content-Type' => 'application/json'
            ]
        ]);
    }
    
    /**
     * Authenticate and get JWT token
     * Uses GET /jwt endpoint as per Swagger OpenAPI specification
     *
     * @param string $email User email
     * @param string $userId Third party internal user ID
     * @return array|null Token data or null on failure
     */
    public function authenticate($email = 'openemr@example.com', $userId = '123')
    {
        try {
            $response = $this->client->request('GET', 'jwt', [
                'headers' => [
                    'Heidi-Api-Key' => $this->apiKey
                ],
                'query' => [
                    'email' => $email,
                    'third_party_internal_id' => $userId
                ]
            ]);
            
            $data = json_decode($response->getBody()->getContents(), true);
            
            if (isset($data['token'])) {
                $this->jwtToken = $data['token'];
                $this->tokenExpiration = $data['expiration_time'] ?? null;
                return $data;
            }
            
            return null;
        } catch (GuzzleException $e) {
            error_log("Heidi API Authentication Error: " . $e->getMessage());
            return null;
        }
    }
    
    /**
     * Link API user to a Heidi account
     * POST /users/linked-account
     *
     * @param string $kindeUserId The Heidi kinde_user_id to link to
     * @return array|null Linked account data or null on failure
     */
    public function linkAccount($kindeUserId)
    {
        try {
            $token = $this->getToken();
            if (!$token) {
                error_log("Heidi API: Failed to get token for linking account");
                return null;
            }
            
            $response = $this->client->request('POST', 'users/linked-account', [
                'headers' => [
                    'Authorization' => 'Bearer ' . $token
                ],
                'json' => [
                    'kinde_user_id' => $kindeUserId
                ]
            ]);
            
            return json_decode($response->getBody()->getContents(), true);
        } catch (GuzzleException $e) {
            error_log("Heidi API Link Account Error: " . $e->getMessage());
            return null;
        }
    }
    
    /**
     * Get valid JWT token (uses token from environment)
     *
     * @return string|null JWT token
     */
    private function getToken()
    {
        // Return the pre-configured JWT token from environment
        if (!empty($this->jwtToken)) {
            return $this->jwtToken;
        }
        
        // Fallback: try to authenticate if no token configured
        error_log('No JWT token configured, attempting authentication...');
        $auth = $this->authenticate();
        if ($auth && isset($auth['token'])) {
            $this->jwtToken = $auth['token'];
            return $this->jwtToken;
        }
        
        error_log('Failed to get JWT token');
        return null;
    }
    
    /**
     * Get session details by session ID
     *
     * @param string $sessionId Heidi session ID
     * @return array|null Session data or null on failure
     */
    public function getSession($sessionId)
    {
        $token = $this->getToken();
        if (!$token) {
            return null;
        }
        
        try {
            $response = $this->client->request('GET', 'sessions/' . $sessionId, [
                'headers' => [
                    'Authorization' => 'Bearer ' . $token
                ]
            ]);
            
            return json_decode($response->getBody()->getContents(), true);
        } catch (GuzzleException $e) {
            error_log("Heidi API Get Session Error: " . $e->getMessage());
            return null;
        }
    }
    
    /**
     * Get transcript for a session
     *
     * @param string $sessionId Heidi session ID
     * @return array|null Transcript data or null on failure
     */
    public function getSessionTranscript($sessionId)
    {
        $token = $this->getToken();
        if (!$token) {
            return null;
        }
        
        try {
            $response = $this->client->request('GET', 'sessions/' . $sessionId . '/transcript', [
                'headers' => [
                    'Authorization' => 'Bearer ' . $token
                ]
            ]);
            
            return json_decode($response->getBody()->getContents(), true);
        } catch (GuzzleException $e) {
            error_log("Heidi API Get Transcript Error: " . $e->getMessage());
            return null;
        }
    }
    
    /**
     * Get clinical notes for a session
     *
     * @param string $sessionId Heidi session ID
     * @return array|null Clinical notes data or null on failure
     */
    public function getSessionNotes($sessionId)
    {
        $token = $this->getToken();
        if (!$token) {
            return null;
        }
        
        try {
            $response = $this->client->request('GET', 'sessions/' . $sessionId . '/notes', [
                'headers' => [
                    'Authorization' => 'Bearer ' . $token
                ]
            ]);
            
            return json_decode($response->getBody()->getContents(), true);
        } catch (GuzzleException $e) {
            error_log("Heidi API Get Notes Error: " . $e->getMessage());
            return null;
        }
    }
    
    /**
     * Get all sessions for a patient (from local database mapping)
     *
     * @param int $patientId OpenEMR patient ID
     * @return array Array of session IDs
     */
    public function getPatientSessions($patientId)
    {
        $sql = "SELECT heidi_session_id, created_date 
                FROM heidi_patient_sessions 
                WHERE patient_id = ? 
                ORDER BY created_date DESC";
        
        $result = sqlStatement($sql, [$patientId]);
        $sessions = [];
        
        while ($row = sqlFetchArray($result)) {
            $sessions[] = $row['heidi_session_id'];
        }
        
        return $sessions;
    }
    
    /**
     * Link a Heidi session to a patient
     *
     * @param int $patientId OpenEMR patient ID
     * @param string $sessionId Heidi session ID
     * @return bool Success status
     */
    public function linkSessionToPatient($patientId, $sessionId)
    {
        $sql = "INSERT INTO heidi_patient_sessions (patient_id, heidi_session_id, created_date) 
                VALUES (?, ?, NOW())
                ON DUPLICATE KEY UPDATE created_date = NOW()";
        
        return sqlStatement($sql, [$patientId, $sessionId]);
    }
    
    /**
     * Remove session link from patient
     *
     * @param int $patientId OpenEMR patient ID
     * @param string $sessionId Heidi session ID
     * @return bool Success status
     */
    public function unlinkSessionFromPatient($patientId, $sessionId)
    {
        $sql = "DELETE FROM heidi_patient_sessions 
                WHERE patient_id = ? AND heidi_session_id = ?";
        
        return sqlStatement($sql, [$patientId, $sessionId]);
    }
    
    /**
     * Get available session IDs (for demo/testing)
     *
     * @return array Array of available session IDs
     */
    public static function getAvailableSessionIds()
    {
        return [
            '337851254565527952685384877024185083869',
            '75033324869996810677299265415934259470',
            '209429578973190336673242710141917128963',
            '316272209747326581157737075663692625433',
            '48329781058232302558277795670340808022',
            '189878368687884891206528465309407076433',
            '179340005192510878551324680590964837821',
            '53587316790682971446935880515324100567'
        ];
    }

    /**
     * Get the session ID mapped to a specific patient ID
     * Maps patients 1-8 to sessions 0-7, then cycles for higher patient IDs
     *
     * @param int $patientId OpenEMR patient ID
     * @return string|null Heidi session ID or null if patient ID is invalid
     */
    public static function getSessionIdForPatient($patientId)
    {
        if ($patientId < 1) {
            return null;
        }
        
        $sessions = self::getAvailableSessionIds();
        $index = ($patientId - 1) % count($sessions);
        return $sessions[$index];
    }

    /**
     * Get all session data for a patient (transcript + notes combined)
     *
     * @param int $patientId OpenEMR patient ID
     * @return array Combined session data
     */
    public function getPatientSessionData($patientId)
    {
        error_log("[HeidiService DEBUG] ========================================");
        error_log("[HeidiService DEBUG] Step 1: getPatientSessionData called");
        error_log("[HeidiService DEBUG] Patient ID: " . $patientId);
        
        error_log("[HeidiService DEBUG] Step 2: Getting session ID for patient");
        $sessionId = self::getSessionIdForPatient($patientId);
        error_log("[HeidiService DEBUG] Mapped Session ID: " . ($sessionId ?? 'NULL'));
        
        if (!$sessionId) {
            error_log("[HeidiService DEBUG] ERROR: No session ID mapped to patient");
            return [
                'success' => false,
                'error' => 'No session mapped to this patient'
            ];
        }

        try {
            error_log("[HeidiService DEBUG] Step 3: Fetching session data from Heidi API");
            $session = $this->getSession($sessionId);
            error_log("[HeidiService DEBUG] Session data received: " . ($session ? 'YES' : 'NULL'));
            
            error_log("[HeidiService DEBUG] Step 4: Fetching transcript");
            $transcript = $this->getSessionTranscript($sessionId);
            error_log("[HeidiService DEBUG] Transcript received: " . ($transcript ? 'YES' : 'NULL'));
            
            error_log("[HeidiService DEBUG] Step 5: Fetching notes");
            $notes = $this->getSessionNotes($sessionId);
            error_log("[HeidiService DEBUG] Notes received: " . ($notes ? 'YES' : 'NULL'));

            // Check if we actually got data back
            if (!$session) {
                error_log("[HeidiService DEBUG] ERROR: Session data is NULL");
                return [
                    'success' => false,
                    'error' => 'Unable to retrieve session data from Heidi API',
                    'session_id' => $sessionId
                ];
            }

            error_log("[HeidiService DEBUG] Step 6: Building response array");
            if (is_array($session)) {
                error_log("[HeidiService DEBUG] Session keys: " . json_encode(array_keys($session)));
            }
            
            $response = [
                'success' => true,
                'session_id' => $sessionId,
                'patient_id' => $patientId,
                'session' => $session,
                'transcript' => $transcript,
                'notes' => $notes
            ];
            
            error_log("[HeidiService DEBUG] ✓✓✓ Response built successfully");
            error_log("[HeidiService DEBUG] ========================================");
            return $response;
        } catch (\Exception $e) {
            error_log("[HeidiService DEBUG] EXCEPTION caught: " . $e->getMessage());
            error_log("[HeidiService DEBUG] Exception trace: " . $e->getTraceAsString());
            return [
                'success' => false,
                'error' => $e->getMessage(),
                'session_id' => $sessionId
            ];
        }
    }
}
