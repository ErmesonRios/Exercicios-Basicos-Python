import time
multiplicador = int(input("Digite o Numero: "))

for i in range(1,11):
    mult = i * multiplicador
    if multiplicador == 0:
        print("e zero")
        break
    print(f"resutado {multiplicador} x {i} = {mult}")
    time.sleep(1)
    