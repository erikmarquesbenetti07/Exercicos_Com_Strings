# Listas de palavras para os números de 1 a 19 e dezenas
unidades = ["", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove"]
dezenas = ["", "Dez", "Vinte", "Trinta", "Quarenta", "Cinquenta", "Sessenta", "Setenta", "Oitenta", "Noventa"]

# Solicita que o usuário insira um número até 99
numero = int(input("Digite um número até 99: "))

# Verifica se o número está na faixa válida
if 1 <= numero <= 99:
    # Se o número for menor ou igual a 19, imprime a palavra diretamente
    if numero <= 19:
        print(unidades[numero])
    else:
        # Para números maiores que 19, divide o número em dezenas e unidades
        dezena = numero // 10
        unidade = numero % 10
        # Imprime a representação por extenso da dezena e da unidade
        print(dezenas[dezena] + (" e " if unidade > 0 else "") + unidades[unidade])
else:
    print("Número fora da faixa permitida (1 a 99).")
