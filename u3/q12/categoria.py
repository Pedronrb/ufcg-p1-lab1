#Entrada 
nome = input()
idade = int(input())
#lógica
if idade < 5 :
     print(f'{nome}, {idade} anos, Não pode competir.')
else:
    if idade >= 5 and idade <=7:
        print(f'{nome}, {idade} anos, Infantil A.')
        
    elif idade >= 8 and idade <= 10:
        print(f'{nome}, {idade} anos, Infantil B.')
    elif idade >=11 and idade <= 13:
        print(f'{nome}, {idade} anos, Juvenil A.')
    elif idade >= 14 and idade <= 17:
        print(f'{nome}, {idade} anos, Juvenil B.')
    else:
        print(f'{nome}, {idade} anos, Senior.')
