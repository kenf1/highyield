#import modules
import os
import pandas as pd
import docx2pdf

#csv2xlsx
def csv2xlsx(target_dir,current_name,header="infer"):
    """Function to convert `.csv` files to `.xlsx`. Slightly modified from `xlsx2csv` function.

    Args:
        target_dir (_type_): Directory target file is located in. Will also be where generated `.xlsx` will be saved.
        current_name (_type_): Name of `.csv` file.
        header (str, optional): Include header row? Defaults to "infer" (makes best guess).
    """
    
    #change directory
    os.chdir(path=target_dir)

    #split current_name into name & extension
    file_name, ext = os.path.splitext(current_name)

    #import xlsx file
    data = pd.read_csv(filepath_or_buffer=current_name,header=header)

    #xlsx name
    new_file_name = f"{file_name}.xlsx"

    #write to csv
    data.to_excel(excel_writer=new_file_name)
    
    #tell user which file has been converted
    print("Complete")
    print(f"{current_name} has been converted to {new_file_name} in {target_dir}")
    
#xlsx2csv
def xlsx2csv(target_dir,current_name,sheet_name=0,sep=",",index=None,header=True):
    """Function to convert `.xls*` files to `.csv`. Slightly modified from `csv2xlsx` function.

    Args:
        target_dir (_type_): Directory target file is located in. Will also be where generated `.csv` will be saved.
        current_name (_type_): Name of `.xls*` file.
        sheet_name (_type_): Name of sheet. Defaults to 0 (1st sheet).
        sep (str, optional): Separator to use for `.csv`. Defaults to ",".
        index (_type_, optional): Write row names? Defaults to None.
        header (bool, optional): Include header row? Defaults to True.
    """
    
    #change directory
    os.chdir(path=target_dir)

    #split current_name into name & extension
    file_name, ext = os.path.splitext(current_name)

    #import xlsx file
    data = pd.read_excel(io=current_name,sheet_name=sheet_name)

    #csv name
    new_file_name = f"{file_name}.csv"

    #write to csv
    data.to_csv(path_or_buf=new_file_name,sep=sep,index=index,header=header)
    
    #tell user which file has been converted
    print("Complete")
    print(f"{current_name} has been converted to {new_file_name} in {target_dir}")
    
#word2pdf
def word2pdf(target_dir,current_name):
    """Function to convert `.doc*` files to `.pdf`. Might need to grant access to certain files/folders (dependent on operating system).

    Args:
        target_dir (_type_): Directory target file is located in. Will also be where generated `.pdf` will be saved.
        current_name (_type_): Name of `.doc*` file.
    """

    #change directory
    os.chdir(path=target_dir)

    #split current_name into name & extension
    file_name, ext = os.path.splitext(current_name)

    #pdf name
    new_file_name = f"{file_name}.pdf"

    #convert to pdf
    docx2pdf.convert(input_path=current_name,output_path=new_file_name)

    #tell user which file has been converted
    print("Complete")
    print(f"{current_name} has been converted to {new_file_name} in {target_dir}")