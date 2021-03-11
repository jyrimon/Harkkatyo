###########################################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Jyri Montonen
# Opiskelijanumero: 0542040
# Päivämäärä: 16.11.2020
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto: ohjelmointiopas,piazza-keskustelufoorumi
# HUOM! KAIKKI KURSSIN TEHTÄVÄT OVAT HENKILÖKOHTAISIA!
###########################################################################################
import HT_kirjasto


def paaohjelma():
    
    lista=[]
    lista2=[]
    
    while(True):
        
        valinta = HT_kirjasto.valikko()

        if valinta == 1:
            HT_kirjasto.tiedostonLukeminen(lista)
            print("")

        elif valinta == 2:
            HT_kirjasto.tiedostonAnalysointi(lista,lista2)
            print("")
            
        elif valinta == 3:
            HT_kirjasto.tietojenTallentaminen(lista2)
            print("")
            
        elif valinta == 0:
            print("Kiitos ohjelman käytöstä.")
            break
        
        else:
            print("Valintaa ei tunnistettu, yritä uudelleen.")
            
    return None

paaohjelma()
