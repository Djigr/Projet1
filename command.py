#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PIC import read
import argparse
import sys

parser = argparse.ArgumentParser(prog='command.py', description='Protein Interaction Calculator.')
parser.add_argument('input',
                    nargs='?',
                    type=argparse.FileType('r'))
parser.add_argument('--disulfide', help='Calculate the number of disulfide bonds in the protein', default=2.2)

args = parser.parse_args()


print(args.input.name)
if args.input.name.endswith('.pdb'):
    print('Je suis un programme qui fonctionne')
    pdb = args.input
else:
    print('This is not a .pdb file, please provide one. The expected extension is .pdb.')
    sys.exit()
#je pourrais utiliser un raise ValueError("message d'erreur"), mais seulement si j'ai le temps

print(type(pdb))
list = read(pdb)[0]
print(type(list))
print("Le nombre d'atomes s'eleve a",len(list))
print(list[0])
print(list)


#note pour moi-meme : les arguments sont stockés dans args.lenomdel'argument