#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PIC import read, disulf, hydroph
import argparse
import sys

parser = argparse.ArgumentParser(prog='command.py', description='Protein Interaction Calculator.')
parser.add_argument('input',
                    nargs='?',
                    type=argparse.FileType('r'))
parser.add_argument('--disulfide', action="store_true", help='Calculate the number of disulfide bonds in the protein',
                    default=2.2)
parser.add_argument('--hydrophobic', action="store_true",
                    help='Calculate the number of hydrophobic bonds in the protein', default = 5)

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

if args.disulfide == True:
    print("PONTS DISULFURES")
    disulfures = disulf(list)
    for i in disulfures:
        print(i[0].num_atom, 'et ',i[1].num_atom, 'sont à une distance de ', i[2], 'angstroms.')

if args.hydrophobic == True:
    print("LIAISONS HYDROPHOBES")
    hydro = hydroph(list)
    for i in hydro:
        print(i[0].res_number,'(', i[0].aa,')', 'et ',i[1].res_number, 'sont à une distance de ', i[2], 'angstroms.')
print(args)



#note pour moi-meme : les arguments sont stockés dans args.lenomdel'argument
