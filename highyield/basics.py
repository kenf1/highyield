#import modules
import os
import requests

#list all files from specified path
def list_files(path):
    """List all files (including hidden) from specified path.

    Args:
        path (str): Path to folder.
    """
    
    folder_contents = os.listdir(path)
    return folder_contents

#open application from specified path
def open_app(app_path):
    """Open application from specified path.

    Args:
        app_path (str): Path to app.
    """
    
    full_path = f"open {app_path}"
    os.system(full_path)
    
#download pre-defined quarto templates
def quarto_templates(template_name,path,file_name):
    """Download from list of pre-defined Quarto templates.

    Args:
        template_name (str): Name of template to download: `General` or `Presentation`.
        path (str): Path to store file. Exclude file name. `/` is optional.
        file_name (str): Name of file. Include extension.
    """
    
    #store urls inside class
    class urls:
        gen = "https://raw.githubusercontent.com/kenf1/KScripts/main/Quarto%20Templates/General.qmd"
        pres = "https://raw.githubusercontent.com/kenf1/KScripts/main/Quarto%20Templates/Presentation.qmd"
    
    #present options
    if template_name == "General":
        url = urls.gen
    elif template_name == "Presentation":
        url = urls.pres
    else:
        print("Options are `General` or `Presentation`. Please try again.")
        return
    
    #download + save file
    template = requests.get(url)
    if path[-1] == "/":
        open(f"{path}{file_name}","wb").write(template.content)
    else:
        open(f"{path}/{file_name}","wb").write(template.content)
        
#download file from url
def url_download(url,path,file_name):
    """Download file from url.

    Args:
        url (str): Link of item to download.
        path (str): Path to store file. Exclude file name. `/` is optional.
        file_name (str): Name of file. Include extension.
    """
    
    file = requests.get(url)
    if path[-1] == "/":
        open(f"{path}{file_name}","wb").write(file.content)
    else:
        open(f"{path}/{file_name}","wb").write(file.content)