import os, logging

pkgName = "SCAnalysis"
logFile = pkgName + ".log"
logDir = os.path.abspath(os.path.join(".", "./../../Settings/Logs"))
logPath = os.path.abspath(os.path.join(logDir, logFile))
logDefaultFormat = logging.Formatter('[%(asctime)s] - [%(name)s] - [%(levelname)s] - %(message)s')
