sm=float(input("\nDigite seu saldo médio: "))
if (0<sm<=500):
    Crédito = 0
elif (501 <= sm <= 1000):
    Crédito = sm * 0.3
elif (1001 <= sm <= 3000):
    Crédito = sm * 0.4
elif (3001 <= sm):
    Crédito = sm * 0.5
    
if Crédito != 0.0:
     print("\nComo seu saldo médio era de: R$",sm, "seu crédito será de:",Crédito, "\n")
else:
     print("\nComo seu saldo era de: R$",sm, "você não terá nenhuma crédito" ,"\n")
     
