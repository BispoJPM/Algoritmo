x=float(input("\nDigite o valor de X: "))
if x <= 1:
    y = 1
elif x <= 2:
    y = 2
elif 2 < x <= 3:
    y = x ** 2
else:
    y = x ** 3 
print("\nO valor de Y é: ", y)
print("\n")