#Entradas:
congelado = float(input())
descongelado = float(input())
peso = abs(congelado - descongelado)
porcentagem = (peso / congelado) * 100

#algoritmo:
print(f'{porcentagem:.1f}% do peso do produto é de água congelada.')
if  porcentagem  <= 10 and porcentagem  > 5:
    print('Produto em conformidade.')
elif porcentagem <=  5 :
    print('Produto qualis A.')
else:
    print('Produto não conforme.')


