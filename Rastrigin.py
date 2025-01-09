from Problema import Problema

import random
import math

class Rastrigin(Problema):
  def __init__(self, intervalo_min : float = -5.12, intervalo_max : float = 5.12):
    self.intervalo_min = intervalo_min
    self.intervalo_max = intervalo_max
    self.solucao = self.solucao_aleatoria()
    self.custo = self.calcula_custo()
    self.solucao_original = self.solucao
    self.custo_original = self.custo

  def solucao_aleatoria(self):
     return [random.randrange(self.intervalo_min, self.intervalo_max)]

  def calcula_custo(self, solucao_atual):
     return 20 + solucao_atual[0]**2 - 10 * math.cos(2 * math.pi * solucao_atual[0]) + solucao_atual[1]**2 - 10 * math.cos(2 * math.pi * solucao_atual[1])

