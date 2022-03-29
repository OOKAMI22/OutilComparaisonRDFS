import PySimpleGUI as sg
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)
from fonctions import *
from rdflib import *

fileName1 = "source.ttl.txt"
fileName2 = "target.ttl.txt"
fileNameRes = "resultat.ttl"

g1 = Graph()
g2 = Graph()

g1.parse(fileName1)
g2.parse(fileName2)

openFile(fileNameRes)

initialiseurP = {"clef": 0, "titre": 0, "note": 0, "genre": 0, "compositeur": 0, "opus": 0}
initialiseurF = {"jaro": 0, "jaccar": 0, "monge_elkan": 0, "numSimilarity": 0, "ngram1": 0, "ngram2": 0,
                 "levenshtein": 0, "jaroWrinkler": 0, "uriEquality": 0}
seuil = 0.5

layout = [[sg.T(
    "                                                                      OUTIL COMPARAISON RDF (F22)         ")],
          [sg.T("")],
          [sg.T("Choisissez les propriétés à comparer"), sg.T("                         Choisissez les mesures"), ],
          [sg.T("                   "), sg.Checkbox('Clef', default=False, key="ClefC"),
           sg.T("                                      "), sg.Checkbox('Jaro', default=False, key="JaroC"),
           sg.T("              "), sg.InputText(key='1')],
          [sg.T("                   "), sg.Checkbox('Titre', default=False, key="TitreC"),
           sg.T("                                      "), sg.Checkbox('Jaccar', default=False, key="JaccarC"),
           sg.T("          "), sg.InputText(key='2')],
          [sg.T("                   "), sg.Checkbox('Note', default=False, key="NoteC"),
           sg.T("                                     "), sg.Checkbox('Monge Elkan', default=False, key="MongeC"),
           sg.T(" "), sg.InputText(key='3')],
          [sg.T("                   "), sg.Checkbox('Genre', default=False, key="GenreC"),
           sg.T("                                   "),
           sg.Checkbox('NumSimilarity', default=False, key="NumSimilarityC"), sg.T(""), sg.InputText(key='4')],
          [sg.T("                   "), sg.Checkbox('Compositeur', default=False, key="CompositeurC"),
           sg.T("                          "), sg.Checkbox('Ngram', default=False, key="NgramC"), sg.T("           "),
           sg.InputText(key='5')],
          [sg.T("                   "), sg.Checkbox('Opus', default=False, key="OpusC"),
           sg.T("                                              Ngram Size       "), sg.InputText(key='5-2')],
          [sg.T("                                                                            "),
           sg.Checkbox('Levenshtein', default=False, key="LevenshteinC"), sg.T("    "), sg.InputText(key='6')],
          [sg.T("                                                                            "),
           sg.Checkbox('JaroWrinkler', default=False, key="JaroWrinklerC"), sg.T("   "), sg.InputText(key='7')],
          [sg.T("                     Seuil"), sg.InputText(size=(10, 2), key='0'), sg.T("                       "),
           sg.Checkbox('uriEquality', default=False, key="UriEqualityC"), sg.T("      "), sg.InputText(key='8')],
          [sg.T("")],
          [sg.T("                                                                                         "),
           sg.Button('Submit', size=(20, 4))]]

###Setting Window
window = sg.Window('Outil RDF', layout, size=(700, 500))

###Showing the Application, also GUI functions can be placed here.

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == 'Submit':
        if values['ClefC'] == True:
            initialiseurP["clef"] = 1
        else:
            initialiseurP["clef"] = 0
        if values['TitreC'] == True:
            initialiseurP["titre"] = 1
        else:
            initialiseurP["titre"] = 0
        if values['NoteC'] == True:
            initialiseurP["note"] = 1
        else:
            initialiseurP["note"] = 0
        if values['GenreC'] == True:
            initialiseurP["genre"] = 1
        else:
            initialiseurP["genre"] = 0
        if values['CompositeurC'] == True:
            initialiseurP["compositeur"] = 1
        else:
            initialiseurP["compositeur"] = 0
        if values['OpusC'] == True:
            initialiseurP["opus"] = 1
        else:
            initialiseurP["opus"] = 0

        if values['JaroC'] == True:
            initialiseurF["jaro"] = float(values['1'])
        else:
            initialiseurF["jaro"] = 0
        if values['JaccarC'] == True:
            initialiseurF["jaccar"] = float(values['2'])
        else:
            initialiseurF["jaccar"] = 0
        if values['MongeC'] == True:
            initialiseurF["monge_elkan"] = float(values['3'])
        else:
            initialiseurF["monge_elkan"] = 0
        if values['NumSimilarityC'] == True:
            initialiseurF["numSimilarity"] = float(values['4'])
        else:
            initialiseurF["numSimilarity"] = 0
        if values['NgramC'] == True:
            initialiseurF["ngram1"] = float(values['5'])
            initialiseurF["ngram2"] = int(values['5-2'])
        else:
            initialiseurF["ngram1"] = 0
            initialiseurF["ngram2"] = 0

        if values['LevenshteinC'] == True:
            initialiseurF["levenshtein"] = float(values['6'])
        else:
            initialiseurF["levenshtein"] = 0
        if values['JaroWrinklerC'] == True:
            initialiseurF["jaroWrinkler"] = float(values['7'])
        else:
            initialiseurF["jaroWrinkler"] = 0
        if values['UriEqualityC'] == True:
            initialiseurF["uriEquality"] = float(values['8'])
        else:
            initialiseurF["uriEquality"] = 0
        seuil = float(values['0'])
        print("seuil : ", seuil)
        print("clef : ", initialiseurP["clef"])
        print("titre : ", initialiseurP["titre"])
        print("note : ", initialiseurP["note"])
        print("genre : ", initialiseurP["genre"])
        print("compositeur : ", initialiseurP["compositeur"])
        print("opus : ", initialiseurP["opus"])
        print("jaro : ", initialiseurF["jaro"])
        print("jaccar : ", initialiseurF["jaccar"])
        print("monge_elkan : ", initialiseurF["monge_elkan"])
        print("numsimilarity : ", initialiseurF["numSimilarity"])
        print("ngram : ", initialiseurF["ngram1"])
        print("ngram size : ", initialiseurF["ngram2"])
        print("lavenshtein : ", initialiseurF["levenshtein"])
        print("jaroWrinkler : ", initialiseurF["jaroWrinkler"])
        print("uriEquality : ", initialiseurF["uriEquality"])
        print("-")
        compareExpressions(g1, g2, initialiseurP["clef"], initialiseurP["titre"], initialiseurP["genre"],
                           initialiseurP["opus"], initialiseurP["note"], initialiseurP["compositeur"],
                           initialiseurF["jaro"], initialiseurF["jaroWrinkler"], initialiseurF["numSimilarity"],
                           initialiseurF["uriEquality"], initialiseurF["ngram1"], initialiseurF["ngram2"],
                           initialiseurF["jaccar"], initialiseurF["monge_elkan"], initialiseurF["levenshtein"], seuil)

window.close()
