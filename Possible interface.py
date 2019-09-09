#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *

master = Tk()
def var_states():
    print("Hydrophobic interactions: %d, /nDisulphide bridges: %d, /nHydrogen bond: %d" %(var1.get(), var2.get(), var3.get()))

Label(master, text = "Choose the following interactions to check in your molecule:").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, text="hydrophobic interations", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="disulphide bridges", variable=var2).grid(row=2, sticky=W)
var3 = IntVar()
Checkbutton(master, text="hydrogen bond", variable=var3).grid(row=3, sticky=W)
Button(master, text='Quit', command=master.quit).grid(row=4, sticky=W, pady=4)

mainloop()