# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""Protein Interaction Calculator.
Try 6pa8.pdb --disulfide --hydrophobic for a quick example"""

from PIC import read, disulf, hydroph, ionic, dist, hydrogen
import argparse
import sys
import ntpath


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='command.py',
    description='Protein Interaction Calculator.')
    parser.add_argument('input',
                        nargs='?',
                        type=argparse.FileType('r'),
                        help='input PDB file, should be formatted as <6pa8.pdb>')
    parser.add_argument('--disulfide', action="store_true",
    help='Calculate the number of disulphide bonds in the protein')
    parser.add_argument('--hydrophobic', action="store_true",
                        help='Calculate the number of hydrophobic bonds in the protein')
    parser.add_argument('--ionic', action="store_true",
                        help="Calculate the number of ionic bonds in the protein")
    parser.add_argument('--hydrogen', action="store_true",
                        help="Calculate the number of hydrogen bonds in the protein")

    args = parser.parse_args()

    # Check if the file extension is right
    print(args.input.name)
    if args.input.name.endswith('.pdb'):
        print('The PDB file is correct.')
        pdb = args.input
    else:
        print('This is not a .pdb file, please provide one. The expected extension is .pdb.')
        sys.exit()

    # Load the list of atoms in the list variable, and print the length of this list, to check if the number is coherent for the user
    list = read(pdb)[0]
    print("The number of atoms is ", len(list), ".")

    # Create the result file as a csv customized with the name
    # of the PDB
    lala = ntpath.basename(str(args.input.name))
    filename = "results/" + lala + "_PICresults.csv"
    result = open(filename, "w")
    result.write("Protein Interaction Calculator \n"+args.input.name+"\n")

    # Check the arguments to make the calculation
    if args.disulfide is True:
        print("COMPUTING DISULPHIDE BONDS...")
        disulfures = disulf(list)
        result.write("DISULPHIDE BRIDGES \n POSITION,RESIDUE,CHAIN, ,POSITION,RESIDUE,CHAIN\n")
        for i in disulfures:
            line = str(i[0].res_number)+","+str(i[0].aa)+","+str(i[0].chain)+", ,"+str(i[1].res_number)+","+i[1].aa+","+i[0].chain+"\n"
            result.write(line)


    if args.hydrophobic is True:
        print("COMPUTING HYDROPHOBIC INTERACTIONS...")
        hydro = hydroph(list)
        result.write("HYDROPHOBIC BONDS \n POSITION,RESIDUE,CHAIN, ,POSITION,RESIDUE,CHAIN\n")
        for i in hydro:
            line = str(i[0].res_number) + "," + str(i[0].aa) + "," + str(i[0].chain) + ", ," + str(i[1].res_number) + "," + \
                   i[1].aa + "," + i[0].chain + "\n"
            result.write(line)


    if args.ionic is True:
        print("COMPUTING IONIC BONDS...")
        io = ionic(list)
        result.write("IONIC BONDS \n POSITION,RESIDUE,CHAIN, ,POSITION,RESIDUE,CHAIN\n")
        for i in io:
            line = str(i[0].res_number) + "," + str(i[0].aa) + "," + str(i[0].chain) + ", ," + str(i[1].res_number) + "," + \
                   i[1].aa + "," + i[0].chain + "\n"
            result.write(line)


    if args.hydrogen is True:
        print("COMPUTING HYDROGEN BONDS...")
        hyg = hydrogen(list)
        result.write("HYDROGEN BONDS \nDONOR,,,,ACCEPTOR,\n POSITION,RESIDUE,CHAIN, ,POSITION,RESIDUE,CHAIN\n")
        for i in hyg:
            line = str(i[0].res_number) + "," + str(i[0].aa) + "," + str(i[0].chain) + ", ," + str(i[1].res_number) + "," + \
                   i[1].aa + "," + i[0].chain + "\n"
            result.write(line)

    print("Results can be found in", filename)



    # note pour moi-meme : les arguments sont stockés dans args.lenomdel'argument
