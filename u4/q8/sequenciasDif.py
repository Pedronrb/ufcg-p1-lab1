lista = []
tamanho = int(input())
for i in range(tamanho):
    numero = int(input())
    lista.append(numero)
   
for i in range(len(lista)-1):       
    if lista[i] == lista[i+1]:
        lista[i+1] = lista[i+1]-1
print(' '.join(map(str, lista)))
