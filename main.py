from parse_invoices import extract_invoice_data
from db_writer import insert_invoice_data

folder_path = r"C:\Users\Blober\Downloads\invoices"

invoice_data = extract_invoice_data(folder_path)

insert_invoice_data(invoice_data)

print("✅ All invoices processed and saved to MySQL.")