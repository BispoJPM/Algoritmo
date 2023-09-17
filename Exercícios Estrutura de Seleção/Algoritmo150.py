ang=float(input("\nDigite o ângulo em Graus: "))
import math as math
rang=ang*math.pi/180
if ((rang > math.pi/2 and rang <= math.pi) or (rang >3* math.pi/2 and rang <= 2*math.pi)):
    print("\nSeno: ", math.sen(rang))
else:
    print("\nCo-seno: ", math.cos(rang), "\n")