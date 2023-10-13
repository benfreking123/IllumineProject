import os
import shutil


def copy_selected(src_dir, dest_dir, folder_list, file_list, files_to_ignore):
    """
    Copy selected folders and files from src_dir to dest_dir, ignoring specific files.

    :param src_dir: Source directory
    :param dest_dir: Destination directory
    :param folder_list: List of folders to be copied
    :param file_list: List of files to be copied
    :param files_to_ignore: List of files to be ignored during copying
    """

    # Check if source directory exists
    if not os.path.exists(src_dir):
        print(f"Source directory '{src_dir}' does not exist.")
        return

    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Iterate over the items in the source directory
    for item_name in os.listdir(src_dir):
        # Construct the full path
        item_path = os.path.join(src_dir, item_name)
        dest_path = os.path.join(dest_dir, item_name)

        # If it's a directory and its name is in the folder list, copy it
        if os.path.isdir(item_path) and item_name in folder_list:
            # If the destination folder exists, delete it
            if os.path.exists(dest_path):
                shutil.rmtree(dest_path)
                print(f"Deleted old version of folder {item_name} in {dest_dir}")

            # Copy directory without files to ignore
            # This creates the top directory of the folder we're copying, so we can copy its subcontents selectively
            os.makedirs(dest_path)

            for root, dirs, files in os.walk(item_path):
                for name in files:
                    if name not in files_to_ignore:
                        source_file = os.path.join(root, name)
                        # Maintain the folder structure in the destination
                        relative_path = os.path.relpath(root, item_path)
                        dest_file_folder = os.path.join(dest_path, relative_path)
                        dest_file = os.path.join(dest_file_folder, name)

                        # If folder doesn't exist, create it
                        if not os.path.exists(dest_file_folder):
                            os.makedirs(dest_file_folder)

                        shutil.copy2(source_file, dest_file)
                # You can also extend this to ignore entire subdirectories if needed
            print(f"Copied folder {item_name} to {dest_path} (ignoring files from the ignore list)")

        # If it's a file and its name is in the file list, copy it
        elif os.path.isfile(item_path) and item_name in file_list:
            # If the destination file exists, delete it
            if os.path.exists(dest_path):
                os.remove(dest_path)
                print(f"Deleted old version of file {item_name} in {dest_dir}")
            shutil.copy2(item_path, dest_path)
            print(f"Copied file {item_name} to {dest_path}")


if __name__ == "__main__":
    SOURCE_DIR = 'Spirituality'
    DESTINATION_DIR = 'content'
    FOLDERS_TO_COPY = ['- Abilities', '- Classes', '- Individuals', '- Items', '- Journal', '- Places', '- Stories']
    FILES_TO_COPY = ['Home.md', 'Fundamental Forces.md']
    FILES_TO_IGNORE = ['Zarda.md', 'ignore2.md']  # Add filenames you want to ignore

    copy_selected(SOURCE_DIR, DESTINATION_DIR, FOLDERS_TO_COPY, FILES_TO_COPY, FILES_TO_IGNORE)
