import os
import re

def bulk_rename_folders(root_dir):
    # Iterate through all folders and files in the root directory
    for root, dirs, files in os.walk(root_dir):
        for folder in dirs:
            # Check if the folder name contains square brackets and extract series name
            match = re.match(r'(.*)\[.*?\](.*)', folder)
            if match:
                old_name = os.path.join(root, folder)
                # Remove anything within square brackets
                series_name = re.sub(r'\[.*?\]', '', folder).strip()
                # Construct the new name
                new_name = os.path.join(root, series_name)
                # If the new name already exists, append a number to it
                counter = 1
                while os.path.exists(new_name):
                    new_name = os.path.join(root, f"{series_name} ({counter})")
                    counter += 1
                # Rename the folder
                os.rename(old_name, new_name)
                print(f'Renamed "{old_name}" to "{new_name}"')

# Get the directory where the script is located
script_directory = os.path.dirname(__file__)
bulk_rename_folders(script_directory)
