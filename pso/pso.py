import math
from random import uniform
from random import randint

import numpy as np
import matplotlib.pyplot as plt

arq = open("saida.txt",'w')

analise = 100
tamanho_populacao = 10
conhecidos = 3
inercia = 0.5
c1 = 1.2
c2 = 1.5
geracoes = 100
melhores = []

def iniciaPopulacao():

	populacao = []

	for i in range(0, tamanho_populacao):
		populacao.append(uniform(-1.0,2.0))

	return populacao

def conhecido_ind(conhecidos, posicao):

	conhece = []
	for i in range(0, conhecidos):
		aux = randint(0, tamanho_populacao-1)
        if((aux not in conhece) and (aux != posicao)):
            conhece.append(aux)
        else:
            while((aux in conhece) or (aux == posicao)):
                aux = randint(0, tamanho_populacao-1)
            conhece.append(aux)
			

	return conhece

def melhor(vizinhos, fit):

	melhores_vizinhos = []
	for i in range(0, len(vizinhos)):
		melhores_vizinhos.append(fit[vizinhos[i]])

	return melhores_vizinhos.index(max(melhores_vizinhos))


def velocidade(v, fit_geral, fit_ind, x):

	return inercia * v + c1*r1*(fit_ind-x) + c2*r2*(fit_geral-x) 

def atualizaX(x, v):

	return x + v

def fitness(x):

    return (x*(math.sin(10*math.pi*x))) + 1

def plota(melhores):
    x = []
    y = []

    for k in range(0,geracoes):
        x.append(k)
        y.append(melhores[k])
    fig,ax = plt.subplots()
    ax.plot(x,y)
    plt.show()

vetor_analise_min = []
vetor_analise_max = []
for j in range(0,analise):
    pop = iniciaPopulacao()
    vInicial = np.zeros(tamanho_populacao)
    i=0

    for i in range(0,geracoes):

        fit = list(map(fitness, pop))

        ind_vizinhos = []

        for i in range(0, tamanho_populacao):
            ind_vizinhos.append(conhecido_ind(conhecidos, tamanho_populacao))

        r1 = uniform(0.0, 1.0)
        r2 = uniform(0.0, 1.0)

        fit_melhor = fit.index(max(fit))

        melhores.append(max(fit))
        
        melhor_ind = []

        for i in range(0, tamanho_populacao):
            melhor_ind.append(melhor(ind_vizinhos[i], fit))

        velocidade_nova = []

        for i in range(0, tamanho_populacao):
            velocidade_nova.append(velocidade(vInicial[i], fit_melhor, melhor_ind[i], pop[i]))

        pop_nova = list(map(atualizaX, pop, vInicial))
        pop = pop_nova
        vInicial = velocidade_nova
        
    #print melhores
    #plota(melhores)
    vetor_analise_min.append(min(melhores))
    vetor_analise_max.append(max(melhores))


arq.write("Menores valores: " + str(vetor_analise_min) + "\n")
arq.write("Maiores valores: " + str(vetor_analise_max) + "\n")
media_valores_max = sum(vetor_analise_max) / len(vetor_analise_max)
media_valores_min = sum(vetor_analise_min) / len(vetor_analise_min)
arq.write("Media dos maiores valores: " + str(media_valores_max) + "\n")
arq.write("Media dos menores valores: " + str(media_valores_min) + "\n")
arq.write("Maior valor: " + str(max(vetor_analise_max)) + "\n")
arq.write("Menor valor: " + str(min(vetor_analise_min)) + '\n')


