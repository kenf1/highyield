#import modules
import os
import shutil
from highyield import create

#gen_proj_folder
def gen_proj_folder(full_path,file_location):
    """To simplify the creation of a new repo. It achieves this task by creating a new folder and pastes `.gitignore` file from the specified location inside. However, this function can also be used for other files. Note: If folder already exists, the function will only add the specified file to said folder.

    Args:
        full_path (_type_): Full path to new folder.
        file_location (_type_): Full path to where `.gitignore` or file to copy from is located.
    """
    
    #checks if path already exist (creates folder if not)
    if os.path.exists(full_path) is True:
        print("Folder already exists.")
    else:
        os.mkdir(path=full_path)
        print(f"The folder {full_path} has been created.")
        
    #copy specified file
    shutil.copy(src=file_location,dst=f"{full_path}/")
    
    #print completion message
    print(f"The specified file from {file_location} has been copied to {full_path}.")
    
#proj_multi_file
def proj_multi_file(full_path,file_list):
    """Wrapper function around `gen_proj_folder` to generated a new folder and paste multiple files designated in list into the newly created folder.

    Args:
        full_path (_type_): Full path to new folder.
        file_list (_type_): A list of full paths to where files to copy from are located.
    """
    
    #copy each item in file_list
    for item in file_list:
        create.gen_proj_folder(full_path=full_path,file_location=item)
    
    #print completion message
    print("The function `proj_multi_file` has been successfully executed.")