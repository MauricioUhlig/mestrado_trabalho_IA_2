import math
import numpy as np

class Problema:
  def __init__(self):
     self.custo : float = 0
     self.solucao: np.ndarray[float] = None
     self.quantidade_calculo_custo:int = 0

     # Guardando valores originais para possibilitar o reset
     self.solucao_original = None
     self.custo_original = None

  def reset(self):
    'Apenas para dar reset na solução, para que todas as execuções iniciem com os mesmos parametros de entrada'
    self.custo = self.custo_original
    self.solucao = self.solucao_original
    self.quantidade_calculo_custo = 0

  def solucao_aleatoria(self):
    'Retorna solução aleatória para o problema'
    pass

  def obtem_melhor_vizinho(self, solucao_atual):
    'Retorna tupla com melhor solução e custo da melhor solução, comparada com a solução atual'
    melhor_custo = float('inf')
    melhor_vizinho = solucao_atual

    for vizinho in self.gera_vizinhos(solucao_atual):
        custo_atual = self.calcula_custo(vizinho)
        
        if custo_atual < melhor_custo:
            melhor_custo = custo_atual
            melhor_vizinho = vizinho

    return melhor_vizinho, melhor_custo

  def calcula_custo(self, solucao_atual):
    'Calcula o custo da solução atual fornecida'
    self.quantidade_calculo_custo += 1

  def gera_vizinhos(self):
    'Gera todos os vizinhos possíveis'
    pass

  def gera_vizinho_aleatorio(self):
    'Gera um vizinho aleatório'
    pass

  def gera_mutacao(self):
    'Gera mutação na solução'
    pass

  def calcula_crossover(self, outro_problema: "Problema") -> "Problema":
    'Realiza o operador de OX Crossover (Order Crossover) entre dois pais'
    pass

  def calcula_probabilidade(self, novo_custo : float, temperatura : float):
    'Calcula a probabilidade de aceitação da solução baseada no custo e temperatura'
    if novo_custo < self.custo: # melhor == menor (<)
        return 1.0
    else:
        escala = self.calcula_escala_temperatura()
        prob = math.exp((self.custo - novo_custo) / (temperatura * escala + 1e-10)) # é somado + 1e-10 para evitar problema da divisao por 0
        # print(f'prob: {prob} - {self.custo - novo_custo}  {temperatura}')
        return prob

  def calcula_escala_temperatura(self):
    l10 = math.log10(self.custo)
    if l10 < 1:
      return 1
    return math.pow(10, l10 -1)
  
  def gera_problema_aleatorio(self, n_elementos : int):
    'Gera problema aleatório com `n_elementos` elementos para testes'
    pass

  def set_solucao(self, solucao : np.ndarray[float], custo : float = None):
    'Atribui a melhor solucao como solucao do problema'
    self.solucao = solucao
    if custo is not None:
      self.custo = custo 
    else:
      self.custo = self.calcula_custo(solucao)
  
  @staticmethod
  def calcula_nova_temperatura(temperatura_atual : float, taxa_resfriamento : float):
    'Realiza o calculo da decrementação da temperatura para cada problema'
    pass