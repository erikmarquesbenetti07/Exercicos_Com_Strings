import random

# Carrega a lista de palavras a partir de um arquivo de texto
def carregar_palavras():
    with open("palavras.txt", "r") as arquivo:
        palavras = arquivo.readlines()
    return [palavra.strip() for palavra in palavras]

# Escolhe uma palavra aleatória da lista
def escolher_palavra(palavras):
    return random.choice(palavras)

# Embaralha uma palavra
def embaralhar_palavra(palavra):
    palavra_embaralhada = list(palavra)
    random.shuffle(palavra_embaralhada)
    return ''.join(palavra_embaralhada)

# Jogo principal
def jogo_palavra_embaralhada():
    palavras = carregar_palavras()
    palavra_secreta = escolher_palavra(palavras)
    palavra_embaralhada = embaralhar_palavra(palavra_secreta)
    tentativas = 6

    print("Bem-vindo ao Jogo da Palavra Embaralhada!")
    print(f"Você tem {tentativas} tentativas para adivinhar a palavra.")
    print(f"A palavra embaralhada é: {palavra_embaralhada}")

    while tentativas > 0:
        tentativa = input("Tentativa: ").upper()
        if tentativa == palavra_secreta:
            print(f"Parabéns! Você adivinhou a palavra. A palavra é: {palavra_secreta}")
            break
        else:
            print(f"Você errou! Restam {tentativas - 1} tentativas.")
            tentativas -= 1

    if tentativas == 0:
        print(f"Você perdeu! A palavra era: {palavra_secreta}")

if __name__ == "__main__":
    jogo_palavra_embaralhada()
