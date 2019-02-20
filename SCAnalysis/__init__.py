from SCAnalysis.Logging import logPath, logDir
from SCAnalysis.Logging.Log import initLog
from SCAnalysis.System.FileSystem import dirExists, makeDir

import logging, os

pkgName = "SCAnalysis"

# check if dir exists, if not create it
if not dirExists(logPath):
    makeDir(logDir)

# create log
initLog(pkgName, logging.DEBUG)
