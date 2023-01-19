a = int(input())
b = int(input())
c = int(input())
#seja menor que a soma das medidas dos outros dois
#maior que o valor absoluto da diferença entre essas medidas.
if  a < b + c and a > abs(b - c):
    print(f'triangulo valido. {a + b + c:.0f}')
else:
    print('triangulo invalido.')
