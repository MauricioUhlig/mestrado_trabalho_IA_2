
from Problema import Problema
import numpy as np
import pandas as pd
import random
import math
import copy

class TSP(Problema):
    'Travelling Salesman Problem'
    def __init__(self, coordenadas : pd.DataFrame ):
        print(f'Shape das coordenadas: {coordenadas.shape}\n\n')
        self.coordenadas = coordenadas
        self.n_cidades = coordenadas.shape[0]
        self.cidades = [a - 1 for a in self.coordenadas.index.to_list()]
       

        self.qtd_calculo_custo = 0
        self.solucao = self.solucao_aleatoria()

        self.custo = self.calcula_custo(self.solucao)

        self.custo_original = self.custo
        self.solucao_original = self.solucao


    def distancia(self,coordenadas : pd.DataFrame):
        'distancia Euclidiana entre dois pontos'
        ponto1 = coordenadas.iloc[0].values
        ponto2 = coordenadas.iloc[1].values

        distancia = np.linalg.norm(ponto2 - ponto1)

        return distancia

    def calcula_custo(self, solucao):
        '''
        Função Objetivo: calcula custo de uma dada solução.
        Obs: Neste caso do problema do caixeiro viajante (TSP problem), o custo é o comprimento da rota entre todas as cidades.
        '''
        custo = 0

        for i in range(self.n_cidades):

            # Quando chegar na última cidade, será necessário
            # voltar para o início para adicionar o
            # comprimento da rota da última cidade
            # até a primeira cidade, fechando o ciclo.
            #
            # Por isso, a linha abaixo:
            k = (i+1) % self.n_cidades
            cidadeA = solucao[i]
            cidadeB = solucao[k]
        
            custo += self.distancia(self.coordenadas.iloc[[cidadeA,cidadeB]])

            #print(tsp.loc[cidadeA, cidadeB], cidadeA,cidadeB)
        self.qtd_calculo_custo += 1
        return custo

    def gera_vizinhos(self, solucao):
        for i in range(1, self.n_cidades):       # deixa o primeiro fixo
            for j in range(i + 1, self.n_cidades):
                vizinho = solucao[:i] + [solucao[j]] + solucao[i+1:j] + [solucao[i]] + solucao[j+1:]
                yield vizinho

    def gera_vizinho_aleatorio(self):
        i, j = random.sample(range(self.n_cidades), 2)
        new_route = self.solucao[:]
        new_route[i], new_route[j] = new_route[j], new_route[i]
        return new_route


    def obtem_melhor_vizinho(self, solucao):
        melhor_custo = self.calcula_custo(solucao)
        melhor_vizinho = solucao

        for vizinho in self.gera_vizinhos(solucao):
            custo_atual = self.calcula_custo(vizinho)
            
            if custo_atual < melhor_custo:
                melhor_custo = custo_atual
                melhor_vizinho = vizinho

        self.qtd_calculo_custo = 0
        return melhor_vizinho, melhor_custo

    def solucao_aleatoria(self):
        'Cria uma solucao inicial com as cidades em um ordem aleatoria'
        cidades = self.cidades
        solucao = [cidades[0]]

        temp = cidades[1:]
        random.shuffle(temp)
        solucao.extend(temp)
       
        return solucao

    def calcula_crossover(self, outro_problema: "Problema") -> "Problema":
        'Realiza o operador de OX Crossover (Order Crossover) entre dois pais'
        tamanho = len(self.solucao)
        filho = [-1] * tamanho  # Inicializa o filho com valores de marcador (-1)

        # Escolhe dois pontos de corte aleatórios
        inicio, fim = sorted(random.sample(range(tamanho), 2))

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
        i, j = random.sample(range(len(self.solucao)), 2)
        self.solucao[i], self.solucao[j] = self.solucao[j], self.solucao[i]
        self.set_solucao(self.solucao)