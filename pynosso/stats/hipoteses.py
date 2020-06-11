from math import sqrt

def media_testez(xhat, mu, sigma, n):
    return round((xhat - mu)/(sigma/sqrt(n)), 4) 

def media_testet(xhat, mu, s, n):
    return round((xhat - mu)/(s/sqrt(n)), 4) 

def prop_testez(phat, p0, n):
    return round((phat-p0)/sqrt((p0*(1-p0))/(n)), 4)

def prop_testez_duas_amostras(p1, p2, n1, n2):
    phat = ((n1*p1)+(n2*p2))/(n1+n2)
    print(phat)
    z = (p1-p2)/sqrt( ((phat*(1-phat))/n1) + ((phat*(1-phat))/n2) )
    return round(z,4)

def media_testet_amostras_dependentes(di_med, di_std, n):
    tp = di_med/ (di_std/sqrt(n))
    return round(tp, 4)