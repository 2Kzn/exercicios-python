n1 = int(input("Digite o Primeiro Número"))
n2 = int(input("Digite o Segundo Número"))
n3 = int(input("Digite o Primeiro Número"))
n4 = int(input("Digite o Segundo Número"))
disciplina = input("Insira A Sua Disciplina")

media = (n1 + n2 + n3 + n4) /4
if(media >= 7):
 print(f"Sua nota é {media} você está aprovado em {disciplina}")
else:
 print(f"Sua nota é {media} você está reprovado em {disciplina}")