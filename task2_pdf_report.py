from fpdf import FPDF

def generate_pdf_report():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Sample PDF Report", ln=True, align='C')
    pdf.cell(200, 10, txt="Data Analysis Report", ln=True, align='C')
    pdf.output("report.pdf")
    print("PDF Report Generated Successfully!")

if __name__ == "__main__":
    generate_pdf_report()
