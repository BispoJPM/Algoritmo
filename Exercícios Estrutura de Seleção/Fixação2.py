A=input("\nDigite a quantia de litros de Álcool: ")
A=float(A.replace (" , ", "."))
Gs=input("\nDigite a quantia de litros em Gasolina: ")
Gs=float(Gs.replace(",","."))

if A > 20:
    sd=A*2.90
    dc=sd*0.03
    total=sd-dc
    print(f"\nO valor com desconto sobre o Álcool é: {total: .2f}")
else:
    total=A*2.90
    print("\nO valor sem desconto é: ", total, "\n")

if Gs > 20:
        sd=Gs*3.30
        dc=Gs*0.03
        total=sd-dc
        print(f"\nO valor com desconto sobre a Gasolina é: {total: .2f}", "\n")
else:
    total=Gs*3.30
    print(f"\nO valor sem desconto é: {total: .2f}", "\n")