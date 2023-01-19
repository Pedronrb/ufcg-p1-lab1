frase = input("frase? ").split()

iterador = iter(frase)
while True:
    try:
        palavra = next(iterador)
    except StopIteration:
        break

    print(palavra)

print("fim")