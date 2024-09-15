# Algoritmo para ler a altura de 15 pessoas e encontrar a menor e maior altura

alturas = []

# Lendo as alturas
for i in range(15):
    altura = float(input(f"Digite a altura da pessoa {i+1}: "))
    alturas.append(altura)

# Calculando a menor e maior altura
menor_altura = min(alturas)
maior_altura = max(alturas)

# Exibindo os resultados
print(f"A menor altura do grupo é: {menor_altura:.2f} metros")
print(f"A maior altura do grupo é: {maior_altura:.2f} metros")
