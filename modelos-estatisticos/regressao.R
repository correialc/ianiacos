
# DADOS

getwd() 
setwd(".//dados") 
getwd()

dados1 <- read.csv("correl_ex1.csv") 

# Estatistica Descritiva
summary(dados1$vendas) 
summary(dados1$comerciais) 

# Histograma
hist(dados1$comerciais) 
hist(dados1$vendas) 

# Dispersao
plot(dados1$vendas,dados1$comerciais)

#Correlacao
cor(dados1$comerciais,dados1$vendas) # Correlacao de Pearson
cor.test(dados1$comerciais,dados1$vendas) # Teste da Correlacao de Pearson


##########################
# REGRESSAO LINEAR SIMPLES
##########################

modelo1 <- lm(dados1$vendas~dados1$comerciais,dados1) # Fit
summary(modelo1)
plot(modelo1)


###########################
# REGRESSAO LINEAR MULTIPLA
###########################

library("readxl")
dados2 <- read_excel("Regress_ex2.XLS")

modelo2 <- lm(dados2$x1~dados2$x2+dados2$x3,dados2)
summary(modelo2)
plot(modelo2)

