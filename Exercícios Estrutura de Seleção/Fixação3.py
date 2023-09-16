A = float(input("\nDigite o valor do lado A: "))
B = float(input("Digite o valor do lado B: "))
C = float(input("Digite o valor do lado C: "))

if (A + B) <= C or (B + C) <= A or (A + C) <= B:
    print("\nNão compõem um triângulo", "\n")
  
elif A == B == C:
    print("\nEle é um Triângulo equilátero", "\n")
elif A == B or A == C or B == C:
    print("\nEle é um Triângulo isósceles", "\n")
else:
    print("\nEle é um Triângulo escaleno", "\n")
