#!/usr/bin/env/python

import os


modules = ["login"]


for module in modules:
    os.chdir(module)
    os.system("python " + module + "_test_suite.py")
    os.chdir("..")
