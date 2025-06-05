import random
jogador = (input("Sua jogada: ")).lower()
jogadas = ["pedra", "papel", "tesoura"]
mao = random.choice(jogadas)
print(mao)

if jogador == mao:
    print("Empate")

elif jogador == "pedra" and mao == "tesoura":
    print("Ganhou")

elif jogador == "papel" and mao == "pedra":
    print("ganhou")

elif jogador == "tesoura" and mao == "papel":
    print("ganhou")

else:
    print("perdeu")
