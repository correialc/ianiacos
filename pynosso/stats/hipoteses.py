from math import sqrt

def testez(xhat, mu, sigma, n):
    return round((xhat - mu)/(sigma/sqrt(n)),4) 

def testet(xhat, mu, s, n):
    return round((xhat - mu)/(s/sqrt(n)),4) 
