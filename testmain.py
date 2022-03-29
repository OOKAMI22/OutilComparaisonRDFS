import warnings

warnings.filterwarnings("ignore", category=FutureWarning)
from fonctions import *
from rdflib import *

fileName1 = "source.ttl.txt"
fileName2 = "target.ttl.txt"

g1 = Graph()
g2 = Graph()

g1.parse(fileName1)
g2.parse(fileName2)

expressions = getExpressions(g1)

initialiseurP = {"clef": 1, "titre": 0, "note": 0, "genre": 0, "compositeur": 0, "opus": 0}
initialiseurF = {"jaro": 1, "jaccar": 0, "monge_elkan": 0, "numSimilarity": 0, "ngram": 0, "levenshtein": 0, "jaroWrinkler": 0,"uriEquality": 0}

#k="clef"
#for row in expressions:
    #print(getPropriete(k, row[0], g1))

print(mon_main(g1, g2, initialiseurP['clef'], initialiseurP['note'], initialiseurP['compositeur'], initialiseurP['opus'], initialiseurP['titre'], initialiseurP['genre'], initialiseurF['jaro'], initialiseurF['jaroWrinkler'], initialiseurF['numSimilarity'], initialiseurF['uriEquality']))



