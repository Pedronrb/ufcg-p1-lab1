entrada = input()
total_defeituosas = 0
total_sessao = 0
total_detalhado = ""
resposta = ""

while (entrada != ".X.X.X.X.X"):
    for i in range(0, len(entrada)):
        if (entrada[i] == "X"):
            total_defeituosas += 1
            total_sessao += 1
        elif (entrada[i] == "."):
            if (total_sessao > 0):
                total_detalhado += str(total_sessao) + ' + '
                total_sessao = 0
        if (i == len(entrada) - 1 and entrada[i] == "X"):
            total_detalhado += str(total_sessao) + ' + '
    if (total_defeituosas == 0):
        resposta += '0 falhas\n'
    else:
        resposta += f"{total_defeituosas} falha(s): {total_detalhado[0:len(total_detalhado)-3]} \n"

    total_sessao = 0
    total_defeituosas = 0
    total_detalhado = ''
    entrada = input()

print(resposta)
