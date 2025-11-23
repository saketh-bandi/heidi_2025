# pdf_generator.py
# AI-generated code section begins - GitHub Copilot assisted with robust medical PDF generation

from fpdf import FPDF
from datetime import datetime
import base64
import re

def sanitize_text_for_pdf(text):
    """Strict text sanitization for PDF generation with explicit latin-1 encoding"""
    if not text:
        return ""
    
    # Convert to string if not already
    text = str(text)
    
    # Remove or replace problematic Unicode characters
    replacements = {
        # Smart quotes
        '\u2018': "'", '\u2019': "'", '\u201c': '"', '\u201d': '"',
        # Em dash, en dash
        '\u2014': '-', '\u2013': '-',
        # Other common problematic characters
        '\u2022': '-', '\u2026': '...', '\u00a0': ' ',
        # Currency symbols
        '\u20ac': 'EUR', '\u00a3': 'GBP', '\u00a5': 'YEN',
        # Mathematical symbols
        '\u00b1': '+/-', '\u00d7': 'x', '\u00f7': '/',
    }
    
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    # Remove any remaining non-ASCII characters using regex
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    
    # EXPLICIT LATIN-1 ENCODING - This is critical for PDF integrity
    try:
        # Force encode/decode to latin-1 to catch any problematic characters
        text = text.encode('latin-1', errors='replace').decode('latin-1')
        return text
    except Exception as e:
        print(f"Warning: Text sanitization error: {e}")
        # Ultimate fallback - only ASCII characters
        return ''.join(char for char in text if ord(char) < 128)

class MedicalReferralFormPDF(FPDF):
    """Professional Medical Referral Form PDF Generator - Complete Form Layout"""
    
    def __init__(self):
        super().__init__()
        # CRITICAL: Disable auto page break to prevent blank pages
        self.set_auto_page_break(auto=False)
        
    def header(self):
        """PDF Header with medical letterhead styling - matches target design"""
        try:
            # Header background - Professional blue (#2C5282)
            self.set_fill_color(44, 82, 130)
            self.rect(0, 0, 210, 25, 'F')
            
            # Header text - centered, white
            self.set_font('Arial', 'B', 20)
            self.set_text_color(255, 255, 255)
            self.set_y(8)
            self.cell(0, 10, 'MEDICAL REFERRAL FORM', 0, 1, 'C')
            self.ln(5)
        except Exception as e:
            print(f"Warning: PDF header generation issue: {e}")
        
    def footer(self):
        """PDF Footer with timestamp and page numbers - matches target design"""
        try:
            self.set_y(-15)
            self.set_font('Arial', '', 8)
            self.set_text_color(100, 100, 100)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            footer_text = sanitize_text_for_pdf(f'Generated: {timestamp} | Page {self.page_no()}')
            self.cell(0, 10, footer_text, 0, 0, 'C')
        except Exception as e:
            print(f"Warning: PDF footer generation issue: {e}")

    def draw_form_box(self, x, y, width, height, label, content, multiline=False):
        """Draw a labeled form box with content - matches target design"""
        try:
            # Draw box border - medium gray
            self.set_draw_color(150, 150, 150)
            self.set_line_width(0.3)
            self.rect(x, y, width, height)
            
            # Label background - light gray (#E5E7EB)
            self.set_fill_color(229, 231, 235)
            self.rect(x, y, width, 7, 'F')
            
            # Label text
            self.set_font('Arial', 'B', 7)
            self.set_text_color(0, 0, 0)
            self.set_xy(x + 2, y + 1.5)
            sanitized_label = sanitize_text_for_pdf(label)
            self.cell(width - 4, 5, sanitized_label, 0, 0, 'L')
            
            # Content
            self.set_font('Arial', '', 11)
            self.set_xy(x + 2, y + 9)
            sanitized_content = sanitize_text_for_pdf(str(content))
            
            if multiline:
                # For multiline content, use a contained multi_cell
                available_width = width - 4
                available_height = height - 12
                # Manually handle text wrapping within the box
                if len(sanitized_content) > 50:
                    lines = []
                    words = sanitized_content.split()
                    current_line = ""
                    
                    for word in words:
                        test_line = current_line + (" " if current_line else "") + word
                        if len(test_line) <= 50:  # Rough character limit per line
                            current_line = test_line
                        else:
                            if current_line:
                                lines.append(current_line)
                            current_line = word
                    
                    if current_line:
                        lines.append(current_line)
                    
                    # Print each line
                    for i, line in enumerate(lines[:3]):  # Max 3 lines
                        self.set_xy(x + 2, y + 10 + (i * 5))
                        self.cell(available_width, 5, line, 0, 0, 'L')
                else:
                    self.cell(available_width, 5, sanitized_content, 0, 0, 'L')
            else:
                # Single line content
                self.cell(width - 4, 5, sanitized_content, 0, 0, 'L')
                
        except Exception as e:
            print(f"Warning: Failed to draw form box '{label}': {e}")

    def draw_large_text_box(self, x, y, width, height, label, content):
        """Draw a large text box for detailed information - matches target design"""
        try:
            # Draw box border - medium gray
            self.set_draw_color(150, 150, 150)
            self.set_line_width(0.3)
            self.rect(x, y, width, height)
            
            # Label background - light gray (#E5E7EB)
            self.set_fill_color(229, 231, 235)
            self.rect(x, y, width, 7, 'F')
            
            # Label text
            self.set_font('Arial', 'B', 7)
            self.set_text_color(0, 0, 0)
            self.set_xy(x + 2, y + 1.5)
            sanitized_label = sanitize_text_for_pdf(label)
            self.cell(width - 4, 5, sanitized_label, 0, 0, 'L')
            
            # Content area
            self.set_font('Arial', '', 9)
            self.set_xy(x + 2, y + 10)
            sanitized_content = sanitize_text_for_pdf(str(content))
            
            # Word wrap for large content
            words = sanitized_content.split()
            lines = []
            current_line = ""
            chars_per_line = int((width - 4) / 2.5)  # Approximate character width
            
            for word in words:
                test_line = current_line + (" " if current_line else "") + word
                if len(test_line) <= chars_per_line:
                    current_line = test_line
                else:
                    if current_line:
                        lines.append(current_line)
                    current_line = word
            
            if current_line:
                lines.append(current_line)
            
            # Print lines with proper spacing
            max_lines = int((height - 15) / 4)  # Available height for lines
            for i, line in enumerate(lines[:max_lines]):
                self.set_xy(x + 2, y + 12 + (i * 4))
                self.cell(width - 4, 4, line, 0, 0, 'L')
                
        except Exception as e:
            print(f"Warning: Failed to draw large text box '{label}': {e}")

    def safe_cell(self, w, h, txt='', border=0, ln=0, align='', fill=False):
        """Safe cell method that sanitizes text before adding to PDF"""
        try:
            sanitized_text = sanitize_text_for_pdf(txt)
            self.cell(w, h, sanitized_text, border, ln, align, fill)
        except Exception as e:
            print(f"Warning: Failed to add cell text: {e}")
            self.cell(w, h, '[Text encoding error]', border, ln, align, fill)

    def safe_multi_cell(self, w, h, txt, border=0, align='L', fill=False):
        """Safe multi_cell method that sanitizes text before adding to PDF"""
        try:
            sanitized_text = sanitize_text_for_pdf(txt)
            self.multi_cell(w, h, sanitized_text, border, align, fill)
        except Exception as e:
            print(f"Warning: Failed to add multi-cell text: {e}")
            self.multi_cell(w, h, '[Text encoding error - content unavailable]', border, align, fill)

def create_referral_pdf(patient_name, doctor, insurance_result, clinical_context, 
                       procedure_codes, diagnosis_codes, specialty, 
                       patient_dob=None, patient_age=None, patient_sex=None, patient_complaint=None,
                       patient_data=None, pa_result=None):
    """
    Generate a professional medical referral form PDF and return binary content
    CRITICAL: Returns binary PDF data instead of saving to disk for file integrity
    """
    # AI-generated code section begins - GitHub Copilot assisted with robust PDF generation
    
    # Create timestamp for reference (not used for filename anymore)
    timestamp = datetime.now().strftime('%H%M%S')
    
    print(f"📄 Generating Medical Referral Form (Binary Output): referral_{timestamp}")
    
    # Create PDF instance with error handling
    try:
        pdf = MedicalReferralFormPDF()
        # CRITICAL: Only add ONE page and set compact margins
        pdf.add_page()
        pdf.set_margins(8, 8, 8)  # Reduced margins for more space
        
        # Reset text color for body content
        pdf.set_text_color(0, 0, 0)
    except Exception as e:
        print(f"❌ PDF initialization error: {e}")
        return None, None
    
    # FORM GENERATION with error handling
    try:
        # DATE AND REFERENCE NUMBER - Row 1
        current_date = datetime.now().strftime("%m/%d/%Y")
        ref_number = f"REF-{timestamp}"
        
        # PROFESSIONAL LAYOUT - Matches target design exactly
        # Row 1: Date and Reference Number
        pdf.draw_form_box(10, 40, 90, 20, "DATE OF REFERRAL", current_date)
        pdf.draw_form_box(108, 40, 92, 20, "REFERENCE NUMBER", ref_number)
        
        # Row 2: Patient Name, Age, Sex
        pdf.draw_form_box(10, 65, 90, 20, "PATIENT NAME", patient_name or "Not Provided")
        pdf.draw_form_box(108, 65, 45, 20, "AGE", patient_age or "Not Provided")
        pdf.draw_form_box(158, 65, 42, 20, "SEX", patient_sex or "Not Provided")
        
        # Row 3: Date of Birth and Insurance Plan
        pdf.draw_form_box(10, 90, 90, 20, "DATE OF BIRTH", patient_dob or "Not Provided")
        pdf.draw_form_box(108, 90, 92, 20, "INSURANCE PLAN", insurance_result.get('plan', 'Unknown'))
        
        # Row 4: Network Status and Estimated Copay
        network_status = insurance_result.get('status', 'Unknown')
        copay_info = insurance_result.get('copay', 'N/A')
        pdf.draw_form_box(10, 115, 90, 20, "NETWORK STATUS", network_status)
        pdf.draw_form_box(108, 115, 92, 20, "ESTIMATED COPAY", copay_info)
        
        # Row 5: Referring to Specialist and Specialty
        pdf.draw_form_box(10, 140, 90, 20, "REFERRING TO SPECIALIST", 
                         f"{doctor.get('name', 'Unknown Provider')}")
        pdf.draw_form_box(108, 140, 92, 20, "SPECIALTY", specialty.title())
        
        # Row 6: NPI Number and Clinic/Practice
        pdf.draw_form_box(10, 165, 63, 18, "NPI NUMBER", doctor.get('npi', 'N/A'))
        pdf.draw_form_box(78, 165, 122, 18, "CLINIC/PRACTICE", doctor.get('clinic', 'Unknown Clinic'))
        
        # Row 7: Major Complaint / Presenting Symptoms (full width)
        major_complaint = patient_complaint or clinical_context or "General consultation requested"
        pdf.draw_large_text_box(10, 188, 190, 25, "MAJOR COMPLAINT / PRESENTING SYMPTOMS", major_complaint)
        
        # Row 8: Clinical Context / History (full width)
        pdf.draw_large_text_box(10, 218, 190, 28, "CLINICAL CONTEXT / HISTORY", clinical_context or "See complaint above")
        
        # PAGE 1 COMPLETE - Matches target design
        # Additional information can be added on page 2 if needed
        
    except Exception as e:
        print(f"❌ Error generating form content: {e}")
        # Add fallback content
        pdf.set_font('Arial', '', 12)
        pdf.set_xy(10, 50)
        pdf.safe_cell(0, 10, "Error: Unable to generate form content properly", 0, 1, 'L')
    
    # Generate PDF as binary data - CRITICAL for file integrity
    try:
        print(f"📄 Generating PDF binary content...")
        
        # Use dest='S' to return PDF as binary data instead of saving to disk
        pdf_binary = pdf.output(dest='S')
        
        # Handle different FPDF versions - newer versions return bytes directly
        if isinstance(pdf_binary, str):
            pdf_binary = pdf_binary.encode('latin-1')
        # If it's already bytes or bytearray, convert to bytes
        elif isinstance(pdf_binary, bytearray):
            pdf_binary = bytes(pdf_binary)
        
        if pdf_binary and len(pdf_binary) > 1000:  # Reasonable size check
            print(f"✅ PDF Generated Successfully: {len(pdf_binary)} bytes (binary)")
            
            # Create filename for reference
            filename = f"medical_referral_{timestamp}.pdf"
            
            # Return both binary data and filename
            return pdf_binary, filename
        else:
            print(f"❌ PDF generation failed - binary data too small or empty")
            return None, None
            
    except UnicodeEncodeError as e:
        print(f"❌ PDF Unicode Encoding Error: {e}")
        print("   Text sanitization failed - check input data")
        return None, None
    except Exception as e:
        print(f"❌ PDF Generation Error: {e}")
        print(f"   Error type: {type(e).__name__}")
        return None, None
    
    # AI-generated code section ends

def test_pdf_generation():
    """Test function for PDF generation with comprehensive patient data"""
    # AI-generated code section begins - GitHub Copilot assisted with comprehensive test data
    sample_doctor = {
        'name': 'Dr. Emily Chen',
        'npi': '1457389201',
        'clinic': 'Mercy Heart Institute',
        'address': '1234 Medical Plaza Dr, San Francisco, CA 94115'
    }
    
    sample_insurance = {
        'plan': 'Blue Cross Blue Shield PPO',
        'status': 'IN-NETWORK',
        'copay': '$25.00'
    }
    
    sample_procedures = [
        {'code': '99244', 'description': 'Office consultation for cardiac evaluation', 'cost': '$450'},
        {'code': '93000', 'description': 'Electrocardiogram (ECG/EKG)', 'cost': '$150'}
    ]
    
    sample_diagnoses = [
        {'code': 'I25.10', 'description': 'Atherosclerotic heart disease'},
        {'code': 'I20.9', 'description': 'Angina pectoris, unspecified'}
    ]
    
    pdf_binary, filename = create_referral_pdf(
        patient_name="John Smith",
        doctor=sample_doctor,
        insurance_result=sample_insurance,
        clinical_context="Patient presenting with chest pain and shortness of breath. Episodes occur with exertion and resolve with rest. No radiation to arms or jaw. Patient reports increased frequency over past 2 weeks.",
        procedure_codes=sample_procedures,
        diagnosis_codes=sample_diagnoses,
        specialty="cardiology",
        patient_dob="03/15/1975",
        patient_age="48",
        patient_sex="Male",
        patient_complaint="Chest pain with exertion, shortness of breath, palpitations"
    )
    
    # Save binary data to file for testing
    if pdf_binary and filename:
        with open(filename, 'wb') as f:
            f.write(pdf_binary)
        print(f"💾 Test PDF saved to disk: {filename}")
    
    return pdf_binary, filename
    # AI-generated code section ends

if __name__ == "__main__":
    print("🧪 Testing PDF Generation...")
    pdf_binary, test_filename = test_pdf_generation()
    if pdf_binary and test_filename:
        print(f"✅ Test PDF created: {test_filename} ({len(pdf_binary)} bytes)")
    else:
        print("❌ PDF generation failed")

# AI-generated code section ends
