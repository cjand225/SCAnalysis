import os, sys

# UI file Dir
resourceDir = os.path.abspath(os.path.join(__file__, "../UI"))

mainUIPath = os.path.join(resourceDir, 'MainWindow.ui')
logUIPath = os.path.join(resourceDir, 'LogWidget.ui')
quitDialogUIPath = os.path.join(resourceDir, 'QuitDialog.ui')
helpDialogUIPath = os.path.join(resourceDir, 'HelpDialog.ui')
