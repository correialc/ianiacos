from scipy.stats import poisson

# Exemplos de uso
# Gerando a distribuicao
mu = 0.3 # Para um intervalo contínuo e limitado
dist = poisson(mu)

# Estatísticas da distribuição
estats = lambda mu : print(f"Média: {poisson.mean(mu)}, Variância: {poisson.var(mu)}, Desvio: {poisson.std(mu)}") 
estats(mu)

# Definindo a probabilidade de um x específico
x = 2
print("Probabilidade de exatamente {} ocorrências: {}".format(x, dist.pmf(x)))

# Definindo a probabilidade de um intervalo <=x
x = 2
print("Probabilidade de até {} ocorrências: {}".format(x, dist.cdf(x)))

# Definindo a probabilidade de um intervalo >x
x = 2
print("Probabilidade maior que {} ocorrências: {}".format(x, 1 - dist.cdf(x)))