from src.rename import rename_files_and_folders

# Define the old and new strings in names
directory = input("directory (default is C:\dev\jaar) =")
if directory == "":
    directory = "C:\dev\jaar"

old_string = input("old_string=")
new_string = input("new_string=")


if __name__ == "__main__":
    rename_files_and_folders(directory, old_string, new_string)
    print(f"{directory=} 1st File and folder renaming complete.")
    rename_files_and_folders(directory, old_string, new_string)
    print(f"{directory=} 2nd File and folder renaming complete.")
    rename_files_and_folders(directory, old_string, new_string)
    print(f"{directory=} 3rd File and folder renaming complete.")
    rename_files_and_folders(directory, old_string, new_string)
    print(f"{directory=} 4th File and folder renaming complete.")
