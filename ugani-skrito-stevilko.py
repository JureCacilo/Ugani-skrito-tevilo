# -*- coding: utf-8 -*-
# Programček s katerim uganjaš skrito število
from random import randint # uvozimo random knjiznico


secret = randint(0,20)
guess = input("Vnesi celo stevilo med 0 in 20: ")
if int(guess) != secret:
    print("Vaše ugibanje je bilo napačno, pravilno število je bilo " + str(secret))
else:
    print("Čestitam, uganili ste pravo stevilo!")