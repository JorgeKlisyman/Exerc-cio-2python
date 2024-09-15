# Algoritmo para gerar uma sequência de 10 valores em P.A.

# Lendo o valor inicial A e a razão R
A = int(input("Digite o valor inicial A: "))
R = int(input("Digite a razão R: "))

# Gerando e exibindo a sequência em P.A.
print("Sequência em P.A.:")
for i in range(10):
    termo = A + i * R
    print(termo)
