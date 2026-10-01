altura = float(input("Digite a sua altura em metros: "))
sexo = input("Digite o seu sexo  'M' para masculino e 'f' para feminino: ")
if(sexo == "m"):
 pesoideal = (72.7 * altura) - 58
 print(f"Seu paso ideal é: {pesoideal:.2f} kg ")
 
elif(sexo == "f"):
 pesoideal = (62.1 * altura) - 44.7
 print(f"Seu paso ideal é: {pesoideal:.2f} kg ")

else:
 print("valor inválido")