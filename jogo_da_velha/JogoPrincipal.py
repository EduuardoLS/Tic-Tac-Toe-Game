from funcoes.tabuleiro import exibir_tabuleiro, realizar_jogada
from funcoes.verificacoes import verificar_vencedor, verificar_empate
from funcoes.arquivo import salvar_resultado

def jogar():
    while True:
        nome_jogador1 = input("Nome do Jogador 1 (X): ").strip()
        if not nome_jogador1:
            print("Nome inválido. O nome do jogador não pode estar vazio.")
            continue

        nome_jogador2 = input("Nome do Jogador 2 (O): ").strip()
        if not nome_jogador2:
            print("Nome inválido. O nome do jogador não pode estar vazio.")
            continue

        jogador_atual, simbolo_atual = nome_jogador1, "X"
        tabuleiro = [" " for _ in range(9)]

        while True:
            exibir_tabuleiro(tabuleiro)
            try:
                posicao = int(input(f"{jogador_atual}, escolha uma posição (1-9): ")) - 1
                if posicao < 0 or posicao > 8:
                    raise ValueError("Posição inválida. Escolha uma posição entre 1 e 9.")
            except ValueError as e:
                print(e)
                continue

            if realizar_jogada(tabuleiro, posicao, simbolo_atual):
                if verificar_vencedor(tabuleiro, simbolo_atual):
                    exibir_tabuleiro(tabuleiro)
                    print(f"{jogador_atual} venceu!")
                    salvar_resultado(nome_jogador1, nome_jogador2, tabuleiro, jogador_atual)
                    break
                elif verificar_empate(tabuleiro):
                    exibir_tabuleiro(tabuleiro)
                    print("O jogo empatou!")
                    salvar_resultado(nome_jogador1, nome_jogador2, tabuleiro, None)
                    break
                
                jogador_atual, simbolo_atual = (nome_jogador2, "O") if simbolo_atual == "X" else (nome_jogador1, "X")
            else:
                print("Essa posição já está ocupada. Escolha outra.")
        
        resposta = input("Deseja jogar novamente? (S/N): ").strip().upper()
        if resposta != "S":
            print("Obrigado por jogar!")
            break

if __name__ == "__main__":
    jogar()