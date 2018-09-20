from random import randint
from random import uniform
from random import random
import math
import matplotlib.pyplot as plt

tamanho_populacao = 50
numero_individuos = 8
geracoes = 200
alfa = 0.8
melhores = []
individuo = []
arq = open("saida.txt",'w')


def mochila():
	produtos = []
	produtos.append([11,1])
	produtos.append([21,11])
	produtos.append([31,21])
	produtos.append([33,23])
	produtos.append([43,33])
	produtos.append([53,43])
	produtos.append([55,45])
	produtos.append([65,55])
	return produtos

def geraIndividuo():
	for i in range(0,tamanho_populacao):
		individuo.append([])
		for j in range(0,numero_individuos):
			if(random()< 0.5):
				individuo[i].append(0)
			else:
				individuo[i].append(1)
	return individuo

def geraPeso(individuo):
	peso_individuo = 0
	utilidade_mochila = 0
	for i in range(0,len(individuo)):
		if(individuo[i] == 1):
			peso_individuo = peso_individuo + mochila[i][0]
			utilidade_mochila = utilidade_mochila + mochila[i][1]
	mochila_individuo = []
	mochila_individuo.append(peso_individuo)
	mochila_individuo.append(utilidade_mochila)
	return mochila_individuo

def fitness(individuo):
	fit_ind = []
	for i in range(0,len(individuo)):
		peso_uti = geraPeso(individuo[i])
		if(peso_uti[0] > 100):
			if(peso_uti[0] >= 200):
				peso_uti[0] = 100
				peso_uti[1] = 0
			else:
				extrapola = peso_uti[0] - 100
				porcentagem_extrapolada = float(extrapola) / float(100)
				reduz_uti = porcentagem_extrapolada * float(peso_uti[1])
				peso_uti[0] = 100
				peso_uti[1] = peso_uti[1] - reduz_uti
			fit_ind.append(peso_uti)
		else:
			fit_ind.append(peso_uti)
	return fit_ind

def roleta(porcentagem_individual):
	roleta = uniform(0.0, 1.0)
	soma = 0
	j = 0
	while(soma <= roleta):
		soma = soma + porcentagem_individual[j]
		j = j + 1
	pos_pai = j - 1
	return pos_pai

def selecao(fit_ind):
	porcentagem_individual = []
	total_uti = 0
	for i in range(0, len(fit_ind)):
		total_uti = total_uti + fit_ind[i][1]
	for j in range(0, len(fit_ind)):
		porcentagem = float(fit_ind[j][1]) / float(total_uti)
		porcentagem_individual.append(porcentagem)
	pai1 = roleta(porcentagem_individual)
	pai2 = roleta(porcentagem_individual)
	pais = []
	pais.append(pai1)
	pais.append(pai2)
	return pais

def cruzamento(pai1, pai2):
	randao = uniform(0, 8)
	pos = int(randao)
	filho = []
	for i in range(0,len(pai1)):
		if(i < pos):
			filho.append(pai1[i])
		else:
			filho.append(pai2[i])
	return filho

def plota(melhores):
	x = []
	y = []
	for k in range(0,geracoes):
		x.append(k)
		y.append(melhores[k])
	fig,ax = plt.subplots()
	ax.plot(x, y)
	plt.show()

mochila = mochila()
analise = 100
m = 0
melhores = []
vetor_analise_min = []
vetor_analise_max = []

while(m < analise):
	individuo = []
	individuo = geraIndividuo()
	k = 0

	while(k < geracoes):
		filhos = []
		fit_pais = []
		fit_ind = fitness(individuo)
		for i in range(0,len(individuo)):
			fit_pais.append(fit_ind[i][1])
			pai = selecao(fit_ind)
			fi = cruzamento(individuo[pai[0]], individuo[pai[1]])
			filhos.append(fi)
		melhores.append(max(fit_pais))
		individuo = filhos
		k = k + 1
	vetor_analise_min.append(min(melhores))
	vetor_analise_max.append(max(melhores))
	m = m + 1


arq.write("Menores valores: " + str(vetor_analise_min) + "\n")
arq.write("Maiores valores: " + str(vetor_analise_max) + "\n")
media_valores_max = sum(vetor_analise_max) / len(vetor_analise_max)
media_valores_min = sum(vetor_analise_min) / len(vetor_analise_min)
arq.write("Media dos maiores valores: " + str(media_valores_max) + "\n")
arq.write("Media dos menores valores: " + str(media_valores_min) + "\n")
arq.write("Maior valor: " + str(max(vetor_analise_max)) + "\n")
arq.write("Menor valor: " + str(min(vetor_analise_min)) + '\n')
