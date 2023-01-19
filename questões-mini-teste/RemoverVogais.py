palavra = "bicicleta"
vogais = "aAeEiIoOuU"

palavra_sem_vogais = ""

for letra in palavra:
    if letra not in vogais:
        palavra_sem_vogais += letra

print (palavra_sem_vogais)