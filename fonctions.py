import psm as psm
from rdflib import *
from rdflib import *
import SPARQLWrapper
from SPARQLWrapper import SPARQLWrapper, JSON
import warnings
import py_stringmatching as psm


def getExpressions(graphe):
    # je recupere toutes les expressions de type F22
    req = """
  PREFIX efrbroo: <http://erlangen-crm.org/efrbroo/>
  SELECT DISTINCT ?expression
  WHERE{
    ?expression a efrbroo:F22_Self-Contained_Expression.
  }
  """
    reqResultat = graphe.query(req)

    return reqResultat


def getPropriete(propriete, expression, graphe):
    if (propriete == "clef"):
        req = """ 
	    PREFIX mus: <http://data.doremus.org/ontology#>
		SELECT ?expression ?clef
		WHERE{
			?expression mus:U11_has_key ?clef.
			FILTER(isIRI(?clef)).
		}"""
    elif (propriete == "note"):
        req = """ 
		PREFIX ecrm: <http://erlangen-crm.org/current/>
		SELECT ?expression ?note
		WHERE{
			?expression ecrm:P3_has_note ?note.
		}"""
    elif (propriete == "opus"):
        req = """ 
		PREFIX mus: <http://data.doremus.org/ontology#>
		SELECT ?expression ?opus
		WHERE{
			?expression mus:U17_has_opus_statement / mus:U42_has_opus_number ?opus.
		}"""
    elif (propriete == "compositeur"):
        req = """
     PREFIX ecrm: <http://erlangen-crm.org/current/>
		 PREFIX efrbroo: <http://erlangen-crm.org/efrbroo/>
		 SELECT ?expression ?compositeur
		 WHERE{
			 ?expression a efrbroo:F22_Self-Contained_Expression .
			 ?expCreation efrbroo:R17_created ?expression ;
			 ecrm:P9_consists_of / ecrm:P14_carried_out_by ?compositeur ;
		 }"""
    elif (propriete == "titre"):
        req = """
     PREFIX ecrm: <http://erlangen-crm.org/current/>
		 SELECT ?expression ?title
		 WHERE {
			 ?expression ecrm:P102_has_title ?title .
            }"""
    elif (propriete == "genre"):
        req = """
		 PREFIX mus: <http://data.doremus.org/ontology#>
		 SELECT ?expression ?genre
		 WHERE {
			 ?expression mus:U12_has_genre ?genre.
			 FILTER (isIRI(?genre))
            }"""
    else:
        return 0

    # pour le binding
    reqResultat = graphe.query(req, initBindings={'expression': expression})
    resultat = []
    # print(reqResultat)
    for i in reqResultat:
        resultat.append(str(i[1]))

    return resultat


# Fonctions de pretraiment pour les URI afin de ne pas biaser le calcul
def isURL(str):
    return str.startswith("http")


def tokenisation(str):
    if (type(str) == list):
        token = []
        for elem in str:
            token = list(set(token) | set(elem.split(" ")))
        return token
    elif (isURL(str)):
        token = str.split("/")[-2:]
        return token
    else:
        return str.split(" ")


def pretraitementURL(url):
    token = tokenisation(url)
    resultat = "".join(token)
    return resultat


# Fonctions de comparaison de Strings/URL
def stringEquality(str1, str2):
    if (len(str1) == 0 or len(str2) == 0):
        return 0.0
    elif (str1 == str2):
        return 1.0
    else:
        return 0.0


def jaro(str1, str2):
    if (len(str1) == 0 or len(str2) == 0):
        return 0.0
    else:
        return psm.Jaro().get_sim_score(str(str1), str(str2))


def jaroWrinkler(str1, str2):
    if (len(str1) == 0 or len(str2) == 0):
        return 0.0
    else:
        return psm.JaroWinkler().get_sim_score(str1, str2)


def Jaccard(str1, str2):
    if (len(str1) == 0 or len(str2) == 0):
        return 0.0
    else:
        str1 = tokenisation(str1)
        str2 = tokenisation(str2)
        print(str1)
        print(str2)
        return psm.Jaccard().get_sim_score(str1, str2)


def Ngram(s1, s2, s):
    s1 = pretraitementURL(s1)
    s2 = pretraitementURL(s2)
    print(s1)
    print(s2)
    i = 0
    id = 0
    while ((i + s) <= len(s1)) or ((i + s) <= len(s2)):
        # print(s1[i:i + s], " == ", s2[i:i + s] + "     ?")
        if s1[i:i + s] == s2[i:i + s]:
            # print("OUI")
            id += 1
        i += 1
    if ((min(len(s1), len(s2)) - s) < 0):
        # print("trop grand")
        return 0
    return (id) / (min(len(s2), len(s1)) - s + 1)


def mongeElkan(str1, str2):
    if (len(str1) == 0 or len(str2) == 0):
        return 0.0
    else:
        str1 = tokenisation(str1)
        str2 = tokenisation(str2)
        return psm.MongeElkan().get_raw_score(str1, str2)


def levenshtein(str1, str2):
    if (len(str1) == 0 or len(str2) == 0):
        return 0.0
    else:
        str1 = pretraitementURL(str1)
        str2 = pretraitementURL(str2)
        return psm.Levenshtein().get_sim_score(str1, str2)


def numSimilarity(num1, num2):
    if (len(num1) == 0 or len(num2) == 0):
        return 0.0
    elif (num1 == num2):
        return 1.0
    else:
        return 0.0


def uriEquality(uri1, uri2):
    if (len(uri1) == 0 or len(uri2) == 0):
        return 0.0
    elif (pretraitementURL(uri1) == pretraitementURL(uri2)):
        return 1.0
    else:
        return 0.0


# compare(expression1, expression2, propriete)
# expression1 et expression2 sont les expressions a comparer
# propriete est la propriete a comparer
# la fonction renvoie un score entre 0 et 1
# si la propriete est une propriete de type string, la fonction compare les strings
# si la propriete est une propriete de type num, la fonction compare les nombres
# si la propriete est une propriete de type uri, la fonction compare les uris

def compare(l1, l2, fonction):
    somme = []
    for elem1 in l1:
        for elem2 in l2:
            print(elem1, elem2)
            somme.append(fonction(elem1, elem2))
    print(min(somme))
    return max(somme)


def compareNgram(l1, l2, n, fonction):
    somme = []
    for elem1 in l1:
        for elem2 in l2:
            print(elem1, elem2)
            somme.append(fonction(str(elem1), str(elem2), n))
    print(min(somme))
    return max(somme)


def compareProriete(exp1, exp2, g1, g2, proprieteStr, jaro1, jaroWrinkler1, numSimilarity1, uriEquality1, ngram1,
                    ngram2, jaccard1, monge_elkan1, levenshtein1):
    nombre = 0
    somme = 0
    propriete1 = []
    propriete2 = []
    # print(exp1)
    for row in exp1:
        # print(getPropriete(proprieteStr, row, g1))
        propriete1.append(getPropriete(proprieteStr, row, g1))
    for row in exp2:
        propriete2.append(getPropriete(proprieteStr, row, g2))
    if jaro1 > 0:
        somme += compare(propriete1, propriete2, jaro) * jaro1
        nombre += jaro1
    if jaroWrinkler1 > 0:
        somme += compare(propriete1, propriete2, jaroWrinkler) * jaroWrinkler1
        nombre += jaroWrinkler1
    if numSimilarity1 > 0:
        somme += compare(propriete1, propriete2, numSimilarity) * numSimilarity1
        nombre += numSimilarity1
    if uriEquality1 > 0:
        somme += compare(propriete1, propriete2, uriEquality) * uriEquality1
        nombre += uriEquality1
    if ngram1 > 0:
        somme += compareNgram(propriete1, propriete2, ngram2, Ngram) * ngram1
        nombre += ngram1
    if jaccard1 > 0:
        somme += compare(propriete1, propriete2, Jaccard) * jaccard1
        nombre += jaccard1
    if monge_elkan1 > 0:
        somme += compare(propriete1, propriete2, mongeElkan) * monge_elkan1
        nombre += monge_elkan1
    if levenshtein1 > 0:
        somme += compare(propriete1, propriete2, levenshtein) * levenshtein1
        nombre += levenshtein1

    return somme / nombre


# fonction qui ecrit sur le fichier de sortie les resultats de la comparaison
def createFile(fileName, exp1, exp2):
    content = "<" + str(exp1) + "> <http://www.w3.org/2002/07/owl#sameAs> <" + str(exp2) + "> .\n"
    with open(fileName, "a") as f:
        f.write(content)
        f.close()


# fonction qui ouvre un fichier en écriture et qui le ferme
def openFile(fileName):
    with open(fileName, "w") as f:
        f.close()


def compareExpressions(g1, g2, clef, titre, genre, opus, note, compositeur, jaro1, jaroWrinkler1, numSimilarity1,
                       uriEquality1, ngram1, ngram2, jaccard1, monge_elkan1, levenshtein1, seuil):
    expressions1 = getExpressions(g1)

    expressions2 = getExpressions(g2)

    for exp1 in expressions1:
        print("Expression  : " + str(exp1))
        for exp2 in expressions2:
            somme = 0
            nombre = 0
            if clef > 0:
                somme += compareProriete(exp1, exp2, g1, g2, "clef", jaro1, jaroWrinkler1, numSimilarity1, uriEquality1,
                                         ngram1, ngram2, jaccard1, monge_elkan1, levenshtein1)
                nombre += 1
            if titre > 0:
                somme += compareProriete(exp1, exp2, g1, g2, "titre", jaro1, jaroWrinkler1, numSimilarity1,
                                         uriEquality1, ngram1, ngram2, jaccard1, monge_elkan1, levenshtein1)
                nombre += 1
            if genre > 0:
                somme += compareProriete(exp1, exp2, g1, g2, "genre", jaro1, jaroWrinkler1, numSimilarity1,
                                         uriEquality1, ngram1, ngram2, jaccard1, monge_elkan1, levenshtein1)
                nombre += 1
            if opus > 0:
                somme += compareProriete(exp1, exp2, g1, g2, "opus", jaro1, jaroWrinkler1, numSimilarity1, uriEquality1,
                                         ngram1, ngram2, jaccard1, monge_elkan1, levenshtein1)
                nombre += 1
            if note > 0:
                somme += compareProriete(exp1, exp2, g1, g2, "note", jaro1, jaroWrinkler1, numSimilarity1, uriEquality1,
                                         ngram1, ngram2, jaccard1, monge_elkan1, levenshtein1)
                nombre += 1
            if compositeur > 0:
                somme += compareProriete(exp1, exp2, g1, g2, "compositeur", jaro1, jaroWrinkler1, numSimilarity1,
                                         uriEquality1, ngram1, ngram2, jaccard1, monge_elkan1, levenshtein1)
                nombre += 1
            if (somme / nombre) >= seuil:
                createFile("resultat.ttl", exp1.expression, exp2.expression)
    print("c'est finis")
