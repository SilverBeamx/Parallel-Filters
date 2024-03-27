import PyPDF2
import re

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        text = ''
        for page_number in range(num_pages):
            page = reader.pages[page_number]
            text += page.extract_text()

    return text

def write_words_to_file(text, output_file):
    # Remove non-alphanumeric characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # Split the text into words
    words = text.split()

    # Write each word to the file
    with open(output_file, 'w') as file:
        for word in words:
            file.write(word + '\n')

if __name__ == "__main__":
    pdf_path = 'input.pdf'  # Specify the path to your PDF file
    output_file = 'output.txt'  # Specify the output file path

    pdf_text = extract_text_from_pdf(pdf_path)
    write_words_to_file(pdf_text,output_file)
