# Função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    print(f"\n{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}\n")

# Função para verificar se a jogada é válida
def jogada_valida(tabuleiro, posicao):
    return tabuleiro[posicao] == " "

# Função para realizar uma jogada
def realizar_jogada(tabuleiro, posicao, jogador):
    if jogada_valida(tabuleiro, posicao):
        tabuleiro[posicao] = jogador
        return True
    return False