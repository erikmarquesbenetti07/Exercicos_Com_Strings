# Solicita que o usuário insira uma frase
frase = input("Digite uma frase: ")

# Inicializa contadores
espacos = 0
vogais = 0

# Define uma lista de vogais
vogais_lista = ['a', 'e', 'i', 'o', 'u']

# Percorre a frase para contar espaços em branco e vogais
for caracter in frase:
    if caracter == ' ':
        espacos += 1
    elif caracter.lower() in vogais_lista:
        vogais += 1

# Exibe o número de espaços em branco e o número de vogais
print(f"Quantidade de espaços em branco: {espacos}")
print(f"Quantidade de vogais (a, e, i, o, u): {vogais}")
