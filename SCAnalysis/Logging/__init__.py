import os, logging

from SCAnalysis.Application import resourcesDir

logUIPath = os.path.join(resourcesDir, 'LogWidget.ui')

logDefaultFormat = logging.Formatter('[%(asctime)s] - [%(name)s] - [%(levelname)s] - %(message)s')
