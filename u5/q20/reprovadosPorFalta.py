reprovados = 0
presenca = ""

while presenca != "-":
    presenca = input()
    nFaltas = 0
    i = 0

    while i < 14:
        print(i)
        if presenca[i] == 'f':
            print("entrou")
            nFaltas += 1
        i += 1

    if nFaltas == 8:
        reprovados += 1
print(reprovados)


