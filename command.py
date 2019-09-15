#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PIC import read, disulf, hydroph, ionic,dist
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
parser.add_argument('--ionic', action="store_true",
                    help="Calculate the number of ionic bonds in the protein")

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

result = open("result.csv","w")
result.write("Protein Interaction Calculator \n"+args.input.name+"\n")
if args.disulfide == True:
    print("PONTS DISULFURES")
    disulfures = disulf(list)
    result.write("DISULPHIDE BRIDGES \n POSITION,RESIDUE,CHAIN, ,POSITION,RESIDUE,CHAIN\n")
    for i in disulfures:
        line = str(i[0].res_number)+","+str(i[0].aa)+","+str(i[0].chain)+", ,"+str(i[1].res_number)+","+i[1].aa+","+i[0].chain+"\n"
        result.write(line)
        print(i[0].num_atom, 'et ',i[1].num_atom, 'sont à une distance de ', i[2], 'angstroms.')

if args.hydrophobic == True:
    print("LIAISONS HYDROPHOBES")
    hydro = hydroph(list)
    result.write("HYDROPHOBIC BONDS \n POSITION,RESIDUE,CHAIN, ,POSITION,RESIDUE,CHAIN\n")
    for i in hydro:
        line = str(i[0].res_number) + "," + str(i[0].aa) + "," + str(i[0].chain) + ", ," + str(i[1].res_number) + "," + \
               i[1].aa + "," + i[0].chain + "\n"
        result.write(line)
        print(i[0].res_number,'(', i[0].aa,')', 'et ',i[1].res_number, 'sont à une distance de ', i[2], 'angstroms.')

if args.ionic == True:
    print("LIAISONS IONIQUES")
    io = ionic(list)
    result.write("IONIC BONDS \n POSITION,RESIDUE,CHAIN, ,POSITION,RESIDUE,CHAIN\n")
    for i in io:
        line = str(i[0].res_number) + "," + str(i[0].aa) + "," + str(i[0].chain) + ", ," + str(i[1].res_number) + "," + \
               i[1].aa + "," + i[0].chain + "\n"
        result.write(line)
        print(i[0].res_number, '(', i[0].aa, ')', 'et ', i[1].res_number, 'sont à une distance de ', i[2], 'angstroms.')
print(args)



#note pour moi-meme : les arguments sont stockés dans args.lenomdel'argument
