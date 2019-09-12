#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PIC import read, disulf
import argparse
import sys

parser = argparse.ArgumentParser(prog='command.py', description='Protein Interaction Calculator.')
parser.add_argument('input',
                    nargs='?',
                    type=argparse.FileType('r'))
parser.add_argument('--disulfide', action="store_true", help='Calculate the number of disulfide bonds in the protein',
                    default=2.2)

args = parser.parse_args()


print(args.input.name)
if args.input.name.endswith('.pdb'):
    print('Je suis un programme qui fonctionne')
    pdb = args.input
else:
    print('This is not a .pdb file, please provide one. The expected extension is .pdb.')
    sys.exit()
#je pourrais utiliser un raise ValueError("message d'erreur"), mais seulement si j'ai le temps

list = read(pdb)[0]
print("Le nombre d'atomes s'eleve a",len(list),".")

disulfures = disulf(list)[3]
print(disulfures[1].num_atom)
for i in disulfures:
    print(i.num_atom)
print(args)



#note pour moi-meme : les arguments sont stockés dans args.lenomdel'argument