# Algoritmo para calcular a média aritmética, quantidade de valores positivos e negativos,
# e o percentual de cada um

valores = []
positivos = 0
negativos = 0

# Lendo os valores até que o usuário decida parar
while True:
    valor = float(input("Digite um valor (ou 0 para encerrar): "))
    if valor == 0:
        break
    valores.append(valor)
    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1

# Calculando a média
if len(valores) > 0:
    media = sum(valores) / len(valores)
else:
    media = 0

# Calculando o percentual de positivos e negativos
total_valores = len(valores)
if total_valores > 0:
    percentual_positivos = (positivos / total_valores) * 100
    percentual_negativos = (negativos / total_valores) * 100
else:
    percentual_positivos = percentual_negativos = 0

# Exibindo os resultados
print(f"Média aritmética: {media:.2f}")
print(f"Quantidade de valores positivos: {positivos}")
print(f"Quantidade de valores negativos: {negativos}")
print(f"Percentual de valores positivos: {percentual_positivos:.2f}%")
print(f"Percentual de valores negativos: {percentual_negativos:.2f}%")
