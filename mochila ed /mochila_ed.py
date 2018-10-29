from random import randint
from random import uniform
import math
import matplotlib.pyplot as plt
import random

tamanho_populacao = 10
numero_individuos = 8
cr = 0.8
F = 0.3
#f = 1.0 #0.6
geracoes = 10
melhores = []
individuo = []

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

def popInicial():
	for i in range(0,tamanho_populacao):
		individuo.append([])
		for j in range(0,numero_individuos):
			if(random.random()<0.5):
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
	peso_uti = geraPeso(individuo)
	if(peso_uti[0] > 100):
		if(peso_uti[0] >= 200):
			peso_uti[0] = 199
		extrapola = peso_uti[0] - 100
		porcentagem_extrapolada = float(extrapola) / float(100)
		reduz_uti = porcentagem_extrapolada * float(peso_uti[1])
		peso_uti[0] = 100
		peso_uti[1] = peso_uti[1] - reduz_uti
		fit_ind.append(peso_uti)
	else:
		fit_ind.append(peso_uti)
	return fit_ind

def mutacao(individuo):
	x1 = 0
	x2 = 1
	x3 = 2
	while((x1 != x3) and (x1 != x2) and (x2 != x3)):
		x1 = uniform(0.0, float(tamanho_populacao))
		x2 = uniform(0.0, float(tamanho_populacao))
		x3 = uniform(0.0, float(tamanho_populacao))
		x1 = int(x1)
		x2 = int(x2)
		x3 = int(x3)
	ind1 = individuo[x1]
	ind2 = individuo[x2]
	ind3 = individuo[x3]
	for i in range(0,numero_individuos):
		if uniform(0.0,1) <= F:
			ind1[i] = ind1[i] or ind2[i] 
		#ind1[i] = ind1[i] + (ind3[i] * ind2[i])
		#if ind1[i] > 1:
			#ind1[i] = 1
	return ind1 

def cruzamento(individuo, pop_inter):
	filhos = []
	for i in range(0,tamanho_populacao):
		filho = []
		for j in range(0, numero_individuos):
			random = uniform(0.0, 1.0)
			if(random < cr):
				filho.append(individuo[i][j])
			else:
				filho.append(pop_inter[i][j])
		filhos.append(filho)
	return filhos

def prox_geracao(individuo, filhos, fit_pai):
	novo_ind = []
	for i in range(0, len(individuo)):
		fit_filho = fitness(filhos[i])
		if (fit_pai[i][0][1] > fit_filho[0][1]):
			novo_ind.append(individuo[i])
		else:
			novo_ind.append(filhos[i])
	return novo_ind

def fit_geral(populacao):
	fit_geral = [0] * tamanho_populacao
	for i in range(0, len(populacao)):
		fit_i = fitness(populacao[i])
		fit_geral[i] = fit_i
	return fit_geral

mochila = mochila()
individuo = popInicial()
k = 0
melhor = []

while(k<geracoes):

	print individuo
	
	pop_int = []
	novo_ind = []
	fit_melhor = []
	fit_melhor = fit_geral(individuo)

	for i in range(0,tamanho_populacao):
		ind_int = mutacao(individuo)
		pop_int.append(ind_int)
	
	filhos = cruzamento(individuo, pop_int)
	novo_ind = prox_geracao(individuo, filhos, fit_melhor)
	
	util = []
	for i in range(0,len(fit_melhor)):
		util.append(fit_melhor[i][0][1])
	index = util.index(max(util))
	melhor.append(max(util))
	novo_ind[0] = individuo[index][:]
	k = k + 1
	individuo = novo_ind[:]

print melhor
