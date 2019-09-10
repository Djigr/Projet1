#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIC import read
import argparse
import sys

parser = argparse.ArgumentParser(prog='command.py', description='Protein Interaction Calculator.')
parser.add_argument('input',
                    nargs='?',
                    type=argparse.FileType('r'))
#parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers(default: find the max')

#parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
parser.add_argument('--disulfide', help='Calculate the number of disulfide bonds in the protein', default=2.2)

args = parser.parse_args()


print(args.input.name)
if args.input.name.endswith('.pdb'):
    print('Je suis un programme qui fonctionne')
else:
    print('This is not a .pdb file, please provide one. The expected extension is .pdb.')
    sys.exit()

read(args.input)

#note pour moi-meme : les arguments sont stockés dans args.lenomdel'argument