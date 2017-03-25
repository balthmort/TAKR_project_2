#!/usr/bin/env python3
# Author:   Petr Surý
# Data:     7.3.2017
# File:     Caesar.py
# Project:  TAKR project 2

import sys
from my_lib import param_parser

if __name__ == "__main__":
    sys.stderr.write("Beginning execution\n")
    param = param_parser.ParseParams()

    if param.args.subparser is not None:
        sys.stderr.write("Show params\n")
        print("Input file:\t" + param.args.file)
        print("Output file:\t" + param.args.output)
        print("Key file:\t" + param.args.key_file)
        if param.args.subparser != "decrypt":
            print("Shift key\t" + param.args.shift_key)
