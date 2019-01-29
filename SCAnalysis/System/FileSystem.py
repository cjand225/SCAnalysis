import os

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


def createFile(path, arg):
    if not fileExists(path):
        fp = open(path, arg)
        fp.close()
