angulo=float(input("\nDigite um ângulo em graus: "))
import math
rang=angulo*math.pi/180
print("\nSeno: ", math.sin(rang))
print("\nCo-seno: ", math.cos(rang))
print("\nTangente: ", math.tan(rang))
print("\nCo-secante: ", 1/math.sin(rang))
print("\nSecante: ", 1/math.cos(rang))
print("\nCotangente: ",1/math.tan(rang))
print("\n")
