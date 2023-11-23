import math

#ÍRJ METÓDUST , AMI A PARAMÉTERBEN KAPOTT LSTA ELEMEIT KIRJA A KÉPERNYŐRE
def feladat1(szam_lista):
    for i in range(0,len(szam_lista),1):
        print(szam_lista[i])

#MENNYI A POZITÍV SZÁMOK ÖSSZEGE?-ÖSSZEGZÉS
def feladat2(szam_lista):
    osszegzes=0
    for i in range(0,len(szam_lista),1):
        if szam_lista[i]>0:
            osszegzes+=szam_lista[i]

    print(f"Poztiv számok összeg:{osszegzes}")
    return osszegzes


#HÁNY NEGATÍV SZÁM VAN BENNE?-MEGSZÁMLÁLÁS?-SZÁMLÁLÁS
def feladat3(szam_lista):
    szamlalas=0
    for i in range(0,len(szam_lista),1):
        if szam_lista[i]<0:
            szamlalas+=1
    print(f"A negatív számok száma:{szamlalas}")
    return szamlalas
#HÁNY NEM EGÉSZ SZÁM VAN BENNE? -MEGSZÁMLÁLS-SZÁMOLÁS
def feladat4(szam_lista):
    szamlalo=0
    for i in range(0,len(szam_lista),1):
        if szam_lista[i]!=math.floor(szam_lista[i]):
            szamlalo+=1
    print(f"A nem egész számok száma:{szamlalo}")
    return szamlalo


#MENYI A HÁROMAL OSZTHATÓ SZÁMOK ÁTLAGA? -ÖSSZEGZÁS - SZÁMLÁLÁS
def feladat5(szam_lista):
    szamlalo=0
    for i in range(0,len(szam_lista),1):
        if szam_lista[i] % 3==0:
            szamlalo+=1
        i+=1
    print(f"A hárommal osztható számok átlaga:{szamlalo}")
    return szamlalo
#MEKKORA A LEGNAGYOBB SZÁM?-MAX
def feladat6(szam_lista):
    max=szam_lista[0]
    for i in range(0,len(szam_lista),1):
        if max<szam_lista[i]:
            max=szam_lista[i]
    print(f"A legnagyobb szám összege:{max}")
    return max


#MEKKORA A LEGKISEBB SZÁM?-MAX
def feladat7(szam_lista):
    min=szam_lista[0]
    for i in range(0,len(szam_lista),1):
        if min<szam_lista[i]:
            min=szam_lista[i]
    print(f"A legkisseb szám összege:{min}")
    return min

#MEKKORA A LEGKISSEB ÉS A LEGNAGYOBB SZÁM KÜLÖNBSÉGE?
def feladat8(szam_lista):
    max:float=feladat6(szam_lista)
    min:float=feladat7(szam_lista)
    kulombseg=max - min
    print(kulombseg)
    return kulombseg