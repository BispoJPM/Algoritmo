nome=str(input("\nDigite seu nome: ")) 
idade=int(input("\nDigite sua idade: "))
if idade <= 10:
    print("\n", nome,"pagara R$ 30.00","\n")
elif 10 < idade <= 29:
    print("\n" ,nome,"pagara R$ 60.00","\n")
elif 29 < idade <= 45:
    print("\n", nome,"pagara R$ 120.00","\n")
elif 45 < idade <=59:
    print("\n", nome,"pagara R$ 150.00","\n")
elif 59 < idade <= 65:
    print("\n", nome,"pagara R$ 250.00","\n")
else:
    print("\n", nome,"pagara R$ 400,00","\n")

    