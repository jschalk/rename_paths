from os import rename as os_rename, walk as os_walk
from os.path import join as os_path_join


def rename_files_and_folders_4times(directory: str, old_string: str, new_string: str):
    rename_files_and_folders(directory, old_string, new_string)
    rename_files_and_folders(directory, old_string, new_string)
    rename_files_and_folders(directory, old_string, new_string)
    rename_files_and_folders(directory, old_string, new_string)


def rename_files_and_folders(
    directory: str, old_string: str, new_string: str
) -> list[str]:
    # new_string = new_string.lower()
    # old_string = old_string.lower()
    alert_messages = []

    for root, dirs, files in os_walk(directory):
        # Rename directories
        for d in dirs:
            old_dir_path = os_path_join(root, d)
            new_dir_name = d.replace(old_string, new_string)
            new_dir_path = os_path_join(root, new_dir_name)
            if old_dir_path != new_dir_path:
                os_rename(old_dir_path, new_dir_path)
                print(f"{old_string=} {new_string=} {new_dir_path=}")
            else:
                lower_new_string = new_string.lower()
                lower_old_string = old_string.lower()
                lower_new_dir_name = d.replace(lower_old_string, lower_new_string)
                lower_new_dir_path = os_path_join(root, lower_new_dir_name)
                if old_dir_path != lower_new_dir_path:
                    alert_messages.append("huh")

        # List of file extensions to consider
        file_extensions = [".py", ".json"]
        # Rename files
        for file_name in files:
            if any(file_name.endswith(ext) for ext in file_extensions):
                old_file_path = os_path_join(root, file_name)
                new_file_name = file_name.replace(old_string, new_string)
                new_file_path = os_path_join(root, new_file_name)
                if old_file_path != new_file_path:
                    os_rename(old_file_path, new_file_path)
                else:
                    lower_new_string = new_string.lower()
                    lower_old_string = old_string.lower()
                    lower_file_name = file_name.lower()
                    lower_new_file_name = lower_file_name.replace(
                        lower_old_string, lower_new_string
                    )
                    lower_new_file_path = os_path_join(root, lower_new_file_name)
                    print(f"{old_file_path=} {lower_new_file_path=}")
                    if old_file_path != lower_new_file_path:
                        alert_messages.append(f"File that was not renamed: {file_name}")

    for alert_message in alert_messages:
        print(alert_message)
    return alert_messages
