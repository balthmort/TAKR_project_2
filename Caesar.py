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

    param.show()
