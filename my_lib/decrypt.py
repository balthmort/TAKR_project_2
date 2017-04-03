#!/usr/bin/env python3
# Author:   Patrik Vágner
# Date:     3.4.2017
# File:     decrypt.py
# Project:  TAKR project 2

import sys
from collections import Counter
from my_lib import encrypt


class DecryptCaesar(object):

    frekvencePismenAnglicke = {
        'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
        'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78,
        'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
        'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15,
        'Q': 0.10, 'Z': 0.07}

    ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

    PISMENA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, input_file, output_file):
        sys.stderr.write("Decrypt Caesar\n")
        key = self.findKey(input_file)
        encrypt.EncryptCaesar(input_file, output_file, -key)

    def findKey(self, input_file):
        most_common = self.mostCommon(self.fileCharCounter(input_file))
        key = most_common - ord("E")
        if key < 0:
            key *= -1
        return key

    def fileCharCounter(self, input_file):
        cnt = Counter()
        with open(input_file, "r") as file_input:
            for line in file_input:
                for char in line.upper():
                    if char.isalpha():
                        cnt[char] += 1
        return cnt

    def mostCommon(self, counter):
        return ord(counter.most_common(1)[0][0])
