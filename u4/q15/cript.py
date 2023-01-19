entrada = input()
palavra = entrada[0]
cont = 0
for i in range(1, len(entrada)):
   
    if entrada[i] == 'a'or entrada[i] == 'A':
        palavra += '4'
        cont += 1

    elif entrada[i] == 'e'or entrada[i] == 'E':
        palavra += '3'
        cont += 1

    elif entrada[i] == 'i' or entrada[i] == 'I':
        palavra += '1'
        cont += 1
    
    elif entrada[i] == 'o' or entrada[i] == 'O':
        palavra += '0'
        cont += 1
    else:
        palavra += entrada[i]

print(f'{palavra} ({cont} troca(s))')

