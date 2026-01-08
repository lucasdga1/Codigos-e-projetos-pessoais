import random

# ● ┌ ─ ┐ │ ┘└
art_dados = {
    1:(  "┌─────────┐",
         "│         │",
         "│    ●    │",
         "│         │",
         "└─────────┘"),
    2: ( "┌─────────┐",
         "│ ●       │",
         "│         │",
         "│       ● │",
         "└─────────┘"),
    3: ( "┌─────────┐",
         "│ ●       │",
         "│    ●    │",
         "│       ● │",
         "└─────────┘"),
    4: ( "┌─────────┐",
         "│ ●     ● │",
         "│         │",
         "│ ●     ● │",
         "└─────────┘"),
    5: ( "┌─────────┐",
         "│ ●     ● │",
         "│    ●    │",
         "│ ●     ● │",
         "└─────────┘"),
    6: ( "┌─────────┐",
         "│ ●     ● │",
         "│ ●     ● │",
         "│ ●     ● │",
         "└─────────┘"),
}
dado = []
total = 0

qtd_dados = int(input("Quantos dados D6 você deseja rolar: "))

# Loop para rolar números aleatórios e listá-los de acordo com a quantidade escolhida
for x in range(qtd_dados):
    dado.append(random.randint(1, 6))
    total += dado[x]
# Para mostrar os dados verticalmente use o código abaixo:
# for x in range(qtd_dados):
#     for i in art_dados.get(dado[x]):
#         print(i)

# Para mostrar os dados horizontalmente use este código:
for linha in range(5):
    for x in dado:
        print(art_dados.get(x)[linha], end="")
    print()
print(f"O seu total foi: {total}")
