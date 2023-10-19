# Solicita que o usuário insira a data de nascimento no formato dd/mm/aaaa
data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")

# Divida a data em dia, mês e ano
dia, mes, ano = map(int, data_nascimento.split('/'))

# Dicionário para mapear números de meses para nomes de meses
meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

# Exibe a data de nascimento com o nome do mês por extenso
nome_mes = meses.get(mes, "Mês inválido")
print(f"Você nasceu em {dia} de {nome_mes} de {ano}.")
