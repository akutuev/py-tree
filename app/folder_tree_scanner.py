from dataclasses import dataclass
from typing import Self
from os import listdir
from os.path import isdir, join, basename
from enum import Enum

class DirectoryType(Enum):
    FILE = "file"
    FOLDER = "folder"

    def __str__(self):
        return self.value
    
@dataclass        
class DirectoryItem:
    name: str
    type: DirectoryType
    child_items: list[Self]

def get_master_folder_tree(path: str) -> DirectoryItem:
    return DirectoryItem(
        name=basename(path),
        type=DirectoryType.FOLDER,
        child_items=_get_folder_childs(path)
    )

def _get_folder_childs(path: str) -> list[DirectoryItem]:
    child_items = []
    for child_item_name in listdir(path):
        child_full_path = join(path, child_item_name)
        child_type = DirectoryType.FOLDER if isdir(child_full_path) else DirectoryType.FILE
        items = _get_folder_childs(child_full_path) if child_type is DirectoryType.FOLDER else []

        child_item = DirectoryItem(child_item_name, child_type, items)
        child_items.append(child_item)
    return child_items 