# Definição de variáveis
def main():
    jogador_1 = 0
    jogador_2 = 0
    peca = 0
    vencedor = 0
    cont = 0
    print("Bem vindo ao Jogo da Velha!!😊")

    # Verificação de linhas
    def verifica_vencedor(tabuleiro, simbolo):
        # linhas
        for linha in tabuleiro:
            if all(c == simbolo for c in linha):
                return True
        for coluna in range(3):
            if all(tabuleiro[linha][coluna] == simbolo for linha in range(3)):
                return True
        # Diagonais
        if all(tabuleiro[i][i] == simbolo for i in range(3)):
            return True
        if all(tabuleiro[i][2 - i] == simbolo for i in range(3)):
            return True

        return False
    # Criação de tabuleiro
    def criar_tabuleiro():
        return[[" "for _ in range(3) ] for _ in range(3)]
    tabuleiro = criar_tabuleiro()
    def mostrar_tabuleiro(tabuleiro):
        for linha in tabuleiro:
            print(" ".join([f"[{peca}]" if peca != " " else "[]" for peca in linha]))
        print()
    mostrar_tabuleiro(tabuleiro)
    def sep_linha():
        print("-"*20)
    sep_linha()

    jogador_1 = str(input("Escolha X ou O: \n")).upper()
    if jogador_1 == "X":
        jogador_2 = "O"
    elif jogador_1 == "O":
        jogador_2 = "X"
    else:
        print ("Escolha inválida, escolhendo X por padrão\n")
        jogador_1 = "X"
        jogador_2 = "O"

    # Começa o jogador 1
    peca = jogador_1

    # Loop de jogadas
    while vencedor == 0 & cont < 9:
        mostrar_tabuleiro(tabuleiro)
        sep_linha()
        pos = int(input(f"Jogador atual {peca} escolha uma posição de 0 a 8: "))
        if pos < 0 or pos > 8:
            pos = int(input("Posição inválida, tente novamente entre 0 e 8: "))
        # Converte pos em um lugar do tabuleiro
        linha = int(pos / 3)
        coluna = int(pos % 3)
        # Verifica se lugar está vazio e atribui peça
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = peca
            cont += 1

        else:
            print("\nCasa ocupada, tente outra posição\n")
            continue

        # Final de jogo
        mostrar_tabuleiro(tabuleiro)
        sep_linha()
        if verifica_vencedor(tabuleiro, "X"):
            vencedor = "X"
            if vencedor == jogador_1:
                print("Fim de jogo! Vitória do jogador 1")
            elif vencedor == jogador_2:
                print("Fim de jogo! Vitória do jogador 2")
        elif verifica_vencedor(tabuleiro, "O"):
            vencedor = "O"
            if vencedor == jogador_1:
                print("Fim de jogo! Vitória do jogador 1")
            elif vencedor == jogador_2:
                print("Fim de jogo! Vitória do jogador 2")
            sep_linha()
            break

        if peca == jogador_1:
            peca = jogador_2
        else:
            peca = jogador_1

    if vencedor == 0 and cont == 9:
        mostrar_tabuleiro(tabuleiro)
        print("Deu velha!! Vamos jogar novamente\n")


main()