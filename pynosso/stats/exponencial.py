from math import exp


def exibir_exp_stats(alpha):
    med = lambda alpha : 1 / alpha
    var = lambda alpha : 1 / (alpha ** 2)
    print(f"Média: {med(alpha)}, Variância: {var(alpha)}")


def exp_prob(a, b, alpha):
    return exp(-alpha*a)-exp(-alpha*b)
