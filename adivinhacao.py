print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("digite seu número: ")
print("Você digitou",chute_str)
chute = int(chute_str)

if(numero_secreto == chute):
    print("Você acertou!")
else:
    if(chute > numero_secreto):
        print("Você errou! 0 seu chute foi maior que o número secreto.")
else:
    print("Você errou! 0 seu chute foi menor que o número secreto.")

print("Fim do jogo!")