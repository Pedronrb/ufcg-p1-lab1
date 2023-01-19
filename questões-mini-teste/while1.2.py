entrada = ""
defeituosas = 0
list = []

while entrada != "fim":
    entrada = input()
    i = 0
    while i < len(entrada):
        if entrada[i] == "l" or entrada[i] == "z":
            defeituosas += 1
        elif entrada[i] == "p":
            defeituosas = 0
    list.append(defeituosas)
print(list)