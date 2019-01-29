import logging, os

from SCAnalysis.Logging.Log import *
from SCAnalysis.System.FileSystem import *

pkgName = "SCAnalysis"
logFile = pkgName + ".log"

logDir = os.path.abspath(os.path.join(__file__, "./../../settings/logs"))
logPath = os.path.abspath(os.path.join(logDir, logFile))

# check if dir exists, if not create it
if not dirExists(logPath):
    makeDir(logPath)

# if file exists, create new log file instead of appending
if not fileExists(logPath):
    print("")