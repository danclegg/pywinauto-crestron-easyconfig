#####
#
# Title: loadProgram.py
# Author: Dan Clegg
# Copyright: 2016, Dan Clegg
# LICENSE: Apache 2.0
#
#####
import sys
import argparse
import csv
import glob,os
import string

from pywinauto.application import Application
#import re

parser = argparse.ArgumentParser(description='')
parser.add_argument('--csv')

args = parser.parse_args()
csvFile = args.csv
hosts = {}

projectDir=os.path.abspath(os.getcwd())

import csv
with open(csvFile, 'r') as f:
    reader = csv.reader(f)
    hosts = dict((rows[0].strip(),rows[1].strip()) for rows in reader)

for key in hosts.iterkeys():
    app = Application().Start(cmd_line=u'"C:\\Program Files (x86)\\Crestron\\Toolbox\\Toolbox.exe" ')
    installerstoolboxappclass = app.InstallersToolboxAppClass
    installerstoolboxappclass.Wait('ready', timeout=30)
    button = installerstoolboxappclass.Button2
    button.Click()

    editWindow = app.Window_(title="Edit Address")
    editWindow.Wait('ready',timeout=30).TypeKeys(hosts[key]).TypeKeys('{ENTER}')
    #wineditAddressWindowdow.Wait('ready', timeout=30)

    #window.TypeKeys("{TAB 5}")
    #window.TypeKeys("{SPACE}")
    app.top_window_().DrawOutline()

    app.Kill_()
