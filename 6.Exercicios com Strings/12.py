# Solicita que o usuário insira um número de telefone
telefone = input("Telefone: ")

# Remove traços e espaços em branco do número
telefone = telefone.replace("-", "").replace(" ", "")

# Verifica se o número possui apenas 7 dígitos
if len(telefone) == 7:
    telefone_corrigido = "3" + telefone
    telefone_formatado = telefone_corrigido[:4] + "-" + telefone_corrigido[4:]
    print("Telefone possui 7 dígitos. Vou acrescentar o dígito '3' na frente.")
    print(f"Telefone corrigido sem formatação: {telefone_corrigido}")
    print(f"Telefone corrigido com formatação: {telefone_formatado}")
else:
    print("Telefone válido ou com formato incorreto.")
