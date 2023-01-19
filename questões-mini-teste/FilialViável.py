entrada = input()
resposta = ''
viabilidade = 0
contagem = ''

while entrada != 'fim':
    quebra = entrada.split()
    letras = quebra[1]
    
    for i in range(0, len(letras)):

        if letras[i] != 'p':
            viabilidade += 1

        elif letras[i] == 'p' and viabilidade > 0:
            if (len(letras) - 1 == i):
                contagem += str(viabilidade)
            else:
                contagem += str(viabilidade) + ' + '            
            viabilidade = 0

        if (len(letras) - 1 == i and letras[i] != 'p' ):  

            contagem += str(viabilidade)
   
    resposta += f'{quebra[0]}: {contagem}\n'
    contagem = ''
    viabilidade = 0
    entrada = input()
print(resposta)






    