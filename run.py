#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PIC import read, disulf, hydroph, ionic,dist, hydrogen
import argparse
import sys
import ntpath

if __name__ == "__main__":
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
    parser.add_argument('--hydrogen', action="store_true",
                        help="Calculate the number of hydrogen bonds in the protein")

    args = parser.parse_args()


    print(args.input.name)
    if args.input.name.endswith('.pdb'):
        print('The file is correct.')
        pdb = args.input
    else:
        print('This is not a .pdb file, please provide one. The expected extension is .pdb.')
        sys.exit()
    #je pourrais utiliser un raise ValueError("message d'erreur"), mais seulement si j'ai le temps

    list = read(pdb)[0]
    print("The number of atoms is ",len(list),".")


    lala = ntpath.basename(str(args.input.name))
    filename = "results/" + lala +"_PICresults.csv"
    result = open(filename,"w")
    result.write("Protein Interaction Calculator \n"+args.input.name+"\n")


    if args.disulfide == True:
        print("COMPUTING DISULFIDE BONDS...")
        disulfures = disulf(list)
        result.write("DISULPHIDE BRIDGES \n POSITION,RESIDUE,CHAIN, ,POSITION,RESIDUE,CHAIN\n")
        for i in disulfures:
            line = str(i[0].res_number)+","+str(i[0].aa)+","+str(i[0].chain)+", ,"+str(i[1].res_number)+","+i[1].aa+","+i[0].chain+"\n"
            result.write(line)
            #print(i[0].num_atom, 'et ',i[1].num_atom, 'sont à une distance de ', i[2], 'angstroms.')

    if args.hydrophobic == True:
        print("COMPUTING HYDROPHOBIC INTERACTIONS...")
        hydro = hydroph(list)
        result.write("HYDROPHOBIC BONDS \n POSITION,RESIDUE,CHAIN, ,POSITION,RESIDUE,CHAIN\n")
        for i in hydro:
            line = str(i[0].res_number) + "," + str(i[0].aa) + "," + str(i[0].chain) + ", ," + str(i[1].res_number) + "," + \
                   i[1].aa + "," + i[0].chain + "\n"
            result.write(line)
            #print(i[0].res_number,'(', i[0].aa,')', 'et ',i[1].res_number, 'sont à une distance de ', i[2], 'angstroms.')

    if args.ionic == True:
        print("COMPUTING IONIC BONDS...")
        io = ionic(list)
        result.write("IONIC BONDS \n POSITION,RESIDUE,CHAIN, ,POSITION,RESIDUE,CHAIN\n")
        for i in io:
            line = str(i[0].res_number) + "," + str(i[0].aa) + "," + str(i[0].chain) + ", ," + str(i[1].res_number) + "," + \
                   i[1].aa + "," + i[0].chain + "\n"
            result.write(line)
            #print(i[0].res_number, '(', i[0].aa, ')', 'et ', i[1].res_number, 'sont à une distance de ', i[2], 'angstroms.')

    if args.hydrogen == True:
        print("COMPUTING HYDROGEN BONDS...")
        hyg = hydrogen(list)
        result.write("HYDROGEN BONDS \nDONOR,,,,ACCEPTOR,\n POSITION,RESIDUE,CHAIN, ,POSITION,RESIDUE,CHAIN\n")
        for i in hyg:
            line = str(i[0].res_number) + "," + str(i[0].aa) + "," + str(i[0].chain) + ", ," + str(i[1].res_number) + "," + \
                   i[1].aa + "," + i[0].chain + "\n"
            result.write(line)
            #print(i[0].res_number, '(', i[0].aa, ')', 'et ', i[1].res_number, 'sont à une distance de ', i[2], 'angstroms.')
    print("Results can be found in",filename)



    #note pour moi-meme : les arguments sont stockés dans args.lenomdel'argument
