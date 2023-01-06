#import modules
import os
import re

#bulk_rename
def bulk_rename(target_path,search_term,ext,new_name):
    """Custom function to bulk rename files matching criteria specified by regular expressions.

    Args:
        target_path (path): Full path to target folder
        search_term (regex): Name of files to include, use "[A-z0-9]*" to include all files inside target folder
        ext (string): File extension (`.` included)
        new_name (string): New name for all matched files to share
    """
    
    #list all files in target_path
    all_files = os.listdir(target_path)

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