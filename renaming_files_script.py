import os

# Define the old and new strings in names
directory = input("directory (default is C:\dev\jaar) =")
if directory == "":
    directory = "C:\dev\jaar"

old_string = input("old_string=")
new_string = input("new_string=")

# List of file extensions to consider
file_extensions = [".py", ".json"]


def rename_files_and_folders(directory):
    for root, dirs, files in os.walk(directory):
        # Rename directories
        for d in dirs:
            old_dir_path = os.path.join(root, d)
            new_dir_name = d.replace(old_string, new_string)
            new_dir_path = os.path.join(root, new_dir_name)
            if old_dir_path != new_dir_path:
                os.rename(old_dir_path, new_dir_path)
                print(f"{old_string=} {new_string=} {new_dir_path=}")

        # Rename files
        for file in files:
            if any(file.endswith(ext) for ext in file_extensions):
                old_file_path = os.path.join(root, file)
                new_file_name = file.replace(old_string, new_string)
                new_file_path = os.path.join(root, new_file_name)
                if old_file_path != new_file_path:
                    os.rename(old_file_path, new_file_path)
                    print(f"{old_string=} {new_string=} {new_file_path=}")


if __name__ == "__main__":
    rename_files_and_folders(directory)
    print(f"{directory=} 1st File and folder renaming complete.")
    rename_files_and_folders(directory)
    print(f"{directory=} 2nd File and folder renaming complete.")
    rename_files_and_folders(directory)
    print(f"{directory=} 3rd File and folder renaming complete.")
    rename_files_and_folders(directory)
    print(f"{directory=} 4th File and folder renaming complete.")
