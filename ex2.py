# Jogo da Velha NxN

# A matriz NXN representa o tabuleiro
# Solicitar o tamanho do tabuleiro
# Alternar entre os jogadores (X e O) e solicitar as jogadas
# Verificar se há um vencedor após cada jogada
# Continuar até que haja um vencedor ou um empate

def inicializar_tabuleiro(n):
    """Inicializa um tabuleiro vazio NxN."""
    tabuleiro = [[' ' for _ in range(n)] for _ in range(n)]
    return tabuleiro

def imprimir_tabuleiro(tabuleiro):
    """Impressão do tabuleiro."""
    n = len(tabuleiro)
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * (2 * n - 1))

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
    n = len(tabuleiro)

    # Checa as linhas
    for linha in tabuleiro:
        if linha[0] != ' ' and all(x == linha[0] for x in linha):
            return linha[0]

    # Checa as colunas
    for coluna in range(n):
        if tabuleiro[0][coluna] != ' ' and all(tabuleiro[i][coluna] == tabuleiro[0][coluna] for i in range(n)):
            return tabuleiro[0][coluna]

    # Checa as diagonais
    if tabuleiro[0][0] != ' ' and all(tabuleiro[i][i] == tabuleiro[0][0] for i in range(n)):
        return tabuleiro[0][0]
    if tabuleiro[0][n - 1] != ' ' and all(tabuleiro[i][n - 1 - i] == tabuleiro[0][n - 1] for i in range(n)):
        return tabuleiro[0][n - 1]

    return None

def jogo_da_velha():
    n = int(input("Informe a dimensão do tabuleiro: "))
    tabuleiro = inicializar_tabuleiro(n)
    jogadores = {'X': 'Jogador 1', 'O': 'Jogador 2'}
    jogador_atual = 'X'

    while True:
        print(f"Vez do {jogadores[jogador_atual]}:")
        imprimir_tabuleiro(tabuleiro)
        linha = int(input(f"Informe o número da linha (0-{n-1}): "))
        coluna = int(input(f"Informe o número da coluna (0-{n-1}): "))

        if 0 <= linha < n and 0 <= coluna < n:
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
            print(f"Entrada inválida. Tente novamente com valores entre 0 e {n-1}.")

if __name__ == "__main__":
    print("---------- Bem-vindo ao jogo da velha! ----------")
    jogo_da_velha()
