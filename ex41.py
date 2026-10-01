print("dias da semana!\n")
print(" 1 - domingo \n 2 - segunda \n 3 - terça \n 4 - quarta \n 5 - quinta \n 6 - sexta \n 7 - sábado \n")

dia = int(input("insira o dia da semana em número: "))

domingo = 1
segunda = 2
terça = 3
quarta = 4
quinta = 5
sexta = 6
dia = "7" == "sábado"

if(dia > 7 or dia <= -0):
    print("valor inválido!!")

elif(dia == "1"):
    print(f"o seu dia é {1}")    
    
elif(dia == 2):
    print(f"o seu dia é {2}")
    
elif(dia == 3):
    print(f"o seu dia é {3}")

elif(dia == 4):
    print(f"o seu dia é {4}")

elif(dia == 5):
    print(f"o seu dia é {5}")

elif(dia == 6):
    print(f"o seu dia é {6}")

elif(dia ==7):
    print(f"o seu dia é {7}")

else:
    print(f"o dia {dia} não existe!!")