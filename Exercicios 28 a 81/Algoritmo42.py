angulo=float(input("\nDigite um ângulo em graus: "))
import math as m
rang=angulo*m.pi/180
print(f"\nSeno: {m.sin(rang): .2f}")
print(f"\nCo-seno: {m.cos(rang): .2f}")
print(f"\nTangente: {m.tan(rang): .2f}")
print(f"\nCo-secante: {1/m.sin(rang): .2f}")
print(f"\nSecante: {1/m.cos(rang): .2f}")
print(f"\nCotangente: {1/m.tan(rang): .2f}", "\n")