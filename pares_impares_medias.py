# Algoritmo para contar números pares e ímpares, calcular a média dos pares e a média geral

pares = 0
impares = 0
soma_pares = 0
soma_total = 0
quantidade_numeros = 0

# Lendo números até o usuário digitar zero
while True:
    numero = int(input("Digite um número positivo (ou 0 para encerrar): "))

    if numero == 0:
        break
    elif numero > 0:
        quantidade_numeros += 1
        soma_total += numero
        if numero % 2 == 0:
            pares += 1
            soma_pares += numero
        else:
            impares += 1

# Calculando a média dos pares e a média geral
if pares > 0:
    media_pares = soma_pares / pares
else:
    media_pares = 0

if quantidade_numeros > 0:
    media_geral = soma_total / quantidade_numeros
else:
    media_geral = 0

# Exibindo os resultados
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
print(f"Média dos números pares: {media_pares:.2f}")
print(f"Média geral dos números lidos: {media_geral:.2f}")
