#!/usr/bin/env bash python3
# Author:   Petr Surý
# Date:     26.3.2017
# File:     encrypt.py
# Project:  TAKR project 2

import sys
from random import randint


class EncryptCaesar(object):
    # {{{
    alphabet_lenght = 26
    encrypted_string = None

    def __init__(self, input_file, output_file, key, save=True):
        # {{{
        sys.stderr.write("Encrypt Caesar\n")
        if key == "generate":
            key = self.generate_random_key()
        else:
            key = int(key)

        self.encrypted_string = str(self.encrypt(input_file, key))
        if save:
            self.save_into_file(output_file, self.encrypted_string)
        # }}}

    def encrypt(self, input_file, key):
        # {{{
        sys.stderr.write("Encryption in progress\n")
        sys.stderr.write("Encryption key: " + str(key) + "\n")
        sys.stdout.write("Encryption key: " + str(key) + "\n")

        encrypted_string = ""

        with open(input_file, "r") as file_input:
            for line in file_input:
                for char in line:
                    if char.isalpha():
                        ord_char = ord(char)
                        ord_char += key

                        if char.isupper():
                            if ord_char > ord("Z"):
                                ord_char -= self.alphabet_lenght
                            elif ord_char < ord("A"):
                                ord_char += self.alphabet_lenght
                        elif char.islower():
                            if ord_char > ord("z"):
                                ord_char -= self.alphabet_lenght
                            elif ord_char < ord("a"):
                                ord_char += self.alphabet_lenght

                        encrypted_string += chr(ord_char)
                    else:
                        encrypted_string += char

        return encrypted_string
        # }}}

    def save_into_file(self, output_file, encrypted_string):
        # {{{
        sys.stderr.write("Saving encrypted file\n")
        with open(output_file, "w") as file_out:
            file_out.write(encrypted_string)
        # }}}

    def save_key(self, key):
        sys.stderr.write("Saving encryption key\n")
        with open("shift.key", "w") as key_file:
            key_file.write(key)

    def generate_random_key(self):
        # {{{
        sys.stderr.write("Generating random key!\n")
        return randint(0, self.alphabet_lenght-1)
        # }}}
    # }}}
