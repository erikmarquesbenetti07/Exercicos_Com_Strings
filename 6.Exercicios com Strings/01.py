# Solicita que o usuário insira duas strings
string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

# Calcula o comprimento de cada string
comprimento_string1 = len(string1)
comprimento_string2 = len(string2)

# Exibe o conteúdo e o comprimento de cada string
print(f'Tamanho de "{string1}": {comprimento_string1} caracteres')
print(f'Tamanho de "{string2}": {comprimento_string2} caracteres')

# Compara as strings quanto ao comprimento e ao conteúdo
if comprimento_string1 == comprimento_string2:
    print("As duas strings são do mesmo comprimento.")
else:
    print("As duas strings são de tamanhos diferentes.")

if string1 == string2:
    print("As duas strings possuem o mesmo conteúdo.")
else:
    print("As duas strings possuem conteúdo diferente.")