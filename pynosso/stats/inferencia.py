from math import sqrt, ceil

def print_intervalo_confianca(val, e, percent=False):
    if percent:
        print("Intervalo confiança: [{:5.2f}% ; {:5.2f}%]".format((val-e)*100, (val+e)*100))
    else:
        print("Intervalo confiança: [{:6.4f} ; {:6.4f}]".format(val-e, val+e))


def media_margem_erro(vc, dp, n, N=None):
    # vc: Variavel Critica:
    #   z de alpha/2, para Distribuicao Normal Reduzida
    #   t de alpha/2, para Distribuicao t-Student

    # dp: Desvio Padrao:
    #   sigma, quando desvio padrao populacional conhecido
    #   s, quando desvio padrao populacional desconhecido   
    
    if N is not None:
        return round(vc*((dp/sqrt(n))*(sqrt((N-n)/(N-1)))),4)
    
    return round(vc*(dp/sqrt(n)),4)


def media_tamanho_amostra(vc, dp, e, N=None):
    # vc: Variavel Critica:
    #   z de alpha/2, para Distribuicao Normal Reduzida
    #   t de alpha/2, para Distribuicao t-Student

    # dp: Desvio Padrao:
    #   sigma, quando desvio padrao populacional conhecido
    #   s, quando desvio padrao populacional desconhecido   

    if N is not None:
        return ceil((N*(dp**2)*(vc**2))/((N-1)*(e**2)+(dp**2)*(vc**2)))
    
    return ceil(((vc*dp)/e)**2)


def prop_margem_erro(vc, pa, n, N=None):
    # vc: Variavel Critica:
    #   z de alpha/2, para Distribuicao Normal Reduzida
    #   t de alpha/2, para Distribuicao t-Student
    
    # pa: Proporcao Amostral
    
    if not (n*pa >= 5 and n*(1-pa) >=5):
        raise ValueError("Condicao invalida para o calculo da proporcao!")

    if N is not None:
        # Implementar
        return round( vc*sqrt((pa*(1-pa))/n)*(sqrt((N-n)/(N-1))), 4)
    
    return round(vc*sqrt((pa*(1-pa))/n), 4)


def prop_tamanho_amostra(vc, pa, e, N=None):
    # vc: Variavel Critica:
    #   z de alpha/2, para Distribuicao Normal Reduzida
    #   t de alpha/2, para Distribuicao t-Student
    
    # pa: Proporcao Amostral
    # Quando pa nao estiver disponivel, 0.5 pode ser utilizado como padrao
    
    if N is not None:
        # Implementar
        return ceil((N*pa*(1-pa)*(vc**2))/(pa*(1-pa)*(vc**2)+(N-1)*(e**2))) 

    return ceil(((vc**2)*pa*(1-pa))/(e**2))