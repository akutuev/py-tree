from os import getcwd
import sys

from folder_tree_scanner import get_master_folder_tree
from folder_tree_visualizer import visualize_in_console

def main():
    default_path = sys.argv[1] if len(sys.argv) > 1 else getcwd()

    folder_tree = get_master_folder_tree(default_path)
    visualize_in_console(folder_tree)
        
if __name__ == "__main__":
    main()