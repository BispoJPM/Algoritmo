Alt = (input("\nDigite sua altura em metros: "))
Alt=float(Alt.replace(",","."))
Peso = (input("\nDigite seu peso: "))
Peso=float(Peso.replace(",","."))
Sexo = input("\nDigite M para masculino ou F para feminino: ").lower()
Sexo=str(Sexo.replace(",","."))

if Sexo == 'm':
    peso_ideal = (72.7 * Alt) - 58
    print(f"\nPeso Ideal: {peso_ideal: .2f}")
else:
    peso_ideal = (62.1 * Alt) - 44.7
    print(f"\nPeso Ideal: {peso_ideal: .2f}", "\n")