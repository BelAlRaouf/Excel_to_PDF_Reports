import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")


for filepath in filepaths:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    # print("this is file path = ", filename)
    invoice_nr = filename.split("-")[0]
    # print("this is the invoice number", invoice_nr)
    pdf.set_font(family="Times", size=20, style="B")
    pdf.cell(w=50, h=10, txt=f"Invoice No: {invoice_nr}", ln=1)

    date = filename.split("-")[1]
    pdf.cell(w=50, h=20, txt=f"Date: {date}", ln=1)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    file_columns = list(df.columns)
    file_columns = [item.replace("_", " ").title() for item in file_columns]
    pdf.set_font(family="Times", size=9, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=str(file_columns[0]), border=1)
    pdf.cell(w=70, h=8, txt=str(file_columns[1]), border=1)
    pdf.cell(w=30, h=8, txt=str(file_columns[2]), border=1)
    pdf.cell(w=30, h=8, txt=str(file_columns[3]), border=1)
    pdf.cell(w=30, h=8, txt=str(file_columns[4]), border=1, ln=1)
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=9)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)
    # Calculating the total price and adding empy cells.
    total_price = df['total_price'].sum()
    pdf.set_font(family="Times", size=9, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=70, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_price), border=1, ln=1)

    # adding the
    pdf.set_font(family="Times", size=14, style="B")
    pdf.cell(w=30, h=8, txt=f"The total price is {total_price}", ln=1)

    pdf.set_font(family="Times", size=14, style="B")
    pdf.cell(w=30, h=8, txt="Belal Raouf", ln=1)

    pdf.output(f"PDF/{filename}.pdf")
