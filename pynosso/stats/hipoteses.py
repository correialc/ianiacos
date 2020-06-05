from math import sqrt

def testez(xhat, mu, sigma, n):
    return round((xhat - mu)/(sigma/sqrt(n)),4) 
