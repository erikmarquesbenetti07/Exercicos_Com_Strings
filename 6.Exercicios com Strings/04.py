# Solicita que o usuário insira seu nome
nome = input("Digite o seu nome: ")

# Inicializa uma variável para construir o nome progressivamente
nome_escada = ""

# Exibe o nome em formato de escada
for letra in nome:
    nome_escada += letra  # Adiciona a letra atual ao nome em escada
    print(f"o {nome_escada.upper()}")
