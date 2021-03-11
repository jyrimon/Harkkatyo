###########################################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Jyri Montonen
# Opiskelijanumero: 0542040
# Päivämäärä: 16.11.2020
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto: ohjelmointiopas,piazza-keskustelufoorumi
# HUOM! KAIKKI KURSSIN TEHTÄVÄT OVAT HENKILÖKOHTAISIA!
###########################################################################################

import datetime
import sys

class DATA:
    paivamaara=None
    pvmjakello=None
    kellonaika=0
    paino=0

class TULOKSET:
    pvmPienin=None
    painoMin=0
    pvmSuurin=None
    painoMax=0
    vali=0
    painoYhteensa=0
    painoKeskimaarin=0
        
    
def valikko():
    print("Mitä haluat tehdä:")
    print("1) Lue kuormatiedot")
    print("2) Analysoi kuormatiedot")
    print("3) Tallenna kuormien tulostiedot")
    print("0) Lopeta")
    while(True):
        try:
            valinta=int(input("Valintasi: "))
            break
        except ValueError:
            print("Anna valinta kokonaislukuna.")
    return valinta

def tiedostonLukeminen(lista):
    
    luettava_tiedosto=input("Anna kuormatietotiedoston nimi: ")
    
    try:
        tiedosto=open(luettava_tiedosto,'r',encoding="utf-8")
    except Exception:
        print("Tiedoston '"+str(luettava_tiedosto)+"' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
        
    lista.clear() #Tyhjennetään lista.   
    try:
        koko=0
        tiedosto.readline()
        while(True):
            rivi=tiedosto.readline()
            if len(rivi) == 0:
                break
            rivi=rivi[:-1]
            sarakkeet=rivi.split(';')
            tiedot=DATA()
            tiedot.paivamaara=datetime.datetime.strptime(sarakkeet[0],"%d.%m.%Y")
            tiedot.kellonaika=datetime.datetime.strptime(sarakkeet[1],"%H:%M:%S")
            tiedot.pvmjakello=datetime.datetime.strptime(sarakkeet[0] + sarakkeet[1],"%d.%m.%Y" "%H:%M:%S")
            tiedot.paino=int(sarakkeet[2])
            lista.append(tiedot)
            koko=koko+1
        tiedosto.close()
    except Exception:
        print("Tiedoston '"+str(luettava_tiedosto)+"' lukeminen epäonnistui.")
        sys.exit(0)
        
    print("Tiedosto '"+str(luettava_tiedosto)+"' luettu, "+str(koko)+" riviä.")
    return lista

def tiedostonAnalysointi(lista,lista2):
    #Tarkistetaan onko tiedot luettu ennen niiden analysointia.
    #Jos ei ole palataan pääohjelmaan ja annetaan virheilmoitus.

    lista3=[]
    lista4=[]
    
    if len(lista) == 0:
        print("Lista on tyhjä. Lue ensin tiedosto.")
        return None

    
    #Luodaan olio jonne lisätään tuloksia.
    tiedot2=TULOKSET()
    
    #Selvitetään pienin ja suurin painokuorma ja lisätään olioon
    painoMin = lista[0].paino
    painoMax = lista[0].paino
    
    for i in lista:
        if painoMin > i.paino:
            painoMin = i.paino
            tiedot2.painoMin=painoMin
            
        if painoMax < i.paino:
            painoMax = i.paino
            tiedot2.painoMax=painoMax

          
    #Selvitetään jokainen päivämäärä,jona tullut minimikuorma ja lisätään päivämäärä listaan
    #Selvitetään listan pienin päivämäärä ja lisätään se olioon
    indeksi=0
    pieni=None
    for i in lista:
        if i.paino==painoMin:
            indeksi=indeksi
            pieni=datetime.datetime.strftime(lista[int(indeksi)].pvmjakello,"%d.%m.%Y %H:%M:%S")
            lista3.append(datetime.datetime.strptime(pieni,"%d.%m.%Y %H:%M:%S"))
        indeksi += 1
    
    tiedot2.pvmPienin=(datetime.datetime.strftime(min(lista3),"%d.%m.%Y"))
    
    #Selvitetään jokainen päivämäärä,jona tullut maksimikuorma ja lisätään päivämäärä listaan
    #Selvitetään listan suurin päivämäärä ja lisätään se olioon
    
    indeksi2=0
    suuri=None
                          
    for i in lista:
        if i.paino == painoMax:
            ideksi2=indeksi2
            suuri=datetime.datetime.strftime(lista[int(indeksi2)].pvmjakello,"%d.%m.%Y %H:%M:%S")              
            lista4.append(datetime.datetime.strptime(suuri,"%d.%m.%Y %H:%M:%S"))
        indeksi2 += 1
        
    tiedot2.pvmSuurin=(datetime.datetime.strftime(max(lista4),"%d.%m.%Y"))
    
    #Selvitetään kuinka monta päivää on pienimmän ja suurimman kuorman välillä
    #ja lisätään tieto olioon.

    #paiva1=min(lista3)
    #paiva2=max(lista4)
    
    paiva_pieni=datetime.datetime.strftime(min(lista3),"%d.%m.%Y %H:%M:%S")
    paiva_suuri=datetime.datetime.strftime(max(lista4),"%d.%m.%Y %H:%M:%S")
    pvm_pienin=datetime.datetime.strptime(paiva_pieni,"%d.%m.%Y %H:%M:%S")
    pvm_suurin=datetime.datetime.strptime(paiva_suuri,"%d.%m.%Y %H:%M:%S")
    
    tulos=(pvm_suurin-pvm_pienin).days
    tiedot2.vali=tulos
           
    
   
    #Selvitetään kuinka paljon jätettä tuli yhteensä ja kuinka paljon keskimäärin
    #Lisätään tiedot olioon
    
    koko=0
    painoYhteensa=0
    for i in lista:
        luku=i.paino
        painoYhteensa += luku
        koko=koko+1
    tiedot2.painoYhteensa=painoYhteensa
    tiedot2.painoKeskimaarin=int(painoYhteensa/koko)     
    

    #Selvitetään miltä ajalta tietoja on analysoitu.
    pvmMin=lista[0].paivamaara
    pvmMax=lista[0].paivamaara

    for i in lista:
        if pvmMin > i.paivamaara:
            pvmMin = i.paivamaara
        
        if pvmMax < i.paivamaara:
            pvmMax = i.paivamaara
            
    ekaPaiva=datetime.datetime.strftime(pvmMin,"%d.%m.%Y")
    vikaPaiva=datetime.datetime.strftime(pvmMax,"%d.%m.%Y")
    print("Data analysoitu ajalta "+str(ekaPaiva)+" - "+str(vikaPaiva)+".")

    #Lisätään olio listaan ja palauteaan lista paluuarvona
    lista2.append(tiedot2)
    return lista2


def tietojenTallentaminen(lista2):
    #Tarkistetaan, onko tiedot analysoitu
    #ja jos ei ole palataan päähojelmaan ja annetaan virheilmoitus
    
    if len(lista2)==0:
        print("Ei tuloksia. Analysoi data ennen tallennusta.")
        return None
    
    kirjoitettava_tiedosto=input("Anna tulostiedoston nimi: ")
    
    print("Pienin jätekuorma tuli "+str(lista2[0].pvmPienin)+" ja oli "+str(lista2[0].painoMin)+" kg.")
    print("Suurin jätekuorma tuli "+str(lista2[0].pvmSuurin)+" ja oli "+str(lista2[0].painoMax)+" kg.")
    print("Pienimmän ja suurimman kuorman toimitusten välissä oli "+str(lista2[0].vali)+" päivää.")
    print("Analyysijaksolla jätettä tuli yhteensä "+str(lista2[0].painoYhteensa)+" kg.")
    print("Keskimäärin jätekuorma oli "+str(lista2[0].painoKeskimaarin)+" kg.")
    
    try:
        tiedosto=open(kirjoitettava_tiedosto,'w',encoding="utf-8")
    except Exception:
        print("Tiedoston '"+str(kirjoitettava_tiedosto)+"' käsittelyssä virhe, lopetetaan.")
        sys.exit(0) 
    try:
        tiedosto.write("Pienin jätekuorma tuli "+str(lista2[0].pvmPienin)+" ja oli "+str(lista2[0].painoMin)+" kg.\n")
        tiedosto.write("Suurin jätekuorma tuli "+str(lista2[0].pvmSuurin)+" ja oli "+str(lista2[0].painoMax)+" kg.\n")
        tiedosto.write("Pienimmän ja suurimman kuorman toimitusten välissä oli "+str(lista2[0].vali)+" päivää.\n")
        tiedosto.write("Analyysijaksolla jätettä tuli yhteensä "+str(lista2[0].painoYhteensa)+" kg.\n")
        tiedosto.write("Keskimäärin jätekuorma oli "+str(lista2[0].painoKeskimaarin)+" kg.\n")
        tiedosto.close()        
    except Exception:
        print("Tiedoston '"+str(kirjoitettava_tiedosto)+"' kirjoittaminen epäonnistui.")
        sys.exit(0)
        
    print("Tulokset tallennettu tiedostoon '"+str(kirjoitettava_tiedosto)+"'.")
    return None

    
    
    
    
  
    
    

   
    
  
    
    
    

