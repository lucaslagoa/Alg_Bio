from random import randint
from random import uniform
import math
import matplotlib.pyplot as plt

tamanho_populacao = 50
numero_individuos = 3
taxa_mutacao = 0.05
geracoes = 200
alfa = 0.8
melhores = []
individuo = []

def roleta(porcentagem_individual):
	roleta = uniform(0.0, 1.0)
	soma = 0
	j = 0
	while(soma <= roleta):
		soma = soma + porcentagem_individual[j]
		j = j + 1
	pos_pai = j - 1
	return pos_pai

def selecao(total_fit, fit_uni):
	porcentagem_individual = []
	maximiza = []
	for i in range(0,len(fit_uni)):
		maximiza.append(1 / fit_uni[i])
	total_fit = sum(maximiza)
	for i in range(0,len(fit_uni)):
		porcent = maximiza[i] / total_fit
		porcentagem_individual.append(porcent)
	pai1 = roleta(porcentagem_individual)
	pai2 = roleta(porcentagem_individual)
	pais = []
	pais.append(pai1)
	pais.append(pai2)
	return pais

def cruzamento(individuo, pais):
	pos1 = individuo[pais[0]][0]
	pos2 = individuo[pais[1]][0]
	pos3 = individuo[pais[0]][1] 
	pos4 = individuo[pais[1]][1]  
	pos5 = individuo[pais[0]][2]
	pos6 = individuo[pais[1]][2]
	media1 = (pos1+pos2)/2
	media2 = (pos3+pos4)/2
	media3 = (pos5+pos6)/2
	filho = []
	filho.append(media1)
	filho.append(media2)
	filho.append(media3)
	return filho

def blend_fator(extrapola, fp1, fp2):
	d = fp1 - fp2
	if (d < 0):
		menor = fp1 - extrapola
		maior = fp2 + extrapola
	else:
		menor = fp2 - extrapola
		maior = fp1 + extrapola
	fator_novo = uniform(float(menor), float(maior))
	return fator_novo

def cruzamento_blend(individuo, pais):
	d1 = individuo[pais[0]][0] - individuo[pais[1]][0]
	d2 = individuo[pais[0]][1] - individuo[pais[1]][1]
	d3 = individuo[pais[0]][2] - individuo[pais[1]][2]
	extrapola1 = (abs(d1) * alfa)
	extrapola2 = (abs(d2) * alfa)
	extrapola3 = (abs(d3) * alfa)
	f1 = blend_fator(extrapola1, individuo[pais[0]][0], individuo[pais[1]][0])
	f2 = blend_fator(extrapola2, individuo[pais[0]][1], individuo[pais[1]][1])
	f3 = blend_fator(extrapola3, individuo[pais[0]][2], individuo[pais[1]][2])
	filho = []
	filho.append(f1)
	filho.append(f2)
	filho.append(f3)
	return filho



for i in range(0,tamanho_populacao):
    individuo.append([])
    for j in range(0,numero_individuos):
        a = uniform(-2.0,2.0)
        individuo[i].append(a)

y = 0

while(y<geracoes):
    
    z = []
    for i in range(0,len(individuo)):
        x = 0
        for j in range(0,numero_individuos):
            x += (1.0/(individuo[i][j])**2)
        x = math.sqrt(x)
        z.append(x)

    random = []
    ind = []
    total_fit = 0
    for i in range(0, len(z)):
    	total_fit = total_fit + z[i]
   
    filhos = []

    for i in range(0,(tamanho_populacao/2)):
    	pais = selecao(total_fit, z)
    	fi = cruzamento_blend(individuo, pais)       
        filhos.append(fi)
        fi2 = cruzamento_blend(individuo, pais)       
        filhos.append(fi2)


    fitfilhos = []


    for i in range(0,len(filhos)):
    	for j in range(0,numero_individuos):
    		x = uniform(0.0,1.0)
    		if(taxa_mutacao>x):
    			filhos[i][j] = uniform(-2.0,2.0)
    for i in range(0,len(filhos)):
        x = 0
        for j in range(0,numero_individuos):
            x += (1.0/(filhos[i][j])**2)
        x = math.sqrt(x)
        fitfilhos.append(x)

    test1 = sorted(z)
    indice_melhor = z.index(min(z))
    aux = individuo[indice_melhor]
    individuo = []
    individuo = filhos
    individuo[0] = aux
    melhores.append(test1[0])
    y = y + 1
    
print min(melhores)
idf = melhores.index(min(melhores))
#print idf
x = []
y = []
for k in range(0,geracoes):
	x.append(k)
	y.append(melhores[k])

fig,ax = plt.subplots()
ax.plot(x, y)
plt.show()