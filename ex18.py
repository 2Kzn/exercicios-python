deposito = int(input("Forneça Seu Deposito "))
juros = int(input("Forneça Juros "))
rendimento = deposito * (juros/100)
depoisrendimento = rendimento + deposito
print(f"O Seu Rendimento É {rendimento} ")
print(f"E O Valor Total Depois Do Rendimento É {depoisrendimento}")