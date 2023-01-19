#ENTRADA

nome = input()

valorJoao = 0
countJoao = 0
valorJulio = 0
countJulio = 0

while nome != 'fim':
    dados = nome.split()
    if dados[0] == 'joao':
        valorJoao += float(dados[1])
        countJoao += 1
    else:
        valorJulio += float(dados[1])
        countJulio += 1

    if countJoao > 2 or countJulio > 2:
    
        if countJoao > 2:
            print('joao foi o vencedor. Comprou mais de duas vezes no período.')
            break

        elif countJulio > 2:
            print('julio foi o vencedor. Comprou mais de duas vezes no período.')
            break

    elif valorJulio >= 2000 or valorJoao >= 2000:
        if valorJulio >= 2000:
            print('julio foi o vencedor. Comprou mais R$ 2000.00 no período.')
            break

        elif valorJoao >= 2000:
            print('joao foi o vencedor. Comprou mais R$ 2000.00 no período.')
            break

    nome = input()

if countJoao <= 2 and countJulio <= 2 and valorJoao < 2000 and valorJulio < 2000:
    print('Não houve vencedor.')
