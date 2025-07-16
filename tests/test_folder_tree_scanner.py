from pathlib import Path
from app.folder_tree_scanner import DirectoryItem, DirectoryType, get_master_folder_tree

def test_get_master_folder_tree_with_nested_dirs_and_files(tmp_path: Path):
    structure = [
        "dir_1",
            "dir_1/dir_1_1",
                "dir_1/dir_1_1/file.txt",
        "dir_2",
            "dir_2/dir_2_1",
            "dir_2/dir_2_2",
        "file.txt",
    ]

    create_test_structure(tmp_path, structure)

    master_directory = get_master_folder_tree(tmp_path)
    sorted_master_child_items = sorted(master_directory.child_items, key=lambda item: item.name)

    assert master_directory.type == DirectoryType.FOLDER

    assert sorted_master_child_items[0].name == "dir_1"
    assert sorted_master_child_items[0].type == DirectoryType.FOLDER

    assert sorted_master_child_items[0].child_items[0].name == "dir_1_1"
    assert sorted_master_child_items[0].type == DirectoryType.FOLDER

    assert sorted_master_child_items[0].child_items[0].child_items[0].name == "file.txt"
    assert sorted_master_child_items[0].child_items[0].child_items[0].type == DirectoryType.FILE

    assert sorted_master_child_items[1].name == "dir_2"
    assert sorted_master_child_items[1].type == DirectoryType.FOLDER

    assert sorted_master_child_items[1].child_items[0].name == "dir_2_1"
    assert sorted_master_child_items[1].child_items[0].type == DirectoryType.FOLDER
    assert sorted_master_child_items[1].child_items[1].name == "dir_2_2"
    assert sorted_master_child_items[1].child_items[1].type == DirectoryType.FOLDER

    assert sorted_master_child_items[2].name == "file.txt"
    assert sorted_master_child_items[2].type == DirectoryType.FILE


def test_get_master_folder_tree_with_only_files(tmp_path: Path):
    structure = [
        "file.txt",
        "file_1.txt",
        "file_2.txt",
    ]

    create_test_structure(tmp_path, structure)

    master_directory = get_master_folder_tree(tmp_path)
    sorted_master_child_items = sorted(master_directory.child_items, key=lambda item: item.name)


    assert sorted_master_child_items[0].name == "file.txt"
    assert sorted_master_child_items[0].type == DirectoryType.FILE

    assert sorted_master_child_items[1].name == "file_1.txt"
    assert sorted_master_child_items[1].type == DirectoryType.FILE

    assert sorted_master_child_items[2].name == "file_2.txt"
    assert sorted_master_child_items[2].type == DirectoryType.FILE

def create_test_structure(tmp_path: Path, structure: list[str]):
    for item in structure:
        if item.endswith(".txt"):
            (tmp_path / item).parent.mkdir(parents=True, exist_ok=True)
            (tmp_path / item).touch()
        else:
            (tmp_path / item).mkdir(parents=True, exist_ok=True)