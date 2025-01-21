import random
from typing import List
import copy

from Problema import Problema

class PopulacaoProblema:
  def __init__(self, problema: Problema, tam_populacao : int):
    self.tam_populacao = tam_populacao
    self.problema = problema
    self.populacao : List[Problema] = []

  def gera_populacao(self):
    for _ in range(self.tam_populacao):
        problema_copia = copy.deepcopy(self.problema)
        problema_copia.set_solucao(problema_copia.solucao_aleatoria())
        self.populacao.append(problema_copia)

  def append(self, problema : Problema):
    self.populacao.append(problema)

  def selecao(self) -> Problema:
    """
    Seleciona um indivíduo da população com base no fitness (menor custo é melhor).
    Utiliza o método do torneio simples.
    """
    torneio = random.sample(self.populacao, k=5)  # Seleciona indivíduos aleatórios
    vencedor = min(torneio, key=lambda ind: ind.custo)  # Retorna o de menor custo
    return vencedor
  
  def get_quantidade_calculo_custo(self):
    'Retorna a quantidade total que a populacao acionou a função objetivo'
    return sum(prob.quantidade_calculo_custo for prob in self.populacao)