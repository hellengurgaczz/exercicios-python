# Jogo da Velha 4x4

# A matriz 4X4 representa o tabuleiro
# Alternar entre os jogadores (X e O) e solicitar as jogadas
# Verificar se há um vencedor após cada jogada
# Continuar até que haja um vencedor ou um empate

def criar_tabuleiro():
    """Inicializa um tabuleiro 4x4."""
    return  [[' ' for _ in range(4)] for _ in range(4)]

def imprimir_tabuleiro(tabuleiro):
    """Impressão do tabuleiro."""
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 9)

def realizar_jogada(tabuleiro, jogador, linha, coluna):
    """Realiza uma jogada no tabuleiro."""
    if tabuleiro[linha][coluna] == ' ':
        tabuleiro[linha][coluna] = jogador
        return True
    else:
        print("Essa posição já está ocupada. Tente novamente em outra posição.")
        return False

def verificar_vencedor(tabuleiro):
    """Verificação se há um vencedor no tabuleiro."""
    # Checa as linhas
    for linha in tabuleiro:
        if linha[0] != ' ' and all(x == linha[0] for x in linha):
            return linha[0]

    # Checa as colunas
    for coluna in range(4):
        if tabuleiro[0][coluna] != ' ' and all(tabuleiro[i][coluna] == tabuleiro[0][coluna] for i in range(4)):
            return tabuleiro[0][coluna]

    # Checa as diagonais
    if tabuleiro[0][0] != ' ' and all(tabuleiro[i][i] == tabuleiro[0][0] for i in range(4)):
        return tabuleiro[0][0]
    if tabuleiro[0][3] != ' ' and all(tabuleiro[i][3 - i] == tabuleiro[0][3] for i in range(4)):
        return tabuleiro[0][3]

    return None

def jogo_da_velha():
    tabuleiro = criar_tabuleiro()
    jogadores = {'X': 'Jogador 1', 'O': 'Jogador 2'}
    jogador_atual = 'X'

    while True:
        print(f"Vez do {jogadores[jogador_atual]}:")
        imprimir_tabuleiro(tabuleiro)
        linha = int(input("Informe o número da linha (0-3): "))
        coluna = int(input("Informe o número da coluna (0-3): "))

        if 0 <= linha <= 3 and 0 <= coluna <= 3:
            if realizar_jogada(tabuleiro, jogador_atual, linha, coluna):
                vencedor = verificar_vencedor(tabuleiro)
                if vencedor:
                    imprimir_tabuleiro(tabuleiro)
                    print(f"{jogadores[vencedor]} venceu!")
                    break
                elif all(coluna != ' ' for linha in tabuleiro for coluna in linha):
                    imprimir_tabuleiro(tabuleiro)
                    print("Empate!")
                    break
                jogador_atual = 'X' if jogador_atual == 'O' else 'O'
            else:
                continue
        else:
            print("Entrada inválida. Tente novamente com valores entre 0 e 3.")

if __name__ == "__main__":
    print("---------- Bem-vindo ao jogo da velha! ----------")
    jogo_da_velha()
