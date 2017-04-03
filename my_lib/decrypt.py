#!/usr/bin/env bash python3
# Author:   Patrik Vágner
# Date:     3.4.2017
# File:     decrypt.py
# Project:  TAKR project 2

import sys

class DecryptCaesar(object):
    {
    alphabet_lenght = 26

    def __init__(self, input_file, output_file):
        {
        sys.stderr.write("Decrypt Caesar\n")
        }

    def decrypt(self, input_file):
        {
        sys.stderr.write("Decryption in progress\n")

 
	def filecharcount(openfile):
   		return sorted(collections.Counter(c for l in openfile for c in l).items())
 
	f = open(sys.argv[1])
	print(filecharcount(f))



	
	frekvencePismenAnglicke = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}    """obsahuje četnost písmen v anglické abecedě"""
	ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'  """Nejčastější výskyt anglické abecedy"""
	PISMENA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


     	def getPismenoScitat(zprava):
		pismenoScitat = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
		"""Sčítač četnosti písmen"""
	        for pismeno in zprava.upper():
        		if pismeno in PISMENA:
                		pismenoScitat[pismeno] += 1
    		"""Cyklus pro sčítání písmen"""
    	     	return pismenoScitat

	def getItemAtIndexZero(x):
        	return x[0]

	def getFrekvenciPoradek(zprava):
		"""Uspořádání písmen dle četnosti"""
        	pismenoToFreq = getPismenoScitat(zprava) """Pismeno : četnost"""

		freqTopismeno = {}
        	for pismeno in PISMENA:
             		if pismenoToFreq[pismeno] not in freqTopismeno:
                 		freqTopismeno[pismenoToFreq[pismeno]] = [pismeno]
         		else:
                		freqTopismeno[pismenoToFreq[pismeno]].append(pismeno)
    				"""Změní klíče místo písmenek bude četnost (asi takto Četnost : pismeno), Přiřadí a dá k sobě ty písmena se stejnou četnosti

         	for freq in freqTopismeno:
             		freqTopismeno[freq].sort(key=ETAOIN.find, reverse=True)
             		freqTopismeno[freq] = ''.join(freqTopismeno[freq])
			"""seznam n-tic (páru), které jsme setřídili on nejmenšího po největší"""

         	freqPairs = list(freqTopismeno.items())
         	freqPairs.sort(key=getItemAtIndexZero, reverse=True)
		"""Setřídí n-tice (dvojice) od největší po nejmenší četnost"""
         	freqOrder = []    """Seznam pouze pismen v daném pořadí"""
         	for freqPair in freqPairs:
             		freqOrder.append(freqPair[1])
    
         	return ''.join(freqOrder)
		

	def frekvenceShody(zprava):
         
        	freqOrder = getFrekvenciPoradek(zprava)
    
         	shoda = 0
     
        	for spolecnepismeno in ETAOIN[:6]:
             		if spolecnepismeno in freqOrder[:6]:
                 		shoda += 1

         	for nespolecnepismeno in ETAOIN[-6:]:
             		if nespolecnepismeno in freqOrder[-6:]:
                 		shoda += 1
 
         	return shoda
		"""return shoda měla vracet posun, pouze o 12"""		
		
	key = -key  
      """klíč pro dešifrování by měl být záporný, a dál by mělo být stejné a přejmenované, bez uložení klíče"""
 	decrypted_string = ""

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

                        decrypted_string += chr(ord_char)
                    else:
                        decrypted_string += char

        return decrypted_string
        }

    def save_into_file(self, output_file, decrypted_string):
        {
        sys.stderr.write("Saving decrypted file\n")
        with open(output_file, "w") as file_out:
            file_out.write(decrypted_string)
        }

    }
