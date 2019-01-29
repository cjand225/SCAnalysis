import logging, datetime

'''  
    Function: initLog
    Parameters: N/A
    Return Value: N/A
    Purpose: Initializes the functions necessary for setup of logging.
'''


def initLog(name, logLevel):
    infoLog = logging.getLogger(name)
    infoLog.setLevel(logLevel)


'''  
    Function: getLog
    Parameters: N/A
    Return Value: Logging.Logger
    Purpose: Returns the Global log to be used where ever it may be invoked.
'''


def getLog(name):
    return logging.getLogger(name)


'''  
    Function: getLogName
    Parameters: N/A
    Return Value: str
    Purpose: Returns the current system date at time of invoke as the name for the current session log.
'''


def getlogName():
    return str(datetime.datetime.now())
