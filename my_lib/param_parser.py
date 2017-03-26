#!/usr/bin/env python3
# author:   Petr Surý
# Date:     23.3.2017
# File:     param_parser.py
# Project:  TAKR project 2

import argparse
import sys


class ParseParams(object):
    # {{{
    args = None

    def __init__(self):
        # {{{
        # Create top-level parser
        parser = argparse.ArgumentParser(
                prog="TAKR Project 2",
                description='''
                TAKR - Project 2
                Script for encrypting/decrypting text file with Caesar cipher
                ''')

        # Create subparsers
        subparsers = parser.add_subparsers(
                dest="subparser",
                title="subcommands",
                description="Test decrypt with key or encrypt/decrypt file",
                help="additional help")

        # Create parent parser
        base_parser = argparse.ArgumentParser(add_help=False)

        self.parseParams(parser, base_parser, subparsers)
        # }}}

    def show(self):
        # {{{
        if self.args.subparser is not None:
            sys.stderr.write("Show params\n")
            sys.stderr.write("Input file:\t" + self.args.file + "\n")
            sys.stderr.write("Output file:\t" + self.args.output + "\n")
            sys.stderr.write("Key file:\t" + str(self.args.key_file) + "\n")
            if self.args.subparser != "decrypt":
                sys.stderr.write("Shift key\t" +
                                 str(self.args.shift_key) + "\n")
        # }}}

    def parseParams(self, parser, base_parser, subparsers):
        # {{{
        # {{{ Generic parser
        base_parser.add_argument(
                "--version", action="version",
                version="%(prog)s 0.5")

        base_parser.add_argument(
                "-f", "--file",
                help="input file. Default: file.input",
                required=False,
                default="file.input")

        base_parser.add_argument(
                "-o", "--output",
                help="Output file. Default: file.output",
                required=False,
                default="file.output")
        # }}}

        # {{{ Parser for encrypting
        parser_encryption = subparsers.add_parser(
                "encrypt", parents=[base_parser],
                help="Encrypt file")

        key_shift_key = parser_encryption.add_mutually_exclusive_group(
                required=True)
        key_shift_key.add_argument(
                "-k", "--key",
                nargs="?",
                help="Key file for encryption.\
                One of key file or shift key must be set.",
                const="shift.key",
                dest="key_file",
                required=False)

        key_shift_key.add_argument(
                "-s", "--shift_key",
                nargs="?",
                const="generate",
                help="Shift key for encryption.\
                If not set, will be randomly generated.\
                One of key file or shift key must be set.",
                required=False)
        # }}}

        # {{{ Parser for decrypting
        parser_decryption = subparsers.add_parser(
                "decrypt", parents=[base_parser],
                help="Decrypt file")

        parser_decryption.add_argument(
                "-k", "--key",
                help="Output key file. Default: shift_output.key",
                required=False,
                dest="key_file",
                default="shift_output.key")
        # }}}

        # {{{ Parser for decrypting with key, Test option
        parser_testing = subparsers.add_parser(
                "test", parents=[base_parser],
                help="Decrypt test with key")

        key_shift = parser_testing.add_mutually_exclusive_group(
                required=True)
        key_shift.add_argument(
                "-k", "--key",
                nargs="?",
                help="Key file for encryption.\
                One of key file or shift key must be set.",
                const="shift.key",
                dest="key_file",
                required=False)

        key_shift.add_argument(
                "-s", "--shift_key",
                help="Shift key for encryption.\
                One of key file or shift key must be set.",
                required=False)

        # }}}

        self.args = parser.parse_args()
        # }}}
    # }}}
