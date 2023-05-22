#import modules
import os
import shutil
import pandas as pd

#automate_copy
def automate_copy(ref_file,source_col="source",dest_col="dest"):
    """Use `.csv` or `.xls*` file to automate process of copying files from source path to destination path. Either file must have header. Copies file data and permissions.

    Args:
        ref_file (str): Separate `.csv` or `.xls*` file containing full path of source & destination to pass into `shutil.copy` function.
        source_col (str, optional): Source column. Defaults to "source".
        dest_col (str, optional): Destination column. Defaults to "dest".
    """
    
    #det ext type
    ext = os.path.splitext(ref_file)[1]
    
    #use diff import dep on ext type
    if ext == ".csv":
        
        #import using read_csv
        ref_df = pd.read_csv(filepath_or_buffer=ref_file)
    
    elif ext == ".xls" or ext == ".xlsx":
        
        #import using read_excel
        ref_df = pd.read_excel(io=ref_file)
    
    #non `.csv` or `xls*` extensions
    else:
        print("Failed to recognize `ref_file` format. Please try again using 1 of the following formats: `.csv`, `.xls` or `.xlsx`.")

    #run shutil.copy using for loop
    for i in range(len(ref_df)):
        shutil.copy(src=ref_df.loc[i,source_col],dst=ref_df.loc[i,dest_col])
        
    #print completion message
    print("Complete. Files have been copied from specified source to specified destination.")
    
#automate_copy2
def automate_copy2(ref_file,source_col="source",dest_col="dest"):
    """Use `.csv` or `.xls*` file to automate process of copying files from source path to destination path. Either file must have header. Copies file data, permissions, and metadata.

    Args:
        ref_file (str): Separate `.csv` or `.xls*` file containing full path of source & destination to pass into `shutil.copy` function.
        source_col (str, optional): Source column. Defaults to "source".
        dest_col (str, optional): Destination column. Defaults to "dest".
    """
    
    #det ext type
    ext = os.path.splitext(ref_file)[1]
    
    #use diff import dep on ext type
    if ext == ".csv":
        
        #import using read_csv
        ref_df = pd.read_csv(filepath_or_buffer=ref_file)
    
    elif ext == ".xls" or ext == ".xlsx":
        
        #import using read_excel
        ref_df = pd.read_excel(io=ref_file)
    
    #non `.csv` or `xls*` extensions
    else:
        print("Failed to recognize `ref_file` format. Please try again using 1 of the following formats: `.csv`, `.xls` or `.xlsx`.")

    #run shutil.copy using for loop
    for i in range(len(ref_df)):
        shutil.copy2(src=ref_df.loc[i,source_col],dst=ref_df.loc[i,dest_col])
        
    #print completion message
    print("Complete. Files have been copied from specified source to specified destination.")
    
#automate_copyfile
def automate_copyfile(ref_file,source_col="source",dest_col="dest"):
    """Use `.csv` or `.xls*` file to automate process of copying files from source path to destination path. Either file must have header. Files are copied without permissions and metadata.

    Args:
        ref_file (str): Separate `.csv` or `.xls*` file containing full path of source & destination to pass into `shutil.copy` function.
        source_col (str, optional): Source column. Defaults to "source".
        dest_col (str, optional): Destination column. Defaults to "dest".
    """
    
    #det ext type
    ext = os.path.splitext(ref_file)[1]
    
    #use diff import dep on ext type
    if ext == ".csv":
        
        #import using read_csv
        ref_df = pd.read_csv(filepath_or_buffer=ref_file)
    
    elif ext == ".xls" or ext == ".xlsx":
        
        #import using read_excel
        ref_df = pd.read_excel(io=ref_file)
    
    #non `.csv` or `xls*` extensions
    else:
        print("Failed to recognize `ref_file` format. Please try again using 1 of the following formats: `.csv`, `.xls` or `.xlsx`.")

    #run shutil.copy using for loop
    for i in range(len(ref_df)):
        shutil.copyfile(src=ref_df.loc[i,source_col],dst=ref_df.loc[i,dest_col])
        
    #print completion message
    print("Complete. Files have been copied from specified source to specified destination.")