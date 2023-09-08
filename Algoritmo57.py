pr1=float(input("\nDigite PR1: "))
pr2=float(input("\nDigite PR2: "))
mf=(pr1+pr2)/2
print("\nMédia truncada: ", int((mf-0.5)+0.001))
print("\nMédia Arredondada: ", int(mf+0.001))
print("\n")