from multiprocessing import Process, Array
import os
import random
import time

print("Début")
année = int(input("Année : "))
mois = int(input("Mois : "))
jours = int(input("Jours : "))
print("Fin")
annéeF = int(input("Année : "))
moisF = int(input("Mois : "))
joursF = int(input("Jours : "))
a = -5
temp = 3
tic = 0
event = 0

def calculTemp(jours, mois):
    global a
    if jours == 21 and mois == 12:
        a = -5
    if jours == 21 and mois == 3:
        a = 15
    if jours == 21 and mois == 6:
        a = 25 
    if jours == 21 and mois == 9:
        a = 5

while année < annéeF or mois < moisF or jours < joursF:
    print("Date : ", jours, "/", mois, "/", année,  temp, "°C")
    calculTemp(jours, mois)
    event = random.randint(1,30)
    temp = random.randint(0,10) + a
    jours += 1
    tic += 1
    if jours == 32 and mois == 1:
        jours = 1 
        mois += 1
    if jours == 29 and mois == 2:
        jours = 1 
        mois += 1
    if jours == 32 and mois == 3:
        jours = 1 
        mois += 1
    if jours == 31 and mois == 4:
        jours = 1 
        mois += 1
    if jours == 32 and mois == 5:
        jours = 1 
        mois += 1
    if jours == 31 and mois == 6:
        jours = 1 
        mois += 1
    if jours == 32 and mois == 7:
        jours = 1 
        mois += 1
    if jours == 32 and mois == 8:
        jours = 1 
        mois += 1
    if jours == 31 and mois == 9:
        jours = 1 
        mois += 1
    if jours == 32 and mois == 10:
        jours = 1 
        mois += 1
    if jours == 31 and mois == 11:
        jours = 1 
        mois += 1
    if jours == 32 and mois == 12:
        jours = 1 
        mois += 1
    if mois == 13:
        mois = 1
        année += 1

    time.sleep(0.02)

    sharedmemory[0] = année
    sharedmemory[1] = mois
    sharedmemory[2] = jours
    sharedmemory[3] = temp
    sharedmemory[4] = event