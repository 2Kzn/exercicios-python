import math
n1 = int(input("Digite O Primerio Numero "))
n2 = int(input("Digite O Segundo Numero "))
resultado = math.potencia(n1, n2)
if(n2 <= 10):
 print(f"O Primeiro Número Elevado Ao Segundo É {resultado}")
else:
 print("O Segundo Númerão Pode Ser Maior Que 10")