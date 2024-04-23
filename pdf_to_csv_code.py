import fitz
import csv

def pdf_to_csv(input_path, output_path):
    # Open the PDF
    doc = fitz.open(input_path)

    # Create a CSV writer object
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)

        headers_written = False  # Flag to track if headers are written

        for page in doc:
            # Find tables on the page
            tables = page.find_tables()

            # If tables are found
            if tables:
                # Iterate over each table on the page
                for idx, table in enumerate(tables):
                    # Extract table data
                    table_data = table.extract()

                    # If headers are not yet written, write them
                    if not headers_written:
                        csv_writer.writerows(table_data)
                        headers_written = True
                    else:
                        # Write each row to the CSV file except the first one (headers)
                        csv_writer.writerows(table_data[1:])

    print("Conversion successful!")

# Replace 'test.pdf' and 'output.csv' with your input PDF file and desired output CSV file

pdf_to_csv(r"C:\Users\jatin\OneDrive\Desktop\d2.pdf", r"C:\Users\jatin\Downloads\d11.csv")
