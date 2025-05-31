import fitz
import re 
import os

#this a test
#doc = fitz.open(r"C:\Users\Blober\Downloads\invoices\INV-117_Naman.pdf") C:\Users\Blober\Downloads\invoices

print("test")
def extract_invoice_data(folder_path):
#folderpath = r"C:\Users\Blober\Downloads\invoices"
    
    results = []

    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        
        try:
            doc = fitz.open(filepath)
            text= ''
            for page in doc:
                text += page.get_text()

            invoices_no = re.search(r"Invoice\s*#[:\s]*([\w\-]+)", text, re.IGNORECASE)
            if invoices_no:
                invoices_id = invoices_no.group(1)
            else:
                print("No match found.")

            matchTotal = re.search(r"Total\s*[\n\r]*\s*₹([\d,]+\.\d{2})", text)

            if matchTotal:
                matched_string = matchTotal.group(1)  # This is a string now
                Total = matched_string.replace('/', '').replace('\n', '').replace('₹', '').replace(',', '')
                # Output: 'Total1,667.00'
            else:
                print("No match found.")

            date = re.search(r"Invoice Date\s*#?:?\s*(\d{2}\s+[a-zA-Z]{3}\s+\d{4})", text, re.IGNORECASE)

            if date:
                invoice_date = date.group(1)  # ← this is the string: '01 Jan 2025'    
            else:
                print("No date found.")

            lines = text.splitlines()
            found = False

           
            for i, line in enumerate(lines):
                print(f"Line {i}: {line}")

                if "Customer Details" in line:
                    for j in range(i+1, len(lines)):
                        next_line = lines[j].strip()
                        if next_line:
                            print("Customer Name:", next_line)
                            found = True
                            break
                    break

            if not found:
                print("Name not found.")


            results.append((invoices_id, Total, invoice_date)) 


    
        except Exception as e:
                print(f"❌ Error reading {filename}: {e}")

                #results is missing 
            
    return results
