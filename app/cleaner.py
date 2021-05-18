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
        self.cleanFolder(path)
    
    def cleanFolder(self, path):
        """ This function cleans the folder """
        try:
            for fileName in os.listdir(path):
                fileNamePath = os.path.join(path + "//", fileName)
                if os.path.isfile(fileNamePath):
                    os.unlink(fileNamePath)
                    print(f"File: {fileName} cleaned")
                else:
                    shutil.rmtree(fileNamePath)
            print("Folder cleaned successfully")
        except FileNotFoundError:
            print("The specified path could not be found")

if __name__ == "__main__":
    cleaner = Core(args.path)
    