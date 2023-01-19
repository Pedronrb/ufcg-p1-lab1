#álbum da copa 

import math
total_fig = int(input())
pacote_fig = int(input())
nao_rept = int(input())
valor = float(input())

total_pacotes = math.ceil(total_fig / nao_rept)
rept = total_pacotes * (pacote_fig - nao_rept)
gasto = total_pacotes * valor

print(f'{total_pacotes:.0f}\n{rept:.0f}\nR$ {gasto:.2f}') 
