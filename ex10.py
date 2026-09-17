lado1 = int(input("Digite o Primeiro lado "))
lado2 = int(input("Digite o Segundo lado "))
lado3 = int(input("Digite o terceiro lado "))

if(lado1 == lado2 and lado1 == lado3):
 print("Seu Triangulo é Equilatero")

elif(lado1 == lado2 or lado1 == lado3):
  print("Seu Triangulo é Isósceles")

else:
  (lado1 != lado2 and lado1 != lado3)
  print("Seu Triangulo é Escaleno")