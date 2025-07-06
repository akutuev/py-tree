from typing import List
from folder_tree_scanner import DirectoryItem


def print_master_folder_tree(item: DirectoryItem):
    print(f"Master folder: {item.name}")
    _visualize_folder_child_items(item.child_items)


def _visualize_folder_child_items(child_items: List[DirectoryItem], level = 0):
    level_indent = "  " * level
    for child_item in child_items:
        print(f"{level_indent}|──{child_item.name} ({child_item.type})")

        next_level = level + 1
        _visualize_folder_child_items(child_item, next_level)