#Entradas
peso = int(input('Qual seu pesoe em Kg? '))
altura = float(input('Qual sua altura? '))

#Cálculos
imc = peso / (altura**2)
print(f'IMC = {imc:,.2f}')

#Condições
if imc >= 18.5 and imc < 25:
    print('Classificação = Saudável')
elif imc >= 30.0:
    print('Classificação = Obesidade')
elif imc >= 25 and imc < 30.0:
    print('Classificação = Sobrepeso')
else:
    print('Classificação = Magreza')
