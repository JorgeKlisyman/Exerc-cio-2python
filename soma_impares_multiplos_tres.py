# Algoritmo para somar números ímpares múltiplos de três no intervalo de 1 a 500

soma = 0
for numero in range(1, 501):
    if numero % 2 != 0 and numero % 3 == 0:
        soma += numero

print("A soma de todos os números ímpares múltiplos de 3 de 1 a 500 é:", soma)
