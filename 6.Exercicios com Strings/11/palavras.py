palavras = [
    "ABACAXI",
    "BANANA",
    "CACHORRO",
    "DINOSSAURO",
    "ELEFANTE",
    "FLORESTA",
    "GIRASSOL",
    "HIPOTESE",
    "IGREJA",
    "JOGADOR",
    "KANGAROO",
    "LARANJA",
    "MELANCIA",
    "NARIZ",
    "ORQUÍDEA",
    "PASTEL",
    "QUADRADO",
    "RAIO",
    "SOL",
    "TARTARUGA",
    "URSO",
    "VIOLINO",
    "XADREZ",
    "YOGA",
    "ZEBRA"
]

with open("palavras.txt", "w") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")

print("Lista de palavras gerada e salva no arquivo 'palavras.txt'.")
