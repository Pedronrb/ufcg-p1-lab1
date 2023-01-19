#IPTU da cidade
aConstruida =float(input("Área construída? "))
aliquota = float(input("Alíquota? "))

cal_iptu = (aConstruida * aliquota) + 35
cota_unica = cal_iptu - ((cal_iptu) * (25/100))

p6  = cal_iptu -  ((cal_iptu) * (5/100))


print(f'IPTU: R$ {cal_iptu:.2f}')

print('\nPagamento:')
print(f'1. Quota única. R$ {cota_unica:.2f}')
print(f'2. Em 6 parcelas. Total: R$ {p6:.2f}\n   6 x R$ {p6/6:.2f}')
print(f'3. Em 10 parcelas. Total: R$ {cal_iptu:.2f}\n   10 x R$ {cal_iptu/10}')
