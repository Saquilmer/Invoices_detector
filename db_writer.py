import  mysql.connector
from datetime import datetime

def insert_invoice_data(data):
    if data is not None:
        db_name = "invoices"
        base_conn = mysql.connector.connect(
            host="localhost", #Mysql@localhost:3306
            port=3306,
            user="root",
            password="Administrador01", #change this !!!!    
        )
        base_cursor = base_conn.cursor()

        
        base_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        
        base_cursor.close()
        base_conn.close()

        conn = mysql.connector.connect(
        
            host="localhost", #Mysql@localhost:3306
            port=3306,
            user="root",
            password="Administrador01", #change this !!!!   
            database=db_name 
            
        )
        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS invoices (
                id INT AUTO_INCREMENT PRIMARY KEY,
                invoice_number VARCHAR(50),
                invoice_date DATE,
                total DECIMAL(10, 2),
                file_name VARCHAR(255)
            )
        """)

        for invoice_id, Total, invoice_date in data:
            try:
                parsed_date = datetime.strptime(invoice_date, "%d %b %Y").date()
                    
                if invoice_id != "Not Found" and invoice_date != "Not Found" and Total != "Not Found":  
                    cursor.execute("""
                        INSERT INTO invoices (invoice_number, invoice_date, total)
                        VALUES (%s, %s, %s)
                    """, (invoice_id, parsed_date, Total ))
            except Exception as e:
                print(f"Error inserting data from {invoice_id}: {e}")        

        conn.commit()
        cursor.close()
        conn.close()
    else:
         print("Error!")
