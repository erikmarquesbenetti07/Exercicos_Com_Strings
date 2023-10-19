# Função para verificar se um CPF é válido
def valida_cpf(cpf):
    # Remove caracteres de formatação e mantém apenas os dígitos
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito1 = 11 - resto if resto > 1 else 0

    # Verifica se o primeiro dígito verificador é igual ao fornecido
    if digito1 != int(cpf[9]):
        return False

    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = 11 - resto if resto > 1 else 0

    # Verifica se o segundo dígito verificador é igual ao fornecido
    if digito2 != int(cpf[10]):
        return False

    return True

# Solicita que o usuário insira um número de CPF
cpf = input("Digite um número de CPF (xxx.xxx.xxx-xx): ")

# Verifica se o CPF é válido
if valida_cpf(cpf):
    print("O CPF é válido.")
else:
    print("O CPF é inválido.")
