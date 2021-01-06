import sysv_ipc


key1 = 1 #maison de type 1 ou 3
key2 = 2 #maison de type 2 (ou 3)
 
mq1 = sysv_ipc.MessageQueue(key1, sysv_ipc.IPC_CREX) #message queue de la plateforme de don
mq2 = sysv_ipc.MessageQueue(key2, sysv_ipc.IPC_CREX) #message queue de la plateforme de vente
 
tabMaison[]

#Création d'un tableau de message queue
def










def searchServer(MessageQueue, tabMaison): #recherche des maisons avec trop d'énergie et remplissage de tableau
    longueur=len(tabMaison)
    for i in range(longueur):
        if tabMaison[i].energie > 0 : 
            if tabMaison[i].typeShare == 1:
                message = str(tabMaison[i].energie).encode()
                mq1.send(message)
            if tabMaison[i].typeShare == 2:
                message = str(tabMaison[i].energie).encode()
                mq2.send(message)
        else:








 
value = 1
while value:
    try:
        value = int(input())
    except:
        print("Input error, try again!")
    message = str(value).encode()
    mq.send(message)
 
mq.remove()