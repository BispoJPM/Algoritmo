nome=str(input("\nDigite seu nome: "))
alt=input("Digite sua altura: ")
peso=input("Digite seu peso: ")
altc=float(alt.replace("," ,"."))
pesoc=float(peso.replace("," ,"."))
IMC=pesoc/altc**2
if IMC<20:
    print("\nO Paciente",nome,"está na Faixa de Risco: Abaixo do Peso", "\n")
elif 20 < IMC < 25:
    print("\nO Paciente",nome,"está na Faixa de Risco: Normal", "\n")
elif 25 < IMC < 30:
    print("\nO Paciente",nome,"está na Faixa de Risco: Excesso de Peso", "\n")
elif 30 < IMC < 25:
    print("\nO Paciente",nome,"está na Faixa de Risco: Obesidade", "\n")
else:
    print("\nO Paciente",nome,"está na Faixa de Risco: Obesidade Mórbida", "\n")
