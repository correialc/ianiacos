import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm


# Redução à normal padrão de uma variável X com distribuição normal, 
# média (med) <> 0 e/ou desvio padrão (dp) <> 1
def reduzir_normal_padrao(x, med, dp):
    return (x - med)/dp


# Plota a curva da distribuição normal preenchendo um intervalo de probabilidade de z1 a z2
def plotar_normal(z1, z2):
    # Fonte: Adaptada de Peter Kazarinoff 
    # https://pythonforundergradengineers.com/plotting-normal-curve-with-python.html

    # z1 : Limite inferior da probabilidade (menor valor da v. a. X) reduzido à Normal Padrão
    # z2 : Limite superior da probabilidade (maior valor da v. a. X) reduzido à Normal Padrão
    # save : Indica se a figura deve ser persistida em arquivo

    x = np.arange(z1, z2, 0.001)    # intervalo de x
    x_completo = np.arange(-10, 10, 0.001)   # intervalo total de x
    
    y = norm.pdf(x,0,1)
    y_completo  = norm.pdf(x_completo,0,1)

    # Plotar gráfico
    fig, ax = plt.subplots(figsize=(9,6))
    plt.style.use('fivethirtyeight')
    ax.plot(x_completo,y_completo)

    ax.fill_between(x,y,0, alpha=0.3, color='b')
    ax.fill_between(x_completo, y_completo, 0, alpha=0.1)
    ax.set_xlim([-4,4])
    ax.set_yticklabels([])
    ax.set_title('Curva da Distribuição Normal')
    
    plt.show()