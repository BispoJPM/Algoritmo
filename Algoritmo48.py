sm=float(input("\nEntre com o Salário Mínimo: "))
qtdade=float(input("\nEntre com a quantidade em quilowatt: "))
preco=sm//700
vp=preco*qtdade
vd=vp*0.9
print(f"\nO preço do quilowatt é: {preco: .2f}")
print(f"\nO valor a ser pago é: {vp: .2f}")
print(f"\nO valor com desconto é: {vd: .2f}", "\n")
