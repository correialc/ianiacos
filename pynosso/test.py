import unittest
from stats import binomial as bi
from stats import exponencial as xp
from stats import poisson as po
from stats import normal as nm
from stats import inferencia as inf
from stats import hipoteses as hip

# Distribuicao Binomial
class TestBinomDist(unittest.TestCase):
    def test_binom_prob(self):
        p = 0.02
        n = 10
        x = 2
        prob = bi.binom_prob(n, p, x) 
        self.assertEqual(prob, 0.0153)


# Distribuition de Poisson
class TestPoissonDist(unittest.TestCase):
    def test_poisson_prob(self):
        mu = 0.3
        x = 2
        prob = po.poisson_prob(mu, x) 
        self.assertEqual(prob, 0.0333)


# Distribution Exponencial
class TestExpDist(unittest.TestCase):
    def test_exp_prob(self):
        alpha = 1/8000 
        a = 0
        b = 4000
        prob = xp.exp_prob(a, b, alpha) 
        self.assertEqual(prob, 0.3935)


# Distribuicao Normal
class TestNormalDist(unittest.TestCase):
    def test_reduzir_normal_padrao(self):
        med = 140
        dp = 20
        x = 165.6
        z = nm.reduzir_normal_padrao(x, med, dp) 
        self.assertEqual(z, 1.28)
    
    def test_reverter_reducao_normal_padrao(self):
        med = 130
        dp = 20
        z = 0.67
        x = nm.reverter_reducao_normal_padrao(z, med, dp) 
        self.assertEqual(x, 143.4)


# Inferencia Estatistica (Media)
class TestInferenciaMedia(unittest.TestCase):
    
    # Distribuicao: Normal Reduzida
    # Populacao: Infinita
    # Desvio Padrao Populacional: Conhecido
    def test_media_margem_erro_pop_infinita(self):
        sigma = 1.5
        n = 20
        z = 1.64
        self.assertEqual(inf.media_margem_erro(z, sigma, n), 0.5501)


    # Distribuicao: Normal Reduzida
    # Populacao: Infinita
    # Desvio Padrao Populacional: Conhecido
    def test_media_margem_erro_pop_finita(self):
        n = 16      # (grau de liberdade = 15)
        t = 2.602
        s = 40
        self.assertEqual(inf.media_margem_erro(t, s, n), 26.02)
 

    # Distribuicao: Normal Reduzida
    # Populacao: Infinita
    # Desvio Padrao Populacional: Conhecido
    def test_media_tamanho_amostra_pop_infinita(self):
        sigma = 6250 
        z = 1.96
        e = 1000
        self.assertEqual(inf.media_tamanho_amostra(z, sigma, e), 151)


    # Distribuicao: Normal Reduzida
    # Populacao: Finita
    # Desvio Padrao Populacional: Conhecido
    def test_media_tamanho_amostra_pop_finita_normal(self):
        sigma = 7000 
        z = 1.64
        e = 600
        self.assertEqual(inf.media_tamanho_amostra(z, sigma, e, N=420), 196)


# Inferencia Estatistica (Proporcao)
class TestInferenciaProporcao(unittest.TestCase):
    
    def test_prop_margem_erro_condicao_invalida(self):
        n = 125
        x = 1 
        pa = x/n    
        z = 1.51

        # Condicao invalida: (n*pa) menor do 5 
        with self.assertRaises(ValueError):
            inf.prop_margem_erro(z, pa, n)

        x = 124
        pa = x/n

        # Condicao invalida: n*(1 - pa) menor do 5
        with self.assertRaises(ValueError):
            inf.prop_margem_erro(z, pa, n)


    # Distribuicao: Normal Reduzida
    # Populacao: Infinita
    def test_prop_margem_erro_pop_infinita(self):
        x = 7
        n =125
        pa = x/n
        z = 1.51
        self.assertEqual(inf.prop_margem_erro(z, pa, n), 0.0311)


    # Distribuicao: Normal Reduzida
    # Populacao: Infinita
    def test_prop_tamanho_amostra_pop_infinita(self):
        e = 0.03
        pa = 0.18
        z = 1.96
        self.assertEqual(inf.prop_tamanho_amostra(z, pa, e), 631)

    
    # Distribuicao: Normal Reduzida
    # Populacao: Finita
    def test_prop_tamanho_amostra_pop_finita(self):
        e = 0.05
        N = 550
        z = 2.17
        pa = 0.23
        self.assertEqual(inf.prop_tamanho_amostra(z, pa, e, N=N), 208)


# Testes de Hipoteses
class TestTestesHipoteses(unittest.TestCase):
    
    # Teste z para a media
    def test_media_testez(self):
        xhat = 6300
        mu0 = 6500
        sigma = 2000
        n = 55
        self.assertEqual(hip.media_testez(xhat, mu0, sigma, n), -0.7416)

    # Teste t para a media
    def test_media_testet(self):
        xhat = 50
        mu0 = 60
        s = 20
        n = 9
        self.assertEqual(hip.media_testet(xhat, mu0, s, n), -1.5)


    # Teste z para a proporcao
    def test_prop_testez(self):
        n = 821
        phat = 46/n
        p0 = 0.078
        self.assertEqual(hip.prop_testez(phat, p0, n), -2.3475)


    # Teste z para duas amostras (proporcao)
    def test_prop_testez_duas_amostras(self):
        n1 = 134
        n2 = 145
        p1 = 122/n1
        p2 = 127/n2
        self.assertEqual(hip.prop_testez_duas_amostras(p1, p2, n1, n2), 0.9317)


    # Teste t para duas amostras dependentes (media)
    def test_media_testet_amostras_dependentes(self):
        di_med = 11.4
        di_std = 8.6197
        n = 5
        self.assertEqual(hip.media_testet_amostras_dependentes(di_med, di_std, n), 2.9573)


    # Teste t para duas amostras independentes homocedasticas (media)
    def test_media_testet_amostras_independentes_homocedasticas(self):
        x1 = 11.57
        x2 = 15.38
        s1 = 4.1**2
        s2 = 4.3**2
        n1 = 14
        n2 = 13
        self.assertEqual(hip.media_testet_amostras_independentes(x1, x2, n1, n2, s1, s2, True), -2.3568)


    # Teste t para duas amostras independentes homocedasticas (media)
    def test_media_testet_amostras_independentes_heterocedasticas(self):
        x1 = 40.2
        x2 = 36.7
        s1 = 0.7**2
        s2 = 1.9**2
        n1 = 20
        n2 = 15
        self.assertEqual(hip.media_testet_amostras_independentes(x1, x2, n1, n2, s1, s2, False), 6.7969)

if __name__ == '__main__':
    unittest.main()