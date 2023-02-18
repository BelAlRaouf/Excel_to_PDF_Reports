import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")
# print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    # print("this is file path = ", filename)
    invoice_nr = filename.split("-")[0]
    # print("this is the invoice number", invoice_nr)
    pdf.set_font(family="Times", size=20, style="B")
    pdf.cell(w=50, h=10, txt=f"Invoice Nr: {invoice_nr}", ln=1)

    date = filename.split("-")[1]
    pdf.cell(w=50, h=20, txt=f"Date: {date}")
    pdf.output(f"PDF/{filename}.pdf")
