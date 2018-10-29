from random import randint
from random import uniform
from igraph import *
import math
import matplotlib.pyplot as plt

grafo = Graph.Read_GraphML('dj38.gml')
vertices = grafo.vs['id']
tamanho_individuo = len(vertices)
tam_pop = 100