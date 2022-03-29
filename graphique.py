import tkinter as tk
from tkinter import *

root = tk.Tk()

root.title("Outil RDF")
root.geometry('720x480')
frameCB = tk.Frame(root)
frameCB.pack(fill=tk.X, side=tk.TOP)


titreCB = tk.Checkbutton(frameCB, text='Titre')
notCB = Checkbutton(frameCB, text='Note')
composeurCB = Checkbutton(frameCB, text='Composeur')
genreCB = Checkbutton(frameCB, text='Genre')
clefCB = Checkbutton(frameCB, text='Clef')
opusCB = Checkbutton(frameCB, text='Opus')

frameCB.columnconfigure(0, weight=1)
frameCB.columnconfigure(1, weight=1)

titreCB.grid(row=0, column=0, sticky=tk.W+tk.E)
notCB.grid(row=0, column=1, sticky=tk.W+tk.E)

composeurCB.grid(row=1, column=0, sticky=tk.W+tk.E)
genreCB.grid(row=1, column=1, sticky=tk.W+tk.E)

clefCB.grid(row=2, column=0, sticky=tk.W+tk.E)
opusCB.grid(row=2, column=1, sticky=tk.W+tk.E)

frameCB2 = tk.Frame(root)
frameCB2.pack(fill=tk.X, side=tk.TOP)


jaroCB = tk.Checkbutton(frameCB2, text='Jaro')
jaroWrinklerCB = Checkbutton(frameCB2, text='JaroWrinkler')
numSimilarityCB = Checkbutton(frameCB2, text='NumSimilarity')
uriEqualityCB = Checkbutton(frameCB2, text='UriEquality')
ngramCB = Checkbutton(frameCB2, text='Ngram')
levenshteinCB = Checkbutton(frameCB2, text='Levenshtein')
mongeElkanCB = Checkbutton(frameCB2, text='MongeElkan')
jaccarCB = Checkbutton(frameCB2, text='Jaccar')

frameCB2.columnconfigure(0, weight=1)
frameCB2.columnconfigure(1, weight=1)
frameCB2.columnconfigure(2, weight=1)

jaroCB.grid(row=0, column=0, sticky=tk.W+tk.E)
jaroWrinklerCB.grid(row=0, column=1, sticky=tk.W+tk.E)
numSimilarityCB.grid(row=0, column=2, sticky=tk.W+tk.E)

uriEqualityCB.grid(row=1, column=0, sticky=tk.W+tk.E)
ngramCB.grid(row=1, column=1, sticky=tk.W+tk.E)
levenshteinCB.grid(row=1, column=2, sticky=tk.W+tk.E)

mongeElkanCB.grid(row=2, column=0, sticky=tk.W+tk.E)
jaccarCB.grid(row=2, column=1, sticky=tk.W+tk.E)


root.mainloop()