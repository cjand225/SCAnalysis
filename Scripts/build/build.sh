#!/usr/bin/env bash
# set seed to a known repeatable integer value
PYTHONHASHSEED=1
export PYTHONHASHSEED
pyinstaller --clean --windowed --workpath=../../bin/ --distpath=../../bin/ PyInstaller.spec
# make checksum
cksum ./../../bin/SCAnalysis/SCA | awk '{print $1}' > ./dist/SCA.checksum
# let Python be unpredictable again
unset PYTHONHASHSEED