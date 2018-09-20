import random
import math
import matplotlib.pyplot as plt

arq = open("saida.txt",'w')

def geraPopulacao():
    individuo = []
    for i in range(0,tamanho_populacao):
        individuo.append([])
        for j in range(0,3):
            a = random.uniform(-2.0,2.0)
            individuo[i].append(a)
    return individuo

def mutacao(populacao, f):
    populacaoIntermediaria = []
    for i in range(0, len(populacao)):

        escolhidos = []

        for k in range(0, 3): escolhidos.append(random.randint(0, len(populacao)-1))

        filho = []

        for j in range(0, len(populacao[escolhidos[0]])):
            
            filho.append(populacao[escolhidos[0]][j] + f*(populacao[escolhidos[1]][j] - populacao[escolhidos[2]][j] ) )     

        populacaoIntermediaria.append(filho)
    
    return populacaoIntermediaria


def cruzamento (populacao,popInter):
    popCruzamento = []
    for i in range(0,len(populacao)):
        cruz = random.uniform(0.0,1.0)    
        if(cruz <= 0.8):
            popCruzamento.append(popInter[i])
        else:
            popCruzamento.append(populacao[i])
    return popCruzamento

def fitness(populacao):
    for i in range(0,len(populacao)):
        x = 0
        x += (1.0/(populacao[i]**2))
        x = math.sqrt(x)
    return x

def plota(melhores,num_geracoes):
    x = []
    y = []
    for k in range(0,num_geracoes):
	    x.append(k)
	    y.append(melhores[k])

    fig,ax = plt.subplots()
    ax.plot(x, y)
    plt.show()

num_geracoes = 100
tamanho_populacao = 100
f = 0.7

analise = 100
a = 0
b = 0
#cr 
random.seed()
vetor_analise_min = []
vetor_analise_max = []

while(b<analise):
    melhores = []
    populacao = geraPopulacao()
    a = 0
    while(a < num_geracoes): 
        popInter = mutacao(populacao, f)
        popCruzamento = []

        for i in range(0, len(popInter)):
            popCruzamento.append(cruzamento(populacao[i],popInter[i]))

        valoresFit_pop= map(fitness, populacao)
        valoresFit_filho = map(fitness, popCruzamento)
        minvaloresFit_pop = min(valoresFit_pop)
        minvaloresFit_filho = min(valoresFit_filho)

        if (minvaloresFit_filho < minvaloresFit_pop):
            melhores.append(minvaloresFit_filho)
        else: 
            melhores.append(minvaloresFit_pop)

        np = []

        for i in range(0, len(valoresFit_filho)):

            if valoresFit_filho[i] < valoresFit_pop[i]:
                np.append(popCruzamento[i])
            else:
                np.append(populacao[i])
        populacao = np
        a = a + 1
    vetor_analise_min.append(min(melhores))
    vetor_analise_max.append(max(melhores))
    b = b + 1

arq.write("Menores valores: " + str(vetor_analise_min) + "\n")
arq.write("Maiores valores: " + str(vetor_analise_max) + "\n")
media_valores_max = sum(vetor_analise_max) / len(vetor_analise_max)
media_valores_min = sum(vetor_analise_min) / len(vetor_analise_min)
arq.write("Media dos maiores valores: " + str(media_valores_max) + "\n")
arq.write("Media dos menores valores: " + str(media_valores_min) + "\n")
arq.write("Maior valor: " + str(max(vetor_analise_max)) + "\n")
arq.write("Menor valor: " + str(min(vetor_analise_min)) + '\n')

           
