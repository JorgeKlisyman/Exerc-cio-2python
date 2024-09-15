# Algoritmo para calcular e exibir o fatorial de A

# Lendo o valor inicial A
A = int(input("Digite o valor inicial A: "))

# Calculando o fatorial
fatorial = 1
sequencia = ""

for i in range(A, 0, -1):
    fatorial *= i
    if i == 1:
        sequencia += f"{i}"
    else:
        sequencia += f"{i} x "

# Exibindo a sequência e o resultado
print(f"{A}! = {sequencia} = {fatorial}")
