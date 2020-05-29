import unittest
from stats import binomial as bi
from stats import exponencial as xp
from stats import poisson as po
from stats import normal as nm
from stats import inferencia as inf


class TestBinomDist(unittest.TestCase):
    def test_binom_prob(self):
        p = 0.02
        n = 10
        x = 2
        prob = bi.binom_prob(n, p, x) 
        self.assertEqual(prob, 0.0153)


class TestPoissonDist(unittest.TestCase):
    def test_poisson_prob(self):
        mu = 0.3
        x = 2
        prob = po.poisson_prob(mu, x) 
        self.assertEqual(prob, 0.0333)


class TestExpDist(unittest.TestCase):
    def test_exp_prob(self):
        alpha = 1/8000 
        a = 0
        b = 4000
        prob = xp.exp_prob(a, b, alpha) 
        self.assertEqual(prob, 0.3935)


class TestNormalDist(unittest.TestCase):
    def test_reduzir_normal_padrao(self):
        med = 140
        dp = 20
        x = 165.6
        z = nm.reduzir_normal_padrao(x, med, dp) 
        self.assertEqual(z, 1.28)


class TestInferencia(unittest.TestCase):
    def test_margem_erro(self):
        dp_pop = 1.5
        n = 20
        z = 1.64
        self.assertEqual(inf.margem_erro(z, dp_pop, n), 0.5501)
    
    def test_tamanho_amostra_infinita(self):
        dp_pop = 6250 
        z = 1.96
        e = 1000
        self.assertEqual(inf.tamanho_amostra(z, dp_pop, e), 151)

    def test_tamanho_amostra_finita(self):
        dp_pop = 7000 
        z = 1.64
        e = 600
        self.assertEqual(inf.tamanho_amostra(z, dp_pop, e, popfin=True, N=420), 196)


if __name__ == '__main__':
    unittest.main()