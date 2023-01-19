cpf1 = int(input())
cpf2 = int(input())
cpf3 = int(input())

soma1 = (cpf1 % 100)//10 + (cpf1 %  10)
print(f"{cpf1 //100}-{cpf1 % 100}")
print(soma1)

soma2 = (cpf2 % 100)//10 + (cpf2 %  10)
print(f"{cpf2 //100}-{cpf2 % 100}")
print(soma2)

soma3 = (cpf3 % 100)//10 + (cpf3 %  10)
print(f"{cpf3 //100}-{cpf3 % 100}")
print(soma3)

