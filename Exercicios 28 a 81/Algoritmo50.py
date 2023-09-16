base=float(input("\nDigite a base: "))
alt=float(input("\nDigite a altura: "))
perimetro=2*(base+alt)
area=base*alt
diagonal=1/2**(base**2+alt**2)
print("\nPerimetro: ", perimetro)
print("\nArea: ", area)
print(f"\nDiagonal: {diagonal: .2f}", "\n")