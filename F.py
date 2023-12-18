from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas

def add_watermark(input_pdf, watermark_pdf, output_pdf):

  

    with open(output_pdf, 'wb') as file:
        output.write(file)

def create_watermark(input_text, output_pdf):
    c = canvas.Canvas(output_pdf)
    c.setFont("Helvetica", 12)
    c.rotate(45)
    c.drawString(150, 0, input_text)
    c.save()

if __name__ == "__main__":
    input_pdf_path = sys.argv[1]
    watermark_text = "CONFIDENTIAL WATERMARK"
    watermark_pdf_path = "watermark_temp.pdf"
    output_pdf_path = "Watermarked_PDF.pdf"

 
    create_watermark(watermark_text, watermark_pdf_path)

    
    add_watermark(input_pdf_path, watermark_pdf_path, output_pdf_path)

  e
    os.remove(watermark_pdf_path)

    print("Watermark added to PDF.")
