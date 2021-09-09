import argparse
import os
from pdfminer import high_level
from pdfminer.layout import LTTextBoxHorizontal

# Example search_word = '2-450/750 V'
#Author: macperez


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


def find(fpath, search_word, path_list):
    if os.path.isfile(fpath):
        if '.pdf' in fpath or '.PDF' in fpath:
            # pdf_path = os.path.join(dire
            if search_in_file(fpath, search_word):
                print(f'>> {fpath}')
                path_list.append(fpath)
    elif os.path.isdir(fpath):
        print(f"Explorando directorio: {fpath}")
        for fi in os.listdir(fpath):
            new_path = os.path.join(fpath, fi)
            find(new_path, search_word, path_list)




def main(to_excel, search_word, directory):
    if to_excel:
        output_file = open('results.txt', 'a')
    foundpaths = []
    find(directory, search_word, foundpaths)
    if len(foundpaths) > 0:
        for el in foundpaths:
            if to_excel:
                output_file.write(el + '\n') 
            print(el)
    else: 
        print('No se ha encontrado ningún fichero con ese texto')    

    if to_excel:
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