import unittest
from stats import binomial as bi
from stats import exponencial as xp
from stats import poisson as po
from stats import normal as nm


class TestBinomDist(unittest.TestCase):
    def test_binom_prob(self):
        p = 0.02
        n = 10
        x = 2
        prob = bi.binom_prob(n, p, x) 
        self.assertEqual(prob, 0.015313734406472136)


class TestPoissonDist(unittest.TestCase):
    def test_poisson_prob(self):
        mu = 0.3
        x = 2
        prob = po.poisson_prob(mu, x) 
        self.assertEqual(prob, 0.033336819930677296)


class TestExpDist(unittest.TestCase):
    def test_exp_prob(self):
        alpha = 1/8000 
        a = 0
        b = 4000
        prob = xp.exp_prob(a, b, alpha) 
        self.assertEqual(prob, 0.3934693402873666)


class TestNormalDist(unittest.TestCase):
    def test_reduzir_normal_padrao(self):
        med = 140
        dp = 20
        x = 165.6
        z = nm.reduzir_normal_padrao(x, med, dp) 
        self.assertEqual(z, 1.28)


if __name__ == '__main__':
    unittest.main()