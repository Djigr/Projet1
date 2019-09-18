# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module, called PIC, contains functions related to calculating protein interactions."""
import sys
from collections import namedtuple
import math


def dist(a, b):
    """Calculate the distance between two atoms
        via euclidian calculation.

        a and b are objects of the Atom class."""
    x1 = a.x
    x2 = b.x
    y1 = a.y
    y2 = b.y
    z1 = a.z
    z2 = b.z
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    return distance


def calcul_centre_masse(var):
    """Calculate the centroid of a list of atoms. var is a list of objects of the Atom class."""
    summasse = 0
    XN = 0
    YN = 0
    ZN = 0
    for i in var:
        summasse += i.masse
        XN += i.x*i.masse
        YN += i.y*i.masse
        ZN += i.z*i.masse
    Xbar = XN/summasse
    Ybar = YN/summasse
    Zbar = ZN/summasse
    return Xbar, Ybar, Zbar


class Atom(namedtuple('ligne_Atom',
                      'ATOM num_atom typ_atom aa chain res_number ACha x y z occupancy temp element charge')):
    """The Atom class is used to stock atom objects, along with their variables.

    Parameters :
        -ATOM : just the nature of the line extracted from the .pdb file. Should always be "ATOM"
        -num_atom : gives the unique ID of the atom in the protein
        -typ_atom : displays the place of the atom in the residue and its nomenclature
        -aa : displays in which amino-acid the atom is involved
        -chain : displays in which chain the atom is involved
        -res_number : displays the ID of the residue the atom is involved with
        -ACha : irrelevant
        -x, y, z : coordinates at which the atom is found
        -occupancy : irrelevant
        -temp : irrelevant
        -element : element from the Mendeleiev table the atom is of
        -charge : irrelevant"""

    # ah qu'il est beau le docstring, accessible avec machin.__doc__


# Creation of the variable that will contain the list of atoms
list = []


def read(input):
    """Stock each atom (and its characteristics) in the form of an object of the Atom class, in a list.

input is the file that has been retrieved from argparse in the run.py script"""
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
            list.append(file)
    return list, fich


def disulf(list):
    """Calculate the distance between two sulfur atoms in the list of atoms from the read function and stocks them in a list of list. list is the variable result from the read function"""
# first, stock every sulfur atom in a work list
    travail = []
    for i in list:
        if i.element == 'S':
            travail.append(i)

    final = []
    a = 2.2
    for ii in range(0, len(travail)-1):
        j = travail[ii]
        for p in range(ii+1, len(travail)-1):
            k = travail[p]
            bond = []
            if dist(j, k) < a:
                bond.append(j)
                bond.append(k)
                bond.append(dist(j, k))
                final.append(bond)
    return final


def hydroph(list):
    """Calculate the distance between two hydrophobic atoms from hydrophobic residues in the list of atoms from the read function and stocks them in a list of list. list is the variable result from the read function"""
    aa_hydroph = ["VAL", "ALA", "LEU", "ILE", "MET", "PHE", "TRP", "PRO", "TYR"]
    travail = []
    for i in list:
        flag = False
        for j in aa_hydroph:
            if i.aa == j:
                flag = True
        if flag is True:
            travail.append(i)
            flag = False

    chose = []  # List of amino-acids

    # Check distance between involved atoms
    final = []
    for ii in range(0, len(chose)-1):
        j = chose[ii]
        for p in range(ii+1, len(chose)):
            k = chose[p]
            for imax in j:
                for ichose in k:
                    bond = []
                   # Wrong list is a list of every atom that can not be involved in a hydrophobic interaction
                    wrong = ["C", "CA", "O", "OXT", "H", "N",
                             "H1", "H2", "H3", "HA2", "HA3",
                             "HA", "HB2", "HB3",
                             "HG", "HG2", "HG3",
                             "HD", "HD11", "HD12", "HD13", "HD2", "HD21", "HD22", "HD23", "HD3",
                             "HE1", "HE2", "HE3"]

                    if imax.typ_atom not in wrong and ichose.typ_atom not in wrong:
                        if dist(imax, ichose) < 5:
                            if len(final) == 0:
                                bond.append(imax)
                                bond.append(ichose)
                                bond.append(dist(imax, ichose))
                                final.append(bond)
                            elif final[len(final)-1][0].res_number != imax.res_number and final[len(final)-1][1].res_number != ichose.res_number:
                                bond.append(imax)
                                bond.append(ichose)
                                bond.append(dist(imax, ichose))
                                final.append(bond)
    return final


def ionic(list):
    """Calculate the distance between two atoms from ionic residues in the list of atoms from the read function and stocks them in a list of list. list is the variable result from the read function"""
    plus = ["ASP", "GLU", "LYS", "ARG", "HIS"]
    travail = []
    for i in list:
        flag = False
        for j in plus:
            if i.aa == j:
                flag = True
        if flag is True:
            travail.append(i)
            flag = False
    print(travail[0], 'fait la longueur', len(travail))
    chose = []
    truc = []
    for i in travail:
        if len(truc) == 0:
            truc.append(i)
        elif truc[0].res_number == i.res_number:
            truc.append(i)
        elif truc[0].res_number != i.res_number:
            chose.append(truc)
            truc = []
            truc.append(i)
    chose.append(truc)

    final = []
    plus = ["ASP", "GLU"]
    minus = ["LYS", "ARG", "HIS"]
    listy = ["OD2", "OE2", "NZ", "NH2", "NE2"]
    for ii in range(0, len(chose)-1):
        j = chose[ii]
        for p in range(ii, len(chose)):
            k = chose[p]
            for imax in j:
                for ichose in k:
                    bond = []
                    if imax.typ_atom in listy:
                        if ichose.typ_atom in listy:
                            if (imax.aa in plus and ichose.aa in minus)or(imax.aa in minus and ichose.aa in plus):
                                if dist(imax, ichose) < 6:
                                    if len(final) == 0:
                                        bond.append(imax)
                                        bond.append(ichose)
                                        bond.append(dist(imax, ichose))
                                        final.append(bond)
                                    elif final[len(final)-1][0].res_number != imax.res_number and final[len(final)-1][1].res_number != ichose.res_number:
                                        bond.append(imax)
                                        bond.append(ichose)
                                        bond.append(dist(imax, ichose))
                                        final.append(bond)
    return final


def hydrogen(list):
    """Calculate the distance between two atoms from residues capable of hydrogen bonds in the list of atoms from the read function and stocks them in a list of list. list is the variable result from the read function"""
    travail = []
    atoms = ["N", "O"]
    for i in list:
        if i.typ_atom in atoms and i.aa != "PRO":
            travail.append(i)

    chose = []
    a = 3.5
    for ii in range(0, len(travail) - 1):
        j = travail[ii]
        for p in range(ii + 2, len(travail)):
            k = travail[p]

            bond = []
            if j.typ_atom == "N" and k.typ_atom == "O":
                if dist(j, k) < a:
                    bond.append(j)
                    bond.append(k)
                    bond.append(dist(j, k))
                    chose.append(bond)
            if j.typ_atom == "O" and k.typ_atom == "N":
                if dist(j, k) < a:
                    bond.append(k)
                    bond.append(j)
                    bond.append(dist(j, k))
                    chose.append(bond)
    return chose
