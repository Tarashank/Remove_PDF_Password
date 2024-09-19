import fitz  # PyMuPDF
import os

def remove_password(input_pdf, output_pdf, password):
    pdf_document = fitz.open(input_pdf)

    # Check if the PDF is encrypted
    if pdf_document.isEncrypted:
        # Try to authenticate with the provided password
        if pdf_document.authenticate(password):
            # Create a new PDF writer
            pdf_writer = fitz.open()

            # Copy all pages to the new PDF
            for page_num in range(pdf_document.page_count):
                pdf_writer.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)

            # Save the result to the output PDF file
            pdf_writer.save(output_pdf)
            pdf_writer.close()

            print(f"Password removed successfully from '{input_pdf}'.")
        else:
            print(f"Incorrect password. Unable to remove password from '{input_pdf}'.")
    else:
        print(f"The PDF '{input_pdf}' is not encrypted. No password to remove.")

# Example usage with multiple PDF files
input_directory = r'D:/Personal/....'
output_directory = r'D:/Personal/.....'

password_to_remove = '0wdSDFG(N(##7' 

# Get a list of all PDF files in the input directory
pdf_files = [file for file in os.listdir(input_directory) if file.lower().endswith('.pdf')]

# Process each PDF file
for pdf_file in pdf_files:
    input_pdf_path = os.path.abspath(os.path.join(input_directory, pdf_file))
    output_pdf_path = os.path.abspath(os.path.join(output_directory, pdf_file))

    if os.path.exists(input_pdf_path):
        remove_password(input_pdf_path, output_pdf_path, password_to_remove)
    else:
        print(f"The file '{input_pdf_path}' does not exist.")
