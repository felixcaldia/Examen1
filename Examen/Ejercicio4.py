# from random import randrange --> puedes llamar al metodo sin tener q poner instancia delante

import random
from graficar2 import grafic

def lectura():
    comptaPersonas = random.randint(0, 1) 
    return comptaPersonas

listapersones=[]
minuts=0

#codi principal
while minuts<10:   #contador != 100:  
    contador=0
    for segons in range(60):
        contador += lectura() #recoge dos datos y hacemos una matriz                                               
    minuts+=1
    listapersones.append(contador)
print(listapersones)   
grafic(listapersones)

'''

    print('hola mundo')
'''