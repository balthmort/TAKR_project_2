#!/usr/bin/env bash python3
# Author:   Petr Surý
# Date:     26.3.2017
# File:     check_params.py
# Project:  TAKR project 2

import sys
import os


class CheckParams(object):
    # {{{
    input_file = None
    output_file = None
    key = None

    def __init__(self, args):
        # {{{
        sys.stderr.write("Check params\n")

        if args.subparser is not None:
            self.input_file = self.check_input_file(args.input_file)
            self.output_file = self.check_output_file(args.output_file)
            if args.subparser == "decrypt":
                self.key = self.check_key(
                                args.key_file, None, args.subparser)
            else:
                self.key = self.check_key(
                                args.key_file, args.shift_key, args.subparser)

        # }}}

    def check_input_file(self, file):
        # {{{
        sys.stderr.write("Checking input file: " + file + "\n")
        if not os.path.isfile(file):
            sys.stdout.write(
                "Input file error\nRestart program with correct input file\n")
            sys.exit(1)
        else:
            return file
        # }}}

    def check_output_file(self, file):
        # {{{
        sys.stderr.write("Checking output file: " + file + "\n")
        if os.path.isfile(file):
            sys.stdout.write("Output file exists and will be rewritten\n")
        return file
        # }}}

    def check_key(self, key_file, shift_key, subparser):
        # {{{
        sys.stderr.write("Checking key/key file\n")
        if subparser == "decrypt":
            sys.stderr.write("Checking key file\n")
            if os.path.isfile(key_file):
                sys.stdout.write(
                        "Output key file exists and will be overwritten\n")
                return key_file
            else:
                return key_file
        elif subparser == "encrypt" or subparser == "test":
            if shift_key is None:
                sys.stderr.write("Checking key file\n")
                if os.path.isfile(key_file):
                    with open(key_file, "r") as key:
                        return int(key.read())
                else:
                    sys.stdout.write(
                        "Key file for encryption does not exist.\
                        \nSpecify key file\n")
                    sys.exit(1)
            else:
                sys.stderr.write("Checking key\n")
                return shift_key
        # }}
    # }}}
