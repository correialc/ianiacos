from math import exp

alpha = 1/8000  # para um intervalo contínuo e ilimitado
a = 0           # limite inferior
b = 4000        # limite superior
prob = lambda a, b, alpha : exp(-alpha*a)-exp(-alpha*b)

# Estatísticas da distribuição
med = lambda alpha : 1 / alpha
var = lambda alpha : 1 / (alpha ** 2)
estats = lambda alpha : print(f"Média: {med(alpha)}, Variância: {var(alpha)}")
estats(alpha)

# Definindo a probabilidade de um evento ocorrer até um determinado limite superior
a = 0
b = 4000
print("Probabilidade de uma evento ocorrer até {}: {}".format(b, prob(a, b, alpha)))

# Definindo a probabilidade de um evento ocorrer após um determinado limite superior
a = 0
b = 4000
print("Probabilidade de uma evento ocorrer até {}: {}".format(b, 1 - prob(a, b, alpha)))
