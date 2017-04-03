#!/usr/bin/env python3
# Author:   Petr Surý
# Date:     7.3.2017, 26.3.2017
# File:     Caesar.py
# Project:  TAKR project 2

import sys
from my_lib import param_parser
from my_lib import encrypt
from my_lib import decrypt
from my_lib import check_params

if __name__ == "__main__":
    sys.stderr.write("Beginning execution\n")
    param = param_parser.ParseParams()

    param.show()
    checked_params = check_params.CheckParams(param.args)

    if(param.args.subparser == "encrypt"):
        sys.stderr.write("Encrypt\n")
        encrypt.EncryptCaesar(
                checked_params.input_file,
                checked_params.output_file,
                checked_params.key)
    elif(param.args.subparser == "decrypt"):
        sys.stderr.write("Decrypt\n")
        decrypt.DecryptCaesar(
                checked_params.input_file,
                checked_params.output_file)
    elif(param.args.subparser == "test"):
        sys.stderr.write("Decrypt test\n")
    else:
        sys.stderr.write("Print help\n")
