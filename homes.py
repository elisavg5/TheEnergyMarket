from multiprocessing import Process
import os
import time 
import threading
import math
import sy

def Maison(ID):

        typeShare = int(math.random()*3)+1
        cagnotte = 2300
        tauxConso = int(math.random()*5001)+10000 # taux à l'année entre 10 000 et 15 000 kWh

        initProduct = 30 #production par jour en kWh
        energie = - tauxConso/365.25 + initProduct

tabMaison = []

def besoin(energie): 
    if energie < 0:
        i = 0 
        while i < len(tabMaison):
            if tabMaison[i] == null 
                tabMaison[i] = Maison 
            elif 
                i+=

             
    if energie > 0:
        if typeShare == 1 #give away 
            search(tabMaison)
            #là il faut que du coup la maison donne à la maison du tableau qui a le moins d'énergie (la valeur minimum du tableau)
    
        
            if f typeShare == 2 #sell hon the marke

                
if typeShare == 3 #sell if no takersdef search(tab []):
    while   
    



if __name__ == '__main__':
    p = 
    p.start()
    p.join()