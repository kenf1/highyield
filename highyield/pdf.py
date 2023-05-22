#import modules
import os
from pypdf import PdfReader

#extract text from single page of pdf
def pdf_extract_single(file_path,page_num):
    """Extract text from single page of pdf.

    Args:
        file_path (str): Full path to pdf file.
        page_num (int): Page to extract text from. 0 = page 1.
    """
    
    #import pdf
    reader = PdfReader(file_path)
    
    #save selected pdf page
    pdfpage = reader.pages[page_num]
    
    #print extracted text
    print(pdfpage.extract_text())

#extract text from all pages of pdf
def pdf_extract_all(file_path):
    """Extract text from all pages of pdf.

    Args:
        file_path (str): Full path to pdf file.
    """
    
    #import pdf
    reader = PdfReader(file_path)

    #get total num pages 
    num_pages = len(reader.pages)

    #extract text
    for i in range(num_pages):
        pdfpage = reader.pages[i]
        print(pdfpage.extract_text())
        
#extract text from selected pages of pdf
def pdf_extract_range(file_path,lower_bound,upper_bound):
    """Extract text from range of pages in pdf.

    Args:
        file_path (str): Full path to pdf file.
        lower_bound (int): Page to start extracting from. 0 = page 1.
        upper_bound (int): Page to stop extracting from. Text from this page and afterwards will not be included.
    """
    
    #import pdf
    reader = PdfReader(file_path)

    #extract text
    for i in range(lower_bound,upper_bound):
        pdfpage = reader.pages[i]
        print(pdfpage.extract_text())