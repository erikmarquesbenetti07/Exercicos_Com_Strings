# Dicionário de substituições para leet speak
leet_dict = {
    'A': '4',
    'B': '8',
    'C': '(',
    'D': '|)',
    'E': '3',
    'F': '|=',
    'G': '6',
    'H': '#',
    'I': '1',
    'J': '_|',
    'K': '|<',
    'L': '|_',
    'M': '|\\/|',
    'N': '/\\/',
    'O': '0',
    'P': '|D',
    'Q': '(,)',
    'R': '|2',
    'S': '5',
    'T': '7',
    'U': '|_|',
    'V': '\\/',
    'W': '|/\\|',
    'X': '><',
    'Y': '`/',
    'Z': '2'
}

# Função para converter texto em leet speak
def to_leet_speak(text):
    leet_text = ""
    for char in text.upper():
        if char in leet_dict:
            leet_text += leet_dict[char]
        else:
            leet_text += char
    return leet_text

# Solicita ao usuário que insira um texto
texto = input("Digite um texto: ")

# Converte o texto em leet speak
leet_text = to_leet_speak(texto)

# Imprime o texto em leet speak
print("Texto em Leet Speak:", leet_text)
