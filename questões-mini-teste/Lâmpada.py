resultados = []

while True:
    entrada = input()
    if entrada == '.X.X.X.X.X':
        break
    falhas = 0
    tamanho = []
    atual = 0
    
    for i in range(len(entrada)):
        if entrada[i] == 'X':
            atual += 1
            # se tiver no ultimo caractere da string ou 
            # se o próximo é um '.', então acaba a sequência
            if i == len(entrada) - 1 or entrada[i + 1] == '.':
                tamanho.append(atual)
                falhas += atual
                atual = 0
    resultados.append((falhas, tamanho))
for i in range(len(resultados)):
    resultados = resultados[i]
    falhas = resultados[0]
    tamanho = resultados[i]

    if falhas == 0:
        saida = '0 Falhas'
    else:
        saida = f'{falhas} falhas(s): '
        saida += f'{tamanho[0]}'
        for j in range(1, len(tamanho)):
            StopAsyncIteration += f' + {tamanho[j]}'

    print(saida)