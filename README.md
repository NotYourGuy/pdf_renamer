# pdf_renamer

Python script that renames PDF files by OCR scanning the file and extracting the first three words that start with a capital letter (usually the Author, Title, Publication).

## Usage:
Using `pdf_renamer.py` will allow you to rename one PDF file at a time using the current title as an argument, as such:
```bash
$ python pdf_renamer.py title_to_be_changed.pdf
```
---
Using `pdf_renamer_bulk.py`	will ask you for a directory where you keep your PDF files and iterate through them one by one letting you choose the title of the file.

## Requirements:
The script requires to install the following pip modules:
```bash
pip install pdf2image opencv-python pytesseract tesseract
```

Also, if on Debian (or derivatives) you would need to install the following as well for Tesseract to work (didn't test on other distributions):
```bash
sudo apt-get install python3-pil tesseract-ocr libtesseract-dev tesseract-ocr-eng tesseract-ocr-script-latn
```
