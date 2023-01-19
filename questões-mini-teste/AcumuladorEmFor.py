numeros = [32, 43, 1, 7, 88, 51, 100, 0, -2]
soma = 0

for numero in numeros:
    if numero % 2 != 0:
        soma = soma + numero

print (soma)