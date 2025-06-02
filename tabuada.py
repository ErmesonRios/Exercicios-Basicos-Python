import time


while True:
    multiplicador = int(input("Digite o número para ver a tabuada ou 0 para sair: "))
    if multiplicador == 0:
          break
    for i in range(1, 11):
        resultado = multiplicador * i
        print(f"{multiplicador} x {i} = {resultado}")
        time.sleep(0.5)