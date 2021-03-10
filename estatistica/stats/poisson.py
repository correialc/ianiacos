from scipy.stats import poisson


def exibir_poisson_stats(mu): 
    print(f"Média: {poisson.mean(mu)}, Variância: {poisson.var(mu)}, Desvio: {poisson.std(mu)}")


def poisson_prob(mu, x):
    dist = poisson(mu)
    return round(dist.pmf(x),4)