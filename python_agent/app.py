from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import logging
from datetime import datetime
import os
from dotenv import load_dotenv

# ==========================================
# CRITICAL: Load .env BEFORE importing router
# ==========================================
# Load environment variables from .env file FIRST
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
print(f"🔧 Loading .env from: {env_path}")
print(f"🔧 .env file exists: {os.path.exists(env_path)}")
print(f"🔧 Current working directory: {os.getcwd()}")
print(f"🔧 Absolute .env path: {os.path.abspath(env_path)}")

load_dotenv(env_path, verbose=True, override=True)

# Verify API key loaded BEFORE importing router
api_key = os.getenv("ANTHROPIC_API_KEY")
if api_key:
    print(f"✅ ANTHROPIC_API_KEY loaded successfully!")
    print(f"✅ API Key (first 20 chars): {api_key[:20]}...")
    print(f"✅ API Key length: {len(api_key)} chars")
else:
    print("❌❌❌ CRITICAL WARNING: ANTHROPIC_API_KEY not found in environment!")
    print(f"❌ Environment variables available: {list(os.environ.keys())[:10]}")

# NOW import router (after .env is loaded)
from router import analyze_transcript

# AI-generated code section begins - GitHub Copilot assisted with creating comprehensive Flask healthcare API
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Configure logging for better debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/process-transcript', methods=['POST'])
def process_transcript():
    """
    Main endpoint for processing medical transcripts
    Accepts JSON payload with transcript text and returns processing results
    """
    try:
        # Validate request data
        if not request.is_json:
            return jsonify({
                "status": "error",
                "message": "Request must be JSON",
                "timestamp": datetime.now().isoformat()
            }), 400
        
        data = request.json
        transcript_text = data.get('transcript', '').strip()
        
        # Log incoming request
        logger.info(f"📥 Processing transcript request: '{transcript_text[:100]}...'")
        
        # Validate transcript content
        if not transcript_text:
            return jsonify({
                "status": "error",
                "message": "Transcript text is required",
                "timestamp": datetime.now().isoformat()
            }), 400
        
        if len(transcript_text) < 3:
            return jsonify({
                "status": "error",
                "message": "Transcript text too short",
                "timestamp": datetime.now().isoformat()
            }), 400
        
        # Process the transcript through the router
        processing_result = analyze_transcript(transcript_text)
        
        # Return appropriate response based on processing result
        if processing_result:
            logger.info("✅ Transcript processing successful")
            return jsonify({
                "status": "success",
                "message": "Medical referral processed successfully",
                "description": "Referral has been routed to the appropriate specialist, PDF generated, and notifications sent",
                "features": {
                    "email_sent": True,
                    "pdf_generated": True,
                    "clinical_analysis": True,
                    "insurance_verified": True
                },
                "timestamp": datetime.now().isoformat()
            }), 200
        else:
            logger.info("ℹ️ No medical intent detected in transcript")
            return jsonify({
                "status": "ignored",
                "message": "No actionable medical intent detected",
                "description": "The transcript appears to be casual conversation rather than a medical referral",
                "timestamp": datetime.now().isoformat()
            }), 200
            
    except Exception as e:
        logger.error(f"❌ Error processing transcript: {str(e)}")
        return jsonify({
            "status": "error",
            "message": "Internal server error during transcript processing",
            "error_details": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint for monitoring system status
    """
    return jsonify({
        "status": "healthy",
        "service": "Healthcare Transcript Processing API",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat()
    }), 200

@app.route('/api/info', methods=['GET'])
def api_info():
    """
    API information endpoint showing available specialties and capabilities
    """
    from mock_db import SPECIALIST_REGISTRY, INSURANCE_PLANS
    
    return jsonify({
        "service_name": "Healthcare Referral Processing System",
        "description": "AI-powered medical transcript analysis for automated specialist referrals",
        "capabilities": {
            "patient_name_extraction": "Regex-based name detection from transcript",
            "specialty_detection": "Dynamic specialty matching with synonym support",
            "doctor_matching": "Automated specialist selection with rating optimization",
            "insurance_verification": "Real-time coverage checking and copay calculation",
            "medical_coding": "CPT and ICD-10 code assignment",
            "workflow_integration": "n8n webhook automation for notifications"
        },
        "supported_specialties": list(SPECIALIST_REGISTRY.keys()),
        "supported_insurance": list(INSURANCE_PLANS.keys()),
        "endpoints": {
            "/process-transcript": "POST - Main transcript processing endpoint",
            "/health": "GET - System health check",
            "/api/info": "GET - API information and capabilities"
        },
        "timestamp": datetime.now().isoformat()
    }), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors with helpful message"""
    return jsonify({
        "status": "error",
        "message": "Endpoint not found",
        "available_endpoints": ["/process-transcript", "/health", "/api/info"],
        "timestamp": datetime.now().isoformat()
    }), 404

@app.errorhandler(405)
def method_not_allowed(error):
    """Handle method not allowed errors"""
    return jsonify({
        "status": "error",
        "message": "Method not allowed for this endpoint",
        "timestamp": datetime.now().isoformat()
    }), 405

# ==========================================
# NEW ENDPOINTS FOR TWO-STAGE WORKFLOW
# ==========================================

@app.route('/api/analyze-referral', methods=['POST'])
def analyze_referral_endpoint():
    """
    Stage 1: Analyze Heidi session and return recommendation (NO EMAIL SENT)
    
    Request:
        {
            "session_id": 101
        }
    
    Response (Success):
        {
            "status": "success",
            "recommendation_id": "uuid-string",
            "recommendation": {
                "patient_name": "Emily Brown",
                "specialty": "cardiology",
                "doctor": {...},
                "reasoning": "...",
                "insurance": {...},
                ...
            }
        }
    
    Response (Error):
        {
            "status": "error",
            "error_code": "SESSION_NOT_FOUND",
            "message": "Session ID not found in database"
        }
    """
    from openemr_connector import fetch_heidi_session, fetch_patient_data
    from router import analyze_referral_only, store_recommendation
    
    try:
        logger.info("📥 Received analyze-referral request")
        
        # Validate request
        if not request.is_json:
            return jsonify({
                "status": "error",
                "error_code": "INVALID_INPUT",
                "message": "Request must be JSON"
            }), 400
        
        data = request.json
        session_id = data.get('session_id')
        
        if not session_id:
            return jsonify({
                "status": "error",
                "error_code": "INVALID_INPUT",
                "message": "Missing session_id in request"
            }), 400
        
        logger.info(f"🔍 Analyzing session ID: {session_id}")
        
        # Fetch Heidi session from OpenEMR database
        session_data = fetch_heidi_session(session_id)
        if not session_data:
            return jsonify({
                "status": "error",
                "error_code": "SESSION_NOT_FOUND",
                "message": f"Session ID {session_id} not found in database"
            }), 404
        
        logger.info(f"✅ Session found: {session_data['session_name']}")
        
        # Fetch patient data using PID from session
        patient_data = fetch_patient_data(session_data['pid'])
        if not patient_data:
            return jsonify({
                "status": "error",
                "error_code": "PATIENT_NOT_FOUND",
                "message": f"Patient ID {session_data['pid']} not found in database"
            }), 404
        
        logger.info(f"✅ Patient found: {patient_data['name']}")
        
        # Run analysis (no email sending)
        recommendation = analyze_referral_only(
            transcript_text=session_data['transcript'],
            patient_data=patient_data
        )
        
        if not recommendation:
            return jsonify({
                "status": "ignored",
                "message": "No medical referral intent detected in transcript"
            }), 200
        
        # Store recommendation in memory
        recommendation_id = store_recommendation(recommendation)
        
        logger.info(f"✅ Analysis complete: {recommendation_id}")
        
        # Log clinical note for debugging
        clinical_note = recommendation.get('clinical_triage_note')
        if clinical_note:
            logger.info(f"📋 Clinical Triage Note present: {clinical_note[:100]}...")
        else:
            logger.warning(f"⚠️ No clinical_triage_note in recommendation!")
        
        return jsonify({
            "status": "success",
            "recommendation_id": recommendation_id,
            "recommendation": {
                "patient_name": recommendation['patient_name'],
                "specialty": recommendation['specialty'],
                "doctor": recommendation['doctor'],
                "reasoning": recommendation['reasoning'],
                "insurance": recommendation['insurance'],
                "prior_auth": recommendation['prior_auth'],
                "procedure_codes": recommendation['procedure_codes'],
                "diagnosis_codes": recommendation['diagnosis_codes'],
                "clinical_summary": recommendation['clinical_summary'],
                "clinical_triage_note": recommendation.get('clinical_triage_note'),
                "predictive_alert": recommendation.get('predictive_alert'),
                "patient_dob": recommendation.get('patient_dob'),
                "patient_age": recommendation.get('patient_age'),
                "patient_sex": recommendation.get('patient_sex'),
                "patient_complaint": recommendation.get('patient_complaint'),
                "pdf_filename": recommendation.get('pdf_filename')
            }
        }), 200
        
    except Exception as e:
        logger.error(f"❌ Error in analyze-referral: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({
            "status": "error",
            "error_code": "ANALYSIS_FAILED",
            "message": f"Analysis failed: {str(e)}"
        }), 500

@app.route('/api/send-referral', methods=['POST'])
def send_referral_endpoint():
    """
    Stage 2: Send approved referral email with PDF
    
    Request:
        {
            "recommendation_id": "uuid-string"
        }
    
    Response (Success):
        {
            "status": "success",
            "message": "Referral sent to Dr. Sarah Johnson-Martinez",
            "pdf_filename": "medical_referral_123456.pdf"
        }
    
    Response (Error):
        {
            "status": "error",
            "error_code": "RECOMMENDATION_NOT_FOUND",
            "message": "Invalid or expired recommendation ID"
        }
    """
    from router import get_recommendation, send_referral_email, remove_recommendation
    
    try:
        logger.info("📧 Received send-referral request")
        
        # Validate request
        if not request.is_json:
            return jsonify({
                "status": "error",
                "error_code": "INVALID_INPUT",
                "message": "Request must be JSON"
            }), 400
        
        data = request.json
        recommendation_id = data.get('recommendation_id')
        
        if not recommendation_id:
            return jsonify({
                "status": "error",
                "error_code": "INVALID_INPUT",
                "message": "Missing recommendation_id in request"
            }), 400
        
        logger.info(f"📤 Sending referral: {recommendation_id}")
        
        # Retrieve recommendation from memory
        recommendation_data = get_recommendation(recommendation_id)
        if not recommendation_data:
            return jsonify({
                "status": "error",
                "error_code": "RECOMMENDATION_NOT_FOUND",
                "message": "Invalid or expired recommendation ID"
            }), 404
        
        # Send email with PDF
        result = send_referral_email(recommendation_data)
        
        # Remove from memory after sending (success or failure)
        remove_recommendation(recommendation_id)
        
        if result['status'] == 'success':
            logger.info(f"✅ Referral sent successfully")
            return jsonify(result), 200
        else:
            logger.error(f"❌ Referral send failed: {result['message']}")
            return jsonify(result), 500
        
    except Exception as e:
        logger.error(f"❌ Error in send-referral: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({
            "status": "error",
            "error_code": "EMAIL_SEND_FAILED",
            "message": f"Failed to send email: {str(e)}"
        }), 500

@app.route('/api/pdf/<filename>', methods=['GET'])
def serve_pdf(filename):
    """
    Serve PDF files for preview
    
    Example: GET /api/pdf/preview_medical_referral_123456.pdf
    """
    try:
        # Security: Only allow preview_ prefixed files
        if not filename.startswith('preview_'):
            return jsonify({
                "status": "error",
                "message": "Access denied"
            }), 403
        
        pdf_path = os.path.join(os.path.dirname(__file__), filename)
        
        if not os.path.exists(pdf_path):
            return jsonify({
                "status": "error",
                "message": "PDF file not found"
            }), 404
        
        logger.info(f"📄 Serving PDF: {filename}")
        return send_file(
            pdf_path,
            mimetype='application/pdf',
            as_attachment=False,  # Display inline, not download
            download_name=filename
        )
        
    except Exception as e:
        logger.error(f"❌ Error serving PDF: {str(e)}")
        return jsonify({
            "status": "error",
            "message": f"Error serving PDF: {str(e)}"
        }), 500

if __name__ == '__main__':
    print("🏥 Healthcare Transcript Processing API")
    print("=" * 50)
    print("🚀 Server starting on http://localhost:5000")
    print("📋 Available endpoints:")
    print("   POST /process-transcript - Process medical transcripts")
    print("   GET  /health           - Health check")
    print("   GET  /api/info         - API information")
    print("=" * 50)
    
    app.run(
        host='0.0.0.0',  # Allow external connections
        port=5001,
        debug=True,
        use_reloader=False,  # Disable reloader for background execution
        threaded=True  # Handle multiple requests
    )
# AI-generated code section ends