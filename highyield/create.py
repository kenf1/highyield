#import modules
import os
import shutil

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
        
    #copy .gitignore file
    shutil.copy(src=file_location,dst=f"{full_path}/")
    
    #print completion message
    print(f"The folder {full_path} has been created with a `.gitignore` file copied from {file_location}.")