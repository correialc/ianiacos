from math import sqrt

def media_testez(xhat, mu, sigma, n):
    return round((xhat - mu)/(sigma/sqrt(n)), 4) 

def media_testet(xhat, mu, s, n):
    return round((xhat - mu)/(s/sqrt(n)), 4) 

def prop_testez(phat, p0, n):
    return round((phat-p0)/sqrt((p0*(1-p0))/(n)), 4)
