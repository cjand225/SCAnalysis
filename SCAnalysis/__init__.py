from SCAnalysis.Logging.Log import initLog
from SCAnalysis.System.FileSystem import dirExists, makeDir

import logging, os

pkgName = "SCAnalysis"
logFile = pkgName + ".log"

logDir = os.path.abspath(os.path.join(__file__, "./../../Settings/Logs"))
logPath = os.path.abspath(os.path.join(logDir, logFile))

# check if dir exists, if not create it
if not dirExists(logPath):
    makeDir(logDir)

# create log
initLog(pkgName, logging.DEBUG)
