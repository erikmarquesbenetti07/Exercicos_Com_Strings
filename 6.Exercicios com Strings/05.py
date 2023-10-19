# Solicita que o usuário insira seu nome
nome = input("Digite o seu nome: ")

# Inicializa uma variável para construir o nome progressivamente
nome_escada = ""

# Exibe o nome em formato de escada invertida
for letra in nome[::-1]:  # Percorre o nome em ordem inversa
    nome_escada += letra  # Adiciona a letra atual ao nome em escada
    print(f"o {nome_escada[::-1].upper()}")
