from math import sqrt

def testez(xhat, mu, sigma, n):
    return ((xhat - mu)/(sigma/sqrt(n))) 
