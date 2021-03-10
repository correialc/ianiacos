
# DADOS

getwd() 
setwd(".//dados") 
getwd()

Dados <- read.csv2("Titanic.csv")


# Regressao Logistica Simples para a variavel Sexo
modelo1=glm(Dados$Sobrevivente~Dados$Sexo,family=binomial(link="logit"));modelo1
summary(modelo1)
modelo1$coefficients
odds <- exp(-2.477825)    # razao de chance feminino/masculino
odds <- 1/exp(-2.477825)  # razao de chance masculino/feminino

# Regressao Logistica Simples para a variavel Idade
modelo2=glm(Dados$Sobrevivente~Dados$Idade,family=binomial(link="logit"));modelo2
summary(modelo2)
modelo2$coefficients
oddsIdade <- exp(-0.01096)

# Regressao Logistica Simples para a variavel Classe
modelo3=glm(Dados$Sobrevivente~Dados$Classe,family=binomial(link="logit"));modelo3
summary(modelo3)
modelo3$coefficients
oddsClasse <- exp(-0.9119899)

# Regressao Logistica Simples para a variavel Classe (categorica)
class(Dados$Classe)
Dados$Classecat <- as.factor(Dados$Classe)
class(Dados$Classecat)

modelo4=glm(Dados$Sobrevivente~Dados$Classecat,family=binomial(link="logit"));modelo4
summary(modelo4)
modelo4$coefficients
oddsClasseCat12 <- exp(-0.7261)
oddsClasseCat13 <- exp(-1.8009)


# Regressao Logistica para multiplas variaveis
modelo5=glm(Dados$Sobrevivente~Dados$Sexo+Dados$Idade+Dados$Irmãos+Dados$Pais+Dados$Classecat,family=binomial(link="logit"));modelo5
summary(modelo5)
modelo5$coefficients

proby <- exp(4.356474-2.642267-0.044836*44-0.368280)/(1+exp(4.356474-2.642267-0.044836*44-0.368280))
