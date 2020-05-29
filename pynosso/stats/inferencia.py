from math import sqrt, ceil

def margem_erro(z, dp, n, popfin=False, N=None):
    if popfin:
        return round(z*(dp/sqrt(n)*(sqrt((N-n)/(N-1)))),4)
    
    return round(z*(dp/sqrt(n)),4)


def tamanho_amostra(z, dp, e, popfin=False, N=None):
    if popfin:
        return ceil((N*(dp**2)*(z**2))/((N-1)*(e**2)+(dp**2)*(z**2)))
    
    return ceil(((z*dp)/e)**2)