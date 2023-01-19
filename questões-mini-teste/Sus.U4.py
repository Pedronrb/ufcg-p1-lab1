count = 0
list = []

for i in range(0,12):
    entrada = int(input())
    count += entrada
    list.append(entrada)
media = count / 12
print(f'A média das vacinas aplicadas : {media:.2f}')
print('******')
for j in range(len(list)):
    if media < list[j]:
        print(f'Mês {j+1}: {list[j]}')

