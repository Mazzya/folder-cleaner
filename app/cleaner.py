import sys
import os
import shutil
import argparse

parser = argparse.ArgumentParser(description="Clean folders quickly")
parser.add_argument('-p', '--path', type=str, metavar='', required=True, help="Folder path to clean")
args = parser.parse_args()


class Core:
    def __init__(self, path):
        """ Constructor """
        self.clean_folder(path)
    
    def clean_folder(self, path):
        """ This function cleans the folder """
        try:
            for file_name in os.listdir(path):
                file_name_path = os.path.join(path + "//", file_name)
                if os.path.isfile(file_name_path):
                    os.unlink(file_name_path)
                else:
                    shutil.rmtree(file_name_path)
            print("Folder cleaned successfully")
        except FileNotFoundError:
            print("The specified path could not be found")

if __name__ == "__main__":
    cleaner = Core(args.path)
    