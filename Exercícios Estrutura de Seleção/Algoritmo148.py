regiao = ["1 - Região Norte", "2 - Região Nordeste", "3 - Região Centro-Oeste", "4 - Região Sul"]
print("\nRegiöes Disponíveis:", "\n")
for Região in regiao:
    print(Região)
tipo = ["1 - Ida", "2 - Ida e Volta"]
print("\nTipos Disponíveis: ", "\n")
for Ida in tipo:
    print(Ida)
dt=int(input("\nDigite o número da região: "))
id=int(input("Digite o número da opção desejada: "))
if(dt==1):
    if(id==1):
        print("\nO valor da passagem de ida para a Região Norte é de R$ 500.00", "\n")
    elif(id==2):
        print("\nO valor da passagem de ida-volta para a Região Norte é de R$ 950.00", "\n")
elif(dt==2):
    if(id==1):
        print("\nO valor da passagem de ida para a Região Nordeste é de R$ 350.00", "\n")
    elif(id==2):
        print("\nO valor da passagem de ida e volta para a Região Nordeste é de R$: 650.00", "\n")
elif(dt==3):
    if(id==1):
        print("\nO valor da passagem de ida para a Região Centro Oeste é de R$ 350.00", "\n")
    elif(id==2):
            print("\nO valor da passagem de ida e volta para a Região Centro Oeste é de R$ 600.00", "\n")
elif(dt==4):
    if(id==1):
        print("\nO valor da passagem de ida para a Região Sul é de R$: 300.00", "\n")
    elif(id==2):
        print("\nO valor da passagem de ida-volta para a Região Sul é de R$ 550.00", "\n")
else:
    print("\nOpção Inexistente", "\n")