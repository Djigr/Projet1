#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
from collections import namedtuple
import math

def dist(x1,x2,y1,y2,z1,z2):
    """The dist function calculates the distance between two atoms via euclidian calcul."""
    X1=int(x1)
    X2=int(x2)
    Y1=int(y1)
    Y2=int(y2)
    Z1=int(z1)
    Z2=int(z2)
    dist = math.sqrt((X1-X2)^2 + (Y1-Y2)^2 + (Z1-Z2)^2)
    return dist


# if len(sys.argv)< 2:
#     print("Précisez une action en paramètre")
#     sys.exit(1)
#
# action = sys.argv[1]
# if action == "start":
#     print("on start")
# else:
#     print ("Je ne connais pas cette action")
# print(sys.argv)


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
#probablement là que je mettrai mes fonctions en rapport avec l'extraction primaire
    pass

pdb = open("6pa8.pdb", "r")
#empêcher d'ouvrir autre chose que du .pdb !!

list = []

for line in pdb:

    if line[:4] == 'ATOM':
        file = Atom(line[0:4],line[6:11],line[13:16],line[17:20],line[21],line[23:26],line[27],line[31:38],line[39:46],
                    line[47:54],line[55:60],line[61:66],line[77:78],line[79:80])
        #à changer avec la méthode strip
        list.append(file)

print("Le nombre d'atomes s'élève à",len(list))

travail = []
for i in list:
    if i.element == 'S':
        travail.append(i)
        print(travail)

#for j in travail:

for ii in range(0, len(travail)):
    j = travail[ii]
    k = travail[ii+1]
    for k in travail:
        dist(j.x, k.x, j.y, k.y, j.z, k.z)
        print(dist)