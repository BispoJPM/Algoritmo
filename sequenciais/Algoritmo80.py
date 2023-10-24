quant=int(input("\nDigite a quantidade de fitas: "))
valAluguel=float(input("\nDigite o valor do aluguel: "))
fatAnual=quant/3*valAluguel*12
print("\nFaturamento Anual: ", fatAnual)
multas=valAluguel*0.1*(quant/3)/100
quantFinal=quant-quant*0.2+quant/10 #quant*1.08#
print("\nA quantidade de fitas no final do ano: ", quantFinal, "\n")