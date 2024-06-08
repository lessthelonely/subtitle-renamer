import os

def get_subtitle_language(filename):
    print(filename.lower())
    if 'english' in filename.lower() or 'none' in filename.lower() or '.en' in filename.lower():
        return '.en'
    elif 'portuguese' in filename.lower() or '.pt' in filename.lower():
        return '.pt'
    return '.en'
    

def rename_files_to_folder_name(root_directory):
    # Walk through the root directory
    for dirpath, dirnames, filenames in os.walk(root_directory):
        # Get the folder name
        folder_name = os.path.basename(dirpath)
        
        # Rename each file in the directory
        counter = 1
        for filename in filenames:
            # Get the file extension
            file_extension = os.path.splitext(filename)[1]
            # Construct the new file name
            new_filename = f"{folder_name.replace('./Subs/', '')}{counter}{get_subtitle_language(filename)}{file_extension}"
            new_filename = new_filename.replace('None', '')

            while os.path.isfile(new_filename):
                counter += 1
                new_filename = f"{folder_name.replace('./Subs/', '').replace('None', '')}{counter}{get_subtitle_language(filename)}{file_extension}"

            # Get the full path to the current file
            old_file_path = os.path.join(dirpath, filename)
            # Get the full path to the new file
            new_file_path = os.path.join(dirpath, new_filename)
            
            # Rename the file
            try:
                os.rename(old_file_path, new_file_path)
            except Exception as e:
                print(f"Failed to rename {old_file_path}: {e}")

# Example usage
root_directory = './Subs/'
rename_files_to_folder_name(root_directory)

