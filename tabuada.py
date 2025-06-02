import time

multiplicador = int(input("Digite o número para ver a tabuada: "))

for i in range(1, 11):
    resultado = multiplicador * i
    print(f"{multiplicador} x {i} = {resultado}")
    time.sleep(0.5)