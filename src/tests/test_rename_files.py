from src.file import (
    dir_files,
    save_file,
    open_file,
    count_files,
    get_directory_path,
    is_path_valid,
    can_active_usser_edit_paths,
    is_path_existent_or_creatable,
    is_path_probably_creatable,
    is_path_existent_or_probably_creatable,
    get_all_dirs_with_file,
    get_integer_filenames,
)
from src.tests.instrument_env import (
    get_instrument_temp_env_dir,
    env_dir_setup_cleanup,
)
from os.path import exists as os_path_exist
from src.rename import rename_files_and_folders, rename_files_and_folders_4times


def test_rename_files_and_folders_NotChangesWhenNoneNeeded(env_dir_setup_cleanup):
    # GIVEN
    env_dir = get_instrument_temp_env_dir()
    dolphin_file_name = "dolphin.txt"
    lopster_file_name = "lopster.txt"
    dolphin_file_text = "trying this"
    lopster_file_text = "look there"
    save_file(env_dir, file_name=dolphin_file_name, file_text=dolphin_file_text)
    save_file(env_dir, file_name=lopster_file_name, file_text=lopster_file_text)
    files_dict = dir_files(dir_path=env_dir)
    assert len(files_dict) == 2
    assert files_dict.get(dolphin_file_name) == dolphin_file_text
    assert files_dict.get(lopster_file_name) == lopster_file_text

    # WHEN
    rename_files_and_folders(env_dir, "Bob", "Sue")

    # THEN
    files_dict = dir_files(dir_path=env_dir)
    assert len(files_dict) == 2
    assert files_dict.get(dolphin_file_name) == dolphin_file_text
    assert files_dict.get(lopster_file_name) == lopster_file_text


def test_rename_files_and_folders_ChangesWhenNeeded_lowercase(env_dir_setup_cleanup):
    # GIVEN
    env_dir = get_instrument_temp_env_dir()
    dolphin_file_name = "dolphin.json"
    lopster_file_name = "lopster.json"
    dolphin_file_text = "trying this"
    lopster_file_text = "look there"
    save_file(env_dir, file_name=dolphin_file_name, file_text=dolphin_file_text)
    save_file(env_dir, file_name=lopster_file_name, file_text=lopster_file_text)
    files_dict = dir_files(dir_path=env_dir)
    assert len(files_dict) == 2
    assert files_dict.get(dolphin_file_name) == dolphin_file_text
    assert files_dict.get(lopster_file_name) == lopster_file_text

    # WHEN
    rename_files_and_folders(env_dir, "dol", "bob")

    # THEN
    files_dict = dir_files(dir_path=env_dir)
    assert len(files_dict) == 2
    assert files_dict.get(dolphin_file_name) is None
    bobphin_file_name = "bobphin.json"
    assert files_dict.get(lopster_file_name) == lopster_file_text
    assert files_dict.get(bobphin_file_name) == dolphin_file_text


def test_rename_files_and_folders_ChangesWhenNeeded_lowercase_parameters(
    env_dir_setup_cleanup,
):
    # GIVEN
    env_dir = get_instrument_temp_env_dir()
    dolphin_file_name = "dolphin.json"
    lopster_file_name = "lopster.json"
    dolphin_file_text = "trying this"
    lopster_file_text = "look there"
    save_file(env_dir, file_name=dolphin_file_name, file_text=dolphin_file_text)
    save_file(env_dir, file_name=lopster_file_name, file_text=lopster_file_text)
    files_dict = dir_files(dir_path=env_dir)
    assert len(files_dict) == 2
    assert files_dict.get(dolphin_file_name) == dolphin_file_text
    assert files_dict.get(lopster_file_name) == lopster_file_text

    # WHEN
    rename_files_and_folders(env_dir, "Dol", "bob")

    # THEN
    files_dict = dir_files(dir_path=env_dir)
    assert len(files_dict) == 2
    assert files_dict.get(dolphin_file_name) is None
    bobphin_file_name = "bobphin.json"
    assert files_dict.get(lopster_file_name) == lopster_file_text
    assert files_dict.get(bobphin_file_name) == dolphin_file_text


def test_rename_files_and_folders_ChangesWhenNeeded_lowercase_filenames(
    env_dir_setup_cleanup,
):
    # GIVEN
    env_dir = get_instrument_temp_env_dir()
    dolphin_file_name = "Dolphin.json"
    lopster_file_name = "lopster.json"
    dolphin_file_text = "trying this"
    lopster_file_text = "look there"
    save_file(env_dir, file_name=dolphin_file_name, file_text=dolphin_file_text)
    save_file(env_dir, file_name=lopster_file_name, file_text=lopster_file_text)
    files_dict = dir_files(dir_path=env_dir)
    assert len(files_dict) == 2
    assert files_dict.get(dolphin_file_name) == dolphin_file_text
    assert files_dict.get(lopster_file_name) == lopster_file_text

    # WHEN
    rename_files_and_folders(env_dir, "dol", "bob")

    # THEN
    files_dict = dir_files(dir_path=env_dir)
    assert len(files_dict) == 2
    assert files_dict.get(dolphin_file_name) is None
    bobphin_file_name = "bobphin.json"
    assert files_dict.get(lopster_file_name) == lopster_file_text
    assert files_dict.get(bobphin_file_name) == dolphin_file_text


def test_rename_files_and_folders_ChangesWhenNeeded_directory(
    env_dir_setup_cleanup,
):
    # GIVEN
    env_dir = get_instrument_temp_env_dir()
    dolphine_text = "dolphin"
    dolphin_dir = f"{env_dir}/{dolphine_text}"
    dolphin_file_name = f"{dolphine_text}.json"
    lopster_file_name = "lopster.json"
    dolphin_file_text = "trying this"
    lopster_file_text = "look there"
    save_file(dolphin_dir, dolphin_file_name, file_text=dolphin_file_text)
    save_file(dolphin_dir, lopster_file_name, file_text=lopster_file_text)
    dolphin_files_dict = dir_files(dolphin_dir)
    assert len(dolphin_files_dict) == 2
    assert dolphin_files_dict.get(dolphin_file_name) == dolphin_file_text
    assert dolphin_files_dict.get(lopster_file_name) == lopster_file_text
    bobphin_text = "bobphin"
    bobphin_dir = f"{env_dir}/{bobphin_text}"
    assert os_path_exist(dolphin_dir)
    assert os_path_exist(bobphin_dir) == False

    # WHEN
    rename_files_and_folders_4times(env_dir, "dol", "bob")

    # THEN
    bobphin_files_dict = dir_files(bobphin_dir)
    assert len(bobphin_files_dict) == 2
    assert bobphin_files_dict.get(dolphin_file_name) is None
    bobphin_file_name = f"{bobphin_text}.json"
    assert bobphin_files_dict.get(lopster_file_name) == lopster_file_text
    assert bobphin_files_dict.get(bobphin_file_name) == dolphin_file_text
    assert os_path_exist(dolphin_dir) == False
    assert os_path_exist(bobphin_dir)


def test_rename_files_and_folders_ChangesWhenNeeded_delete_old_directorys(
    env_dir_setup_cleanup,
):
    # GIVEN
    env_dir = get_instrument_temp_env_dir()
    dolphine_text = "dolphin"
    dolphin_dir = f"{env_dir}/{dolphine_text}"
    dolphin_file_name = f"{dolphine_text}.json"
    lopster_file_name = "lopster.json"
    dolphin_file_text = "trying this"
    lopster_file_text = "look there"
    save_file(dolphin_dir, dolphin_file_name, file_text=dolphin_file_text)
    save_file(dolphin_dir, lopster_file_name, file_text=lopster_file_text)
    save_file(dolphin_dir, "penguin.txt", file_text="huh")
    dolphin_files_dict = dir_files(dolphin_dir)
    assert len(dolphin_files_dict) == 3
    assert dolphin_files_dict.get(dolphin_file_name) == dolphin_file_text
    assert dolphin_files_dict.get(lopster_file_name) == lopster_file_text
    bobphin_text = "bobphin"
    bobphin_dir = f"{env_dir}/{bobphin_text}"
    assert os_path_exist(dolphin_dir)
    assert os_path_exist(bobphin_dir) == False

    # WHEN
    rename_files_and_folders_4times(env_dir, "dol", "bob")

    # THEN
    bobphin_files_dict = dir_files(bobphin_dir)
    assert len(bobphin_files_dict) == 3
    assert bobphin_files_dict.get(dolphin_file_name) is None
    bobphin_file_name = f"{bobphin_text}.json"
    assert bobphin_files_dict.get(lopster_file_name) == lopster_file_text
    assert bobphin_files_dict.get(bobphin_file_name) == dolphin_file_text
    assert os_path_exist(dolphin_dir) == False
    assert os_path_exist(bobphin_dir)
