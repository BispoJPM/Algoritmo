hrt=float(input("\nHoras trabalhadas: "))
vhr=float(input("\nValor da Hora-Aula: "))
pdc=float(input("\nPercentual de Desconto: "))
sb=hrt*vhr
td=(pdc/100)*sb
sl=sb-td
print("\nSalário Líquido é: ", sl, "\n")
