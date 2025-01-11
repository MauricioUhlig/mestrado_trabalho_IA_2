from Problema import Problema
import numpy as np
import pandas as pd
import random
import math
import copy
from numba import njit


class TSP(Problema):
    'Travelling Salesman Problem'
    def __init__(self, coordenadas: pd.DataFrame):
        print(f'Shape das coordenadas: {coordenadas.shape}\n\n')
        self.coordenadas = coordenadas
        self.n_cidades = coordenadas.shape[0]
        self.cidades = np.array([a - 1 for a in self.coordenadas.index.to_list()])  # NumPy array
       
        self.qtd_calculo_custo = 0
        self.solucao = self.solucao_aleatoria()  # NumPy array

        self.custo = self.calcula_custo(self.solucao)

        self.custo_original = self.custo
        self.solucao_original = self.solucao.copy()

    def distancia(self, coordenadas: pd.DataFrame):
        'distancia Euclidiana entre dois pontos'
        ponto1 = coordenadas.iloc[0].values
        ponto2 = coordenadas.iloc[1].values

        distancia = np.linalg.norm(ponto2 - ponto1)

        return distancia

    def calcula_custo(self, solucao: np.ndarray):
        '''
        Função Objetivo: calcula custo de uma dada solução.
        '''
        custo = calcula_custo_numba(solucao, self.coordenadas.values)
        self.qtd_calculo_custo += 1
        return custo

    def gera_vizinhos(self, solucao):
        """
        Gera todos os vizinhos possíveis trocando dois elementos da solução.
        O primeiro elemento é fixo.
        """
        return gera_vizinhos_numba(solucao)

    def gera_vizinho_aleatorio(self):
        """
        Gera um vizinho aleatório trocando dois elementos da solução.
        """
        return gera_vizinho_aleatorio_numba(self.solucao)

    def solucao_aleatoria(self):
        'Cria uma solução inicial com as cidades em uma ordem aleatória'
        return solucao_aleatoria_numba(self.cidades)

    def calcula_crossover(self, outro_problema: "Problema") -> "Problema":
        'Realiza o operador de OX Crossover (Order Crossover) entre dois pais'
        tamanho = len(self.solucao)
        filho = np.full(tamanho, -1)  # Inicializa o filho com valores de marcador (-1)

        # Escolhe dois pontos de corte aleatórios
        inicio, fim = sorted(np.random.choice(tamanho, 2, replace=False))

        # Copia o segmento do primeiro pai para o filho
        filho[inicio:fim + 1] = self.solucao[inicio:fim + 1]

        # Usando um set para rastrear genes já adicionados
        genes_adicionados = set(filho[inicio:fim + 1])

        # Preenche o restante dos valores do segundo pai, mantendo a ordem relativa
        i = (fim + 1) % tamanho
        for gene in outro_problema.solucao:
            if gene not in genes_adicionados:
                filho[i] = gene
                genes_adicionados.add(gene)
                i = (i + 1) % tamanho

        problema_copia = copy.deepcopy(self)
        problema_copia.set_solucao(filho)
        return problema_copia
    
    def gera_mutacao(self):
        'Gera mutação na solução'
        i, j = np.random.choice(len(self.solucao), 2, replace=False)
        self.solucao[i], self.solucao[j] = self.solucao[j], self.solucao[i]
        self.set_solucao(self.solucao)

    @staticmethod
    def calcula_nova_temperatura(temperatura_atual: float, taxa_resfriamento: float):
        return temperatura_atual * taxa_resfriamento

#####################################################################################

@njit
def distancia_numba(ponto1, ponto2):
    'Calcula a distância Euclidiana entre dois pontos'
    return np.linalg.norm(ponto2 - ponto1)

@njit
def calcula_custo_numba(solucao, coordenadas_values):
    '''
    Calcula o custo total de uma solução.
    '''
    n_cidades = len(solucao)
    custo = 0

    for i in range(n_cidades):
        k = (i + 1) % n_cidades
        cidadeA = solucao[i]
        cidadeB = solucao[k]
        custo += distancia_numba(coordenadas_values[cidadeA], coordenadas_values[cidadeB])

    return custo


@njit
def gera_vizinhos_numba(solucao):
    n_cidades = len(solucao)
    for i in range(1, n_cidades):  # Deixa o primeiro fixo
        for j in range(i + 1, n_cidades):
            vizinho = solucao.copy()
            vizinho[i], vizinho[j] = vizinho[j], vizinho[i]
            yield vizinho

@njit
def gera_vizinho_aleatorio_numba(solucao: np.ndarray):
    n_cidades = len(solucao)
    i, j = np.random.choice(n_cidades, 2, replace=False)
    vizinho = solucao.copy()
    vizinho[i], vizinho[j] = vizinho[j], vizinho[i]
    return vizinho

@njit
def solucao_aleatoria_numba(cidades):
    '''
    Cria uma solução inicial com as cidades em uma ordem aleatória.
    '''
    solucao = cidades.copy()  # Cria uma cópia do array de cidades
    for i in range(len(solucao) - 1, 0, -1):  # Implementação de Fisher-Yates Shuffle
        j = np.random.randint(0, i + 1)
        solucao[i], solucao[j] = solucao[j], solucao[i]
    return solucao