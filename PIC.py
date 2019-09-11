#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from collections import namedtuple
import math


def dist(a,b):
    """The dist function calculates the distance between two atoms via euclidian calculation."""
    x1=a.x
    x2=b.x
    y1=a.y
    y2=b.y
    z1=a.z
    z2=b.z
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    return distance

class Atom(namedtuple('ligne_Atom','ATOM num_atom typ_atom aa chain res_number ACha x y z occupancy temp element charge')):
    """The Atom class is used to stock atom objects, along with their variables, which are :
        -ATOM : just the nature of the line extracted from the .pdb file. Should always be "ATOM"
        -num_atom : gives the unique ID of the atom in the protein
        -typ_atom : displays the place of the atom in the residue and its nomenclature
        -aa : displays in which amino-acid the atom is involved
        -chain : displays in which chain the atom is involved
        -res_number : displays the ID of the residue the atom is involved with
        -ACha : chépu
        -x, y, z : coordinates at which the atom is found
        -occupancy : chépu
        -temp : chépu
        -element : element from the Mendeleiev table the atom is of
        -charge : chépu"""
    #ah qu'il est beau le docstring, accessible avec machin.__doc__
    pass

#pdb = open("6pa8.pdb", "r")


list = []
def read(input):
    #list = []
    fich = open(input.name, 'r')

    for line in fich:

        if line[:6].strip() == 'ATOM':
            file = Atom(line[0:6].strip(),
                        int(line[6:11].strip()),
                        line[12:16].strip(),
                        line[17:20].strip(),
                        line[21:22].strip(),
                        int(line[23:26].strip()),
                        line[26:27].strip(),
                        float(line[30:38].strip()),
                        float(line[38:46].strip()),
                        float(line[46:54].strip()),
                        float(line[54:60].strip()),
                        float(line[60:66].strip()),
                        line[77:78].strip(),
                        line[78:80].strip())
            #à changer avec la méthode strip
            list.append(file)
    return list, fich

travail = []
for i in list:
    if i.element == 'S':
        travail.append(i)


a = 2.2
for ii in range(0, len(travail)-1):
    j = travail[ii]
    for p in range(ii+1,len(travail)-1):
        k =travail[p]
        print ('Je compare latome', j.num_atom,'et latom',k.num_atom)
        if dist(j, k) < a:
            print('The atoms ', j.num_atom, ' and the atom ', k.num_atom, 'are involved in a disulphide bond bc they are at ', dist(j, k), 'angstroms')
