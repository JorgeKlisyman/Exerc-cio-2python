# Algoritmo para contar quantos números estão em intervalos específicos

intervalo_0_25 = 0
intervalo_26_50 = 0
intervalo_51_75 = 0
intervalo_76_100 = 0

# Lendo os números até que o usuário insira um número negativo
while True:
    numero = float(input("Digite um número (ou um número negativo para encerrar): "))
    if numero < 0:
        break
    elif 0 <= numero <= 25:
        intervalo_0_25 += 1
    elif 26 <= numero <= 50:
        intervalo_26_50 += 1
    elif 51 <= numero <= 75:
        intervalo_51_75 += 1
    elif 76 <= numero <= 100:
        intervalo_76_100 += 1

# Exibindo os resultados
print(f"Quantidade de números no intervalo [0-25]: {intervalo_0_25}")
print(f"Quantidade de números no intervalo [26-50]: {intervalo_26_50}")
print(f"Quantidade de números no intervalo [51-75]: {intervalo_51_75}")
print(f"Quantidade de números no intervalo [76-100]: {intervalo_76_100}")
