def calcular_pontuacao(ouro, prata, bronze):
    return (ouro * 3) + (prata * 2) + bronze

paises = []

for lista in range(3):  # for é usado para dar um loop, e o range é usado para ciar uma sequencia de quantos itens eu quiser.
    nome_pais = input(f"\nDigite o nome do país: ")
    ouro = int(input(f"Digite a quantidade de medalhas de ouro para {nome_pais}: "))
    prata = int(input(f"Digite a quantidade de medalhas de prata para {nome_pais}: "))
    bronze = int(input(f"Digite a quantidade de medalhas de bronze para {nome_pais}: "))
    pontuacao = calcular_pontuacao(ouro, prata, bronze)
    paises.append((nome_pais, pontuacao))

paises_classificados = sorted(paises, key=lambda x: x[1], reverse=True)

print("\nClassificação dos países:")
for i, (nome, pontuacao) in enumerate(paises_classificados):
    print(f"\n{i + 1}. {nome} - Pontuação: {pontuacao}", "\n")
    