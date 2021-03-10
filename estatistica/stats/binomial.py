from scipy.stats import binom


def exibir_binom_stats(n, p):
    print(f"Média: {binom.mean(n, p)}, Variância: {binom.var(n, p)}, Desvio: {binom.std(n, p)}")


def binom_prob(n, p, x):
    dist = binom(n, p)
    return(round(dist.pmf(x),4))