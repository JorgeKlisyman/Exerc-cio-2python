# Algoritmo para calcular a tabuada de N

# Lendo o valor de N
while True:
    N = int(input("Digite um valor para N (de 1 a 10): "))
    if 1 <= N <= 10:
        break
    print("Valor inválido! Digite um número entre 1 e 10.")

# Calculando e exibindo a tabuada de N
print(f"Tabuada do {N}:")
for i in range(11):
    print(f"{i} x {N} = {i * N}")
