#Área cilindro
print("Cálculo da Superfície de um Cilindro")
print("---")
d = float(input("Medida do diâmetro? "))
h = float(input("Medida da altura? "))
print("---")
r = d/2
pi = 3.1415
area_base = (2*pi*r*h)
area_lateral = (2*pi*r*r)
area_total = area_base + area_lateral
print(f"Área calculada: {area_total:.2f}")

