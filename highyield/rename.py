#import modules
import os
import re

def bulk_rename(target_path,ext,new_name,search_term="[A-z0-9]*"):
    """Custom function to bulk rename files matching criteria specified by regular expressions. Will automatically sort and exclude `.DS_Store` (a macOS specific file) (if present).
    Args:
        target_path (path): Full path to target folder.
        ext (string): File extension (`.` included).
        new_name (string): New name for all matched files to share.
        search_term (regex): Name of files to include (can use regex), default is "[A-z0-9]*" to include all files inside target folder.
    """
    
    #list all files in target_path + sort in ascending order
    all_files = sorted(os.listdir(target_path))
    
    #rm DS_Store
    if all_files[0] == ".DS_Store":
        all_files = all_files[1:]
    else:
        all_files = all_files

    #use regex to filter (must meet both criteria)
    temp = [i for i in all_files if re.search(search_term,i) and re.search(ext,i)]

    #rename using for loop
    for count,filename in enumerate(temp):
        source = f"{target_path}/{filename}"
        dest = f"{target_path}/{new_name} {str(count)}.{ext}"
        os.rename(src=source,dst=dest)

    #tell user which files were renamed
    print("Complete. These files were renamed:")
    print(temp,sep=", ")