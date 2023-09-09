num=float(input("\nEntre com um numero com parte fracionaria: "))
numi=int(num)
numfrac=num-numi
numa=int(num+0.00001)
print("\nParte inteira: ", numi)
print(f"\nParte Fracionada: {(numfrac+0.00001): .3f}")
print("\nNúmero arredondado: ", numa, "\n")
