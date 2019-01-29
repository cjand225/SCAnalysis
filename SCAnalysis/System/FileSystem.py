import os, csv

'''  
    Function: makeDir
    Parameters: dirName
    Return Value: Boolean cond
    Purpose: Checks if the logging path exists and if not makes the directory to complete the path.
'''


def makeDir(dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    return True


'''  
    Function: dirExists
    Parameters: dirName (str)
    Return Value: Boolean cond
    Purpose: Returns a boolean cond that determines whether a directory exists or not.
'''


def dirExists(dirName):
    return os.path.exists(dirName)


'''  
    Function: fileExists
    Parameters: path (str)
    Return Value: Boolean cond
    Purpose: Returns a boolean cond that determines whether a file exists or not.
'''


def fileExists(path):
    return os.path.isfile(path)


'''  
    Function: createFile
    Parameters: path (str), args (str)
    Return Value: 
    Purpose: Creates a file with provided path and arguments.
'''


def createFile(path, arg, data):
    if not fileExists(path):
        fp = open(path, arg)
        for dataLine in data:
            if arg == "w":
                fp.write(dataLine)
            else:
                fp.read(dataLine)
        fp.close()


'''  
    Function: exportImage
    Parameters: path (str), img (image file)
    Return Value: Boolean Cond
    Purpose: Exports a graph image from application to path given by user.
'''


def exportImage(path, img):
    print()


'''  
    Function: importCSV
    Parameters: path (str)
    Return Value: List with CSV contents
    Purpose: Imports the file given by the path parameter of a CSV and returns it as a list.
'''


def importCSV(path):
    print()
