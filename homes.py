from multiprocessing import Process
from random import uniform
from random import randint
import os
import time 
import threading
import sys
import sysv_ipc

key2 = 110 
stopKey = 111
mqHomeToHome = sysv_ipc.MessageQueue(key2, sysv_ipc.IPC_CREAT)
mqStop = sysv_ipc.MessageQueue(stopKey, sysv_ipc.IPC_CREAT)

key1 = 106 
mqHomeToMarket = sysv_ipc.MessageQueue(key1, sysv_ipc.IPC_CREAT)

tabTest = [(2, -110), (3, -156)]

maison["typeShare"] = randint(1,3)
maison["tauxConso"] = randint(9000, 15000) # taux à l'année entre 7 000 et 12 000 kWh
maison["initProduct"] = randint(7000, 10000) #production par an entre 5 000 et 10 000 kWh
maison["energie"] = int((maison.get("initProduct") - maison.get("tauxConso"))/365.25)

##def print(self):
 ##   print("La maison numéro " ,self.id," a une énergie de ",self.energie,"kWh, une production de ",self.initProduct," et un taux de conso de ",self.tauxConso,"")


def creationVillage(n): 
    tab = [] * n 
    

tabMaison = []
creationVillage(tabMaison, 3)
print(tabMaison)



"""def maisonDsBesoin(mq, tab):
    i = 0
    while i < len(tab) :
        print("in home")
        message = tab[i]
        message = str(message)
        message = message.encode()
        mq.send(message)
        print("message envoyé")
        time.sleep(0.2)
        i+=1

def search(mq): #recherche de l'indice de la maison avec le moins d'énergie
    tabMaisonBesoin = []
    print(tabMaisonBesoin)
    for _ in range (0, 10):
        message,t = mq.receive()
        message = tuple(message.decode())
        tabMaisonBesoin.append(message)
        print(tabMaisonBesoin)
 

maisonDsBesoin(mqHomeToHome, tabTest)   
search(mqHomeToHome)

def besoin(m.energie): 
    if m.typeShare == 1 : 
        while m.energie > 0:
            search(mqHomeToHome)
            give(.energie)

    if (m.energie) > 0:
        if m.typeShare == 1: #give away 
            if search(tabMaison) =! null: #entre dans la boucle seulement si des maison dans le besoin existent
                give(m.energie, tabMaison[search(tabMaison)].energie)
            else: #dans le cas où plus aucune maison sont dans le besoin la maison de type 1 perd son energie en plus
                m.energie = 0 

        if m.typeShare == 2: #sell hon the market

                
        if m.typeShare == 3: #sell if no takersdef search(tab []):
            if search(tabMaison) =! null: #entre dans la boucle seulement si des maison dans le besoin existent
                give(m.energie, tabMaison[search(tabMaison)].energie)
            else: #dans le cas où plus aucune maison sont dans le besoin la maison de type 1 perd son energie en plus 
                m.typeShare = 2
                besoin(m.energie) #récursivité"""
                 


"""def search(mq): #recherche de l'indice de la maison avec le moins d'énergie
    message,t = mq.receive  #Lecture d'un tableau de 2 valeurs par maison (ID, énergie)
    
    for i in len(mq):
        tabMaisonBesoin[i] = message[i].decode()

    mini = tabMaison[0]
    longueur=len(tabMaison)
    for i in range(longueur):
        if tabMaison[i] <= mini and tabMaison[i].energie < 0 : 
            indiceMin = i 
    return indiceMin"""

"""def give (m.energie, mB.energie): #fonction de transfert d'energie entre deux maisons
    if abs(mB.energie) <= m.energie :
        mB.energie = 0
        m.energie = m.energie - abs(mB.energie)
        if search(tabMaison) =! null: #récursivité
            mB.energie = tabMaison[search(tabMaison)].energie
            give (m.energie, mB.energie)
    else:
        mB.energie = mB.energie + m.energie
        m.energie = 0
        


if __name__ == '__main__':
    p = 
    p.start()
    p.join()"""

mqHomeToHome.remove()
mqHomeToMarket.remove()