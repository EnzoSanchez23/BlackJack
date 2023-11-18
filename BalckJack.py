import random
cartasMao = 0
cartas = [1,2,3,4,5,6,7,8,9,10,11]

escolheCarta = random.randrange(0, len(cartas))
print(escolheCarta)

mao = cartas[escolheCarta]
cartasMao += mao

print("O valor da carta é:" , mao)
 
while(cartasMao < 22):
    print("Gostaria de receber outra carta?")
    resp = input("S/N: ")

    if(resp == "S"):
        NovaEscolhaCarta = random.randrange(0, len(cartas))
        NovaMao = cartas[NovaEscolhaCarta]

        cartasMao += NovaMao
        print("O valor atual da sua mao é:", cartasMao)
    elif(resp == "N"):
        print("Voce deixou de recber cartas!")
        break

if(cartasMao > 21):
    print("Estorou,", cartasMao)
else:
    print("Parabens, voce ganhou o BlackJack!")

print("O valor atual da sua mao é:", cartasMao)













































































































































































































'''import random

def criar_baralho():
    naipes = ['♠', '♥', '♦', '♣']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    baralho = [(valor, naipe) for valor in valores for naipe in naipes]
    return baralho

def somar_cartas(mao):
    valores_cartas = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
    soma = 0
    possui_as = False
    for valor, naipe in mao:
        if valor == 'A':
            possui_as = True
        soma += valores_cartas[valor]
    if possui_as and soma <= 11:
        soma += 10
    return soma

def jogar_blackjack():
    baralho = criar_baralho()
    random.shuffle(baralho)
    mao_jogador = [baralho.pop(), baralho.pop()]
    mao_dealer = [baralho.pop()]

    print(f"Jogador: {mao_jogador} ({somar_cartas(mao_jogador)})")
    print(f"Dealer: [{mao_dealer[0]}]")

    while True:
        escolha = input("Você quer mais uma carta? (S/N): ")
        if escolha.lower() == 's':
            mao_jogador.append(baralho.pop())
            print(f"Jogador: {mao_jogador} ({somar_cartas(mao_jogador)})")
            if somar_cartas(mao_jogador) > 21:
                print("Estourou! Você perdeu.")
                return
        else:
            break

    while somar_cartas(mao_dealer) < 17:
        mao_dealer.append(baralho.pop())
        print(f"Dealer: {mao_dealer} ({somar_cartas(mao_dealer)})")
        if somar_cartas(mao_dealer) > 21:
            print("Dealer estourou! Você ganhou.")
            return

    if somar_cartas(mao_jogador) > somar_cartas(mao_dealer):
        print("Você ganhou!")
    elif somar_cartas(mao_jogador) == somar_cartas(mao_dealer):
        print("Empate!")
    else:
        print("Você perdeu.")

jogar_blackjack()
'''