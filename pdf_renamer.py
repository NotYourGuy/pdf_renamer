import os
import argparse
import cv2
import re
import numpy as np
from pdf2image import convert_from_path
import pytesseract


def ocr_pdf_title(pdf_path):
    pages = convert_from_path(pdf_path, 500)
    candidate_titles = []
    for page in pages:
        # Convert to grayscale and threshold the image to black and white
        img = cv2.cvtColor(np.array(page), cv2.COLOR_RGB2GRAY)
        _, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Extract text from the image using Tesseract
        text = pytesseract.image_to_string(img)

        # Look for the first three lines that start with a capital letter
        for line in text.split('\n'):
            if line.strip() and line[0].isupper() and len(candidate_titles) < 3:
                candidate_titles.append(line.strip())

        if len(candidate_titles) == 3:
            break

    # Prompt the user to choose one of the candidate titles
    for i, title in enumerate(candidate_titles):
        print(f'{i+1}. {title}')
    choice = input('Which title do you want to use? ')

    try:
        choice = int(choice)
        if choice < 1 or choice > len(candidate_titles):
            raise ValueError()
    except ValueError:
        print('Invalid choice')
        return None

    return candidate_titles[choice-1]



def rename_pdf_title(pdf_path):
    # Get the title of the PDF
    title = ocr_pdf_title(pdf_path)
    if not title:
        print(f'Could not find a title for {pdf_path}')
        return

    # Escape special characters in the title
    title = re.sub(r'[<>:"/\\|?*]', '', title)

    # Rename the file with the title
    pdf_dir = os.path.dirname(os.path.abspath(pdf_path))
    pdf_name = os.path.basename(pdf_path)
    new_name = os.path.join(pdf_dir, f'{title}.pdf')
    os.rename(pdf_path, new_name)
    print(f'Renamed {pdf_path} to {new_name}')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Rename a PDF file based on its title.')
    parser.add_argument('pdf_path', type=str, help='path to the PDF file')
    args = parser.parse_args()
    rename_pdf_title(args.pdf_path)
