import time
import os

lista = []
for i in range(1, 100):
    lista.append(i)
    time.sleep(0.1)
for i in lista:
    if i == 46:
        print("Encontrei o número 46!")
        break
    
    print(i)
        