#!/usr/bin/env python3

# LAZAR_Mohamed_kholle_1.py
# Opérations sur une liste de nombre entier
# 24/11/2018
# Mohamed Lazar

#Importation des modules 

import argparse
import csv
from statistics import mean

#Listes des options disponibles

parser = argparse.ArgumentParser()
parser.add_argument("-a", nargs="+", help="Ajoute une ou plusieurs valeurs au csv")
parser.add_argument("-c",  action="store_true", help="Supprime toutes les valeurs au csv")
parser.add_argument("-l", action="store_true", help="Affiche le contenu du csv")
parser.add_argument("-s", action="store_true", help="Affiche la valeur maximum contenue dans le csv")
parser.add_argument("--max", action="store_true", help="Affiche la valeur maximum contenue dans le csv")
parser.add_argument("--min", action="store_true", help="Affiche la valeur minimum contenue dans le csv")
parser.add_argument("--moy", action="store_true", help="Affiche la moyenne contenue dans le csv")
parser.add_argument("--sum", action="store_true", help="Affiche la somme des valeurs du csv")
parser.add_argument("-t", action="store_true", help="Trie la liste par ordre croissant")
parser.add_argument("--desc", action="store_true", help="Trie la liste par ordre décroissant")
args = parser.parse_args()

#Initialisation de la variable

liste = []


#On met les droits d'ecriture sur le fichier liste.csv
def writeCsv(value):
    with open("./liste.csv", "w") as file_csv:
        csv_write = csv.writer(file_csv)

        csv_write.writerow(value)

#On met les droits de lecture sur le fichier liste.csv
def readCsv():
    with open("./liste.csv", "r") as file_csv:
        csv_reader = csv.reader(file_csv)
        for ligne in  csv_reader:
            for i in range(0, len(ligne)):
               liste.append(ligne[i])


#On ajoute des valeurs à la liste
def addItems(value):
    liste.append(value)

#On affiche le contenu de la liste
def contentList():
    readCsv()
    for row in liste:
        print(row)

#On supprime toutes les valeurs de la liste
def deleteAll():
    readCsv()
    while len(liste) > 0:
        del liste[0]
    writeCsv(liste)


#On affiche la valeur max contenue dans la liste
def getMaxValue():
    readCsv()
    liste_max = [int(n) for n in liste]
    value_max = max(liste_max)
    print(value_max)


#On affiche la valeur min contenue dans la liste
def getMinValue():
    readCsv()
    liste_min = [int(n) for n in liste]
    value_min = min(liste_min)
    print(value_min)  


#On affiche la moyenne de toutes les valeurs de la liste
def getAverageValue():
    readCsv()
    liste_moy = [int(n) for n in liste]
    value_average = mean(liste_moy)
    print(value_average)


#On affiche la somme de toutes les valeurs de la liste
def getSumValue():
    readCsv()
    liste_sum = [int(n) for n in liste]
    value_sum = sum(liste_sum)
    print(value_sum)


#On trie la liste par ordre croissant
def listeCro():
    readCsv()
    liste_croissant = [int(n) for n in liste]
    liste_croissant.sort()
    writeCsv(liste_croissant)


#On trie la liste par ordre décroissant
def listeDesc():
    readCsv()
    liste_decroissant = [int(n) for n in liste]
    liste_decroissant.sort(reverse = True)
    writeCsv(liste_decroissant)

#On appelle les fonctions selon les conditions

if args.l:
    contentList()

elif args.a:
    readCsv()
    for num in args.a:
        addItems(num)
    writeCsv(liste)

elif args.c:
    deleteAll()

elif args.s:
    if args.max:
        getMaxValue()
    elif args.min:
        getMinValue()
    elif args.moy:
        getAverageValue()
    elif args.sum:
        getSumValue()

elif args.t:
    if args.desc:
        listeDesc()
    else:
        listeCro()
