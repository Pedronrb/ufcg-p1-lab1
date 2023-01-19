def oculta_letras(palavra, exibir):
    resposta = ''

    for i in range(len(palavra)):
        if palavra[i] in exibir:
            resposta[i] = exibir
        else:
            resposta[i] = '_'

    return resposta
