import sys
from typing import List, Self
from os import listdir, getcwd
from os.path import isfile, join, dirname, basename
from enum import Enum

from folder_tree_scanner import get_master_folder_tree
from folder_tree_visualizer import print_master_folder_tree

def main():
    # Using hardcoded for now
    default_path = "C:\\Work\\Work_files\\Trivy"
    # default_path = getcwd()

    folder_tree = get_master_folder_tree(default_path)
    
    print_master_folder_tree(folder_tree)
        
if __name__ == "__main__":
    main()