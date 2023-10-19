# Solicita que o usuário insira seu nome
nome = input("Digite o seu nome: ")

# Converte o nome para letras maiúsculas
nome = nome.upper()

# Inverte o nome
nome_invertido = nome[::-1]

# Exibe o nome invertido em maiúsculas
print(f"Seu nome ao contrário em maiúsculas é: {nome_invertido}")
