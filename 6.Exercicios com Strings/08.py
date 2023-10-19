import string

# Função para remover espaços e pontuações de uma string
def limpar_string(frase):
    frase = frase.lower()  # Converter a frase para minúsculas
    frase = ''.join(caracter for caracter in frase if caracter not in string.whitespace + string.punctuation)
    return frase

# Função para verificar se a string é um palíndromo
def e_palindromo(frase):
    frase_limpa = limpar_string(frase)
    return frase_limpa == frase_limpa[::-1]

# Solicita que o usuário insira uma sequência de caracteres
sequencia = input("Digite uma sequência de caracteres: ")

# Verifica se a sequência é um palíndromo
if e_palindromo(sequencia):
    print(f"A sequência '{sequencia}' é um palíndromo.")
else:
    print(f"A sequência '{sequencia}' não é um palíndromo.")
