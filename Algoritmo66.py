temp=float(input("\nDigite o tempo gasto: "))
vel=float(input("\nDigite a velocidade média: "))
dist=temp*vel
lts=dist/12
print("\n Velocidade: ", vel, "\nTempo: ", temp, "\nDistancia: ", dist, f"\nLitros: {lts: .2f}", "\n")