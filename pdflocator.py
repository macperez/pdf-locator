import argparse
import os
from pdfminer import high_level
from pdfminer.layout import LTTextBoxHorizontal

# Example search_word = '2-450/750 V'



def search_in_file(pdf_file, search_word):
    found = False
    for page in high_level.extract_pages(pdf_file):
        for element in page:
            if isinstance(element, LTTextBoxHorizontal):
                text = element.get_text()
                if search_word in text: 
                    found = True 
                    break
    return found


def main(to_excel, search_word, directory):
    if to_excel:
        print('Exportando los resultados a un bloc de notas')
        output_file = open('results.txt', 'a')

    for fi in os.listdir(directory):
        if '.pdf' in fi or '.PDF' in fi:
            pdf_path = os.path.join(directory, fi)
            if search_in_file(pdf_path, search_word):
                output_msg = f'>> {pdf_path}\n'
                print(output_msg)
                if to_excel:
                    output_file.write(output_msg)
    if to_excel and output_file:
        output_file.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("text", help="Texto a buscar en los documentos pdfs")
    parser.add_argument("folder", help="Carpeta donde va realizarse la búsqueda")
    parser.add_argument("--notepad", help="Export results to notepad",
                    action="store_true")
    args = parser.parse_args()
    to_excel = True if args.notepad else False
    main(to_excel, args.text, args.folder)