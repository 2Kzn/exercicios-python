print("convertendo tintas")
area = float(input("insira a área em metros "))
if(area <= -0):
 print("Valor inválido")
else:
 metros_por_litro = 3
 litros_por_lata = 18
 preço_lata = 80
 litros_necessarios = area / metros_por_litro
 latas_necessasarias = (litros_necessarios / litros_por_lata)
 custo_total = latas_necessasarias * preço_lata
 print(f"para {area} M², precisamos de {litros_necessarios:.2f} litros")
 print(f"você precisa de {latas_necessasarias:.2f} latas para pintar {area} M²")
 print(f"isso tudo custará R$ {custo_total:.2f}")