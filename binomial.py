from math import sqrt
from scipy.stats import binom

# Exemplos de uso
# Gerando a distribuicao
p = 0.02
n = 10
dist = binom(n, p)

# Estatísticas da distribuição
estats = lambda n, p : print(f"Média: {binom.mean(n, p)}, Variância: {binom.var(n, p)}, Desvio: {binom.std(n, p)}") 
estats(n, p)

# Definindo a probabilidade de um x específico
x = 2
print("Probabilidade de sucesso para exatamente {} ocorrências: {}".format(x, dist.pmf(x)))

# Definindo a probabilidade de um intervalo <=x
x = 2
print("Probabilidade de sucesso para até {} ocorrências: {}".format(x, dist.cdf(x)))

# Definindo a probabilidade de um intervalo >x
x = 2
print("Probabilidade de sucesso para maior que {} ocorrências: {}".format(x, 1 - dist.cdf(x)))