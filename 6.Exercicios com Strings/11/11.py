import random

# Carrega a lista de palavras a partir de um arquivo de texto
def carregar_palavras():
    with open("palavras.txt", "r") as arquivo:
        palavras = arquivo.readlines()
    return [palavra.strip() for palavra in palavras]

# Escolhe uma palavra aleatória da lista
def escolher_palavra(palavras):
    return random.choice(palavras)

# Jogo principal
def jogo_da_forca():
    palavras = carregar_palavras()
    palavra_secreta = escolher_palavra(palavras)
    palavra_em_jogo = ["_" for _ in palavra_secreta]
    erros = 0
    letras_erradas = []

    print("Bem-vindo ao Jogo da Forca!")
    
    while erros < 6:
        print("\n" + " ".join(palavra_em_jogo))
        letra = input("Digite uma letra: ").upper()

        if letra in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    palavra_em_jogo[i] = letra
        else:
            erros += 1
            letras_erradas.append(letra)
            print(f"-> Você errou pela {erros}ª vez. Tente de novo!")

        if "".join(palavra_em_jogo) == palavra_secreta:
            print(f"Parabéns! Você ganhou! A palavra era: {palavra_secreta}")
            break

    if erros == 6:
        print(f"Você foi enforcado! A palavra era: {palavra_secreta}")

if __name__ == "__main__":
    jogo_da_forca()
