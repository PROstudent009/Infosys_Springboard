import pytesseract
from pdf2image import convert_from_path
from PyPDF2 import PdfReader

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
    except Exception as e:
        print(f"Error reading PDF directly: {e}")
    
    if not text:
        print("Falling back to OCR for scanned PDF.")
        images = convert_from_path(pdf_path)
        text = ""
        for image in images:
            text += pytesseract.image_to_string(image)
    
    return text

def clean_text(text):
    # Clean the text (remove headers, footers, symbols)
    text = text.replace("\n", " ").strip()
    return text

# Test the function with a sample PDF
pdf_path = "data/sample.pdf"
raw_text = extract_text_from_pdf(pdf_path)
cleaned_text = clean_text(raw_text)
