from typing import List
from folder_tree_scanner import DirectoryItem


def visualize_in_console(item: DirectoryItem):
    print(f"Master folder: {item.name}")
    _visualize_folder_child_items(item)


def _visualize_folder_child_items(item: DirectoryItem, level = 0):
    level_indent = "  " * level
    if item.child_items:
        for child_item in item.child_items:
            print(f"{level_indent}|──{child_item.name} ({child_item.type})")

            next_level = level + 1
            _visualize_folder_child_items(child_item, next_level)