from pathlib import Path
from app.folder_tree_scanner import DirectoryType, get_master_folder_tree

def test_get_master_folder_tree(tmp_path: Path):
    structure = [
        "dir_1",
            "dir_1/dir_1_1",
                "dir_1/dir_1_1/file.txt",
        "dir_2",
            "dir_2/dir_2_1",
            "dir_2/dir_2_2",
        "file.txt",
    ]

    for item in structure:
        if item.endswith(".txt"):
            (tmp_path / item).parent.mkdir(parents=True, exist_ok=True)
            (tmp_path / item).touch()
        else:
            (tmp_path / item).mkdir()
            
    masterDirectory = get_master_folder_tree(tmp_path)
    
    assert masterDirectory.child_items[0].name == "dir_1"
    assert masterDirectory.child_items[0].type == DirectoryType.FOLDER

    assert masterDirectory.child_items[0].child_items[0].name == "dir_1_1"
    assert masterDirectory.child_items[0].type == DirectoryType.FOLDER

    assert masterDirectory.child_items[0].child_items[0].child_items[0].name == "file.txt"
    assert masterDirectory.child_items[0].child_items[0].child_items[0].type == DirectoryType.FILE

    assert masterDirectory.child_items[1].name == "dir_2"
    assert masterDirectory.child_items[1].type == DirectoryType.FOLDER

    assert masterDirectory.child_items[1].child_items[0].name == "dir_2_1"
    assert masterDirectory.child_items[1].child_items[0].type == DirectoryType.FOLDER
    assert masterDirectory.child_items[1].child_items[1].name == "dir_2_2"
    assert masterDirectory.child_items[1].child_items[1].type == DirectoryType.FOLDER

    assert masterDirectory.child_items[2].name == "file.txt"
    assert masterDirectory.child_items[2].name == DirectoryType.FILE

