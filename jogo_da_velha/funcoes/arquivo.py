import os

# Função para salvar o resultado em um arquivo
def salvar_resultado(nome_jogador1, nome_jogador2, tabuleiro, vencedor):
    if not os.path.exists('resultados_jogo.txt'):
        with open('resultados_jogo.txt', 'w') as arquivo:
            arquivo.write("Resultados do Jogo da Velha\n\n")
    
    with open('resultados_jogo.txt', 'a') as arquivo:
        arquivo.write(f"{nome_jogador1} x {nome_jogador2}\n")
        arquivo.write(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}\n")
        arquivo.write(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}\n")
        arquivo.write(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}\n")
        
        if vencedor:
            arquivo.write(f"Vencedor: {vencedor}\n")
        else:
            arquivo.write("Empate\n")
        
        arquivo.write("-" * 20 + "\n\n")  # Separador para partidas