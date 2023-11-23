#Hány Alma/alma van a listában?
def elsofeladat(szoveg_lista):
  szamlalo=0
  for i in range(0,len(szoveg_lista),1):
      if szoveg_lista[i]<0:
          szamlalo+=1
      print(szamlalo)
      return szamlalo


#Hány Sz betűvel kezdődő szöveg van a listában?
def masodikfeladat(szoveg_lista):
        db=0
        for i in range(0,len(szoveg_lista),1):
            if szoveg_lista[i].rfind("Sz") or szoveg_lista[i].rfind("sz"):
                db+=1
        print(f"Sz betűk száma {db}")
        return db

#Melyik a leghosszab szó? Mekkora a hossza? Hányadik helyen áll a listában?
def harmadikfeladat(szoveg_lista):
    