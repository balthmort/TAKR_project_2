#!/usr/bin/env python3
# author:   Petr Surý
# Date:     23.3.2017
# File:     param_parser.py
# Project:  TAKR project 2

import argparse


class ParseParams(object):
    # {{{
    input_file = None
    output_file = None
    key = None
    subparser = None
    parser = None

    def __init__(self):
        # {{{
        self.parser = argparse.ArgumentParser(
                prog="TAKR Project 2",
                description='''
                TAKR - Project 2
                Script for encrypting/decrypting text file with Caesar cipher
                ''')

        self.parseParams(self.parser)
        # }}}

    def help_print(self):
        # {{{
        self.parser.print_help()
        # }}}

    def parseParams(self, parser):
        # {{{
        # {{{ Generic parser
        parser.add_argument(
                "--version", action="version",
                version="%(prog)s 0.5")
        # }}}

        # {{{ Parent parser for encryptionúdecryption
        parent_parser = argparse.ArgumentParser(add_help=False)
        parent_parser.add_argument(
                "-f", "--file",
                help="input file. Default: file.input",
                required=False,
                default="file.input")

        parent_parser.add_argument(
                "-o", "--output",
                help="Output file. Default: file.output",
                required=False,
                default="file.output")
        # }}}

        # {{{ Create subparsers
        subparsers = parser.add_subparsers(
                dest="subparser",
                title="subcommands",
                description="Test decrypt with key or encrypt/decrypt file",
                help="additional help")
        # }}}

        # {{{ Parser for encrypting
        parser_encryption = subparsers.add_parser(
                "encrypt", parents=[parent_parser],
                help="Encrypt file")

        key_shift_key = parser_encryption.add_mutually_exclusive_group(
                required=True)
        key_shift_key.add_argument(
                "-k", "--key",
                help="Key file for encryption.",
                default="shift.key",
                required=False)

        key_shift_key.add_argument(
                "-s", "--shift_key",
                help="Shift key for encryption.\
                If not set, shift key will be randomly generated.",
                dest="key",
                default=None,
                required=False)
        # }}}

        # {{{ Parser for decrypting
        parser_decryption = subparsers.add_parser(
                "decrypt", parents=[parent_parser],
                help="Decrypt file")

        parser_decryption.add_argument(
                "-k", "--key",
                help="Output key file. Default: shift_output.key",
                required=False,
                default="shift_output.key")
        # }}}

        # {{{ Parser for decrypting with key, Test option
        parser_testing = subparsers.add_parser(
                "test", parents=[parent_parser],
                help="Decrypt test with key")

        key_shift = parser_testing.add_mutually_exclusive_group(
                required=True)
        key_shift.add_argument(
                "-k", "--key",
                help="Key file for encryption.",
                default="shift.key",
                required=False)

        key_shift.add_argument(
                "-s", "--shift_key",
                help="Shift key for encryption.",
                dest="key",
                default=None,
                required=False)

        # }}}

        arguments = parser.parse_args()
        parent_args = parent_parser.parse_args()

        self.subparser = arguments.subparser

        self.input_file = parent_args.file
        self.output_file = parent_args.output

        if self.subparser == "encrypt":
            self.key_file = arguments.key
        elif self.subparser == "decrypt":
            self.key_file = arguments.key
        # }}}
    # }}}
