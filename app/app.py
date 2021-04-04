import sys, os, shutil

class Core:
    def __init__(self, path):
        """ Constructor """
        super().__init__()
        self.cleanFolder(path)
    
    def cleanFolder(self, path):
        """ This function cleans the folder """
        try:
            for fileName in os.listdir(path):
                fileNamePath = os.path.join(path + "\\", fileName)
                if os.path.isfile(fileNamePath):
                    os.unlink(fileNamePath)
                else:
                    shutil.rmtree(fileNamePath)
        except FileNotFoundError:
            print("The specified path could not be found")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        a = Core(sys.argv[1])
    else:
        print("Remember that you can only enter one argument and it must be a valid directory")
    