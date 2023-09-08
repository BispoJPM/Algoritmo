alt=float(input("\nDigite a altura da lata: "))
raio=float(input("\nDigite o raio da lata: "))
import math as m
vol=m.pi*(raio**2)*alt
print(f"\nO volume da lata é: {vol: .2f}", "\n")