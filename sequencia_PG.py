# Algoritmo para gerar uma sequência de 10 valores em P.G.

# Lendo o valor inicial A e a razão R
A = int(input("Digite o valor inicial A: "))
R = int(input("Digite a razão R: "))

# Gerando e exibindo a sequência em P.G.
print("Sequência em P.G.:")
for i in range(10):
    termo = A * (R ** i)
    print(termo)
