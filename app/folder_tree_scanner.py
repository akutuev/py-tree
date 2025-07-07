from typing import List, Self
from os import listdir
from os.path import isdir, join, basename
from enum import Enum

class DirectoryType(Enum):
    FILE = "file"
    FOLDER = "folder"

    def __str__(self):
        return self.value

class DirectoryItem:
    name: str
    type: DirectoryType
    child_items: List[Self] = []

    def __init__(self, name, type, child_items):
        self.name = name
        self.type = type
        self.child_items = child_items

def get_master_folder_tree(path: str) -> DirectoryItem:
    return DirectoryItem(
        name=basename(path),
        type=DirectoryType.FOLDER,
        child_items=_get_folder_childs(path)
    )

def _get_folder_childs(path: str) -> List[DirectoryItem]:
    child_items = []
    for child_item_name in listdir(path):
        child_full_path = join(path, child_item_name)
        child_type = DirectoryType.FOLDER if isdir(child_full_path) else DirectoryType.FILE

        child_item = DirectoryItem(
           name=child_item_name, 
           type=child_type,
           child_items = _get_folder_childs(child_full_path) if child_type is DirectoryType.FOLDER else []
        )

        child_items.append(child_item)
    return child_items 