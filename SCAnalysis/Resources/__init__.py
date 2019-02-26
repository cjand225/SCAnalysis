import os, sys

# UI file Dir
resourceDir = os.path.abspath(os.path.join(__file__, "."))
uiDir = os.path.abspath(os.path.join(resourceDir, "../UI"))
docDir = os.path.abspath(os.path.join(resourceDir, "../Docs"))

mainUIPath = os.path.join(uiDir, 'MainWindow.ui')
logUIPath = os.path.join(uiDir, 'LogWidget.ui')
quitDialogUIPath = os.path.join(uiDir, 'QuitDialog.ui')
helpDialogUIPath = os.path.join(uiDir, 'HelpDialog.ui')

# Documentation reference paths

aboutDocPath = os.path.join(docDir, "About.md")
adminDocPath = os.path.join(docDir, "AdminManual.md")
userDocPath = os.path.join(docDir, "UserManual.md")
