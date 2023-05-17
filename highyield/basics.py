#import modules
import os

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