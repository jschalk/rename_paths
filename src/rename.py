from os import rename as os_rename, walk as os_walk
from os.path import join as os_path_join


def rename_files_and_folders_4times(directory: str, old_string: str, new_string: str):
    rename_files_and_folders(directory, old_string, new_string)
    rename_files_and_folders(directory, old_string, new_string)
    rename_files_and_folders(directory, old_string, new_string)
    rename_files_and_folders(directory, old_string, new_string)


def rename_files_and_folders(directory: str, old_string: str, new_string: str):
    new_string = new_string.lower()
    old_string = old_string.lower()

    for root, dirs, files in os_walk(directory):
        # Rename directories
        for d in dirs:
            old_dir_path = os_path_join(root, d)
            new_dir_name = d.replace(old_string, new_string)
            new_dir_path = os_path_join(root, new_dir_name)
            if old_dir_path != new_dir_path:
                os_rename(old_dir_path, new_dir_path)
                print(f"{old_string=} {new_string=} {new_dir_path=}")

        # List of file extensions to consider
        file_extensions = [".py", ".json"]
        # Rename files
        for file_name in files:
            if any(file_name.endswith(ext) for ext in file_extensions):
                file_name = file_name.lower()
                old_file_path = os_path_join(root, file_name)
                new_file_name = file_name.replace(old_string, new_string)
                new_file_path = os_path_join(root, new_file_name)
                if old_file_path != new_file_path:
                    os_rename(old_file_path, new_file_path)
                    print(f"{old_string=} {new_string=} {new_file_path=}")
