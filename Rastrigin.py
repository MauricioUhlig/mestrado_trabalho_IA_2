from Problema import Problema

import numpy as np
import copy

class Rastrigin(Problema):
  def __init__(self, limite_inferior : float = -5.12, limite_superior : float = 5.12, std_passo : float = 0.2):
    super().__init__()
    self.limite_inferior = limite_inferior
    self.limite_superior = limite_superior
    self.std_passo = std_passo
    self.solucao = self.solucao_aleatoria()
    self.custo = self.calcula_custo(self.solucao)
    self.solucao_original = self.solucao
    self.custo_original = self.custo

  def solucao_aleatoria(self) -> np.ndarray[float]:
     return np.random.uniform(self.limite_inferior, self.limite_superior, size=2).tolist()

  def calcula_custo(self, solucao_atual) -> float:
    super().calcula_custo(solucao_atual)
    return 20 + solucao_atual[0]**2 - 10 * np.cos(2 * np.pi * solucao_atual[0]) + solucao_atual[1]**2 - 10 * np.cos(2 * np.pi * solucao_atual[1])

  def gera_vizinhos(self, solucao: np.ndarray[float])-> list[np.ndarray[float]]:
      solucao = self.gera_movimento_aleatorio_valido(solucao)
      return [solucao]

  def gera_vizinho_aleatorio(self)-> np.ndarray[float]:
     return self.gera_movimento_aleatorio_valido(self.solucao)
  
  def gera_mutacao(self)-> np.ndarray[float]:
    novo = self.gera_movimento_aleatorio_valido(self.solucao)
    self.set_solucao(novo)

  def calcula_crossover(self, outro_problema: Problema) -> Problema: #tuple[Problema, Problema]:
    p1 = np.array(self.solucao)
    p2 = np.array(outro_problema.solucao)

    alpha = np.random.rand()
    c1 = p1*alpha + p2*(1-alpha)
    cp = copy.deepcopy(self)

    cp.set_solucao(c1.tolist())

    return cp
  ## ---------------------------------------------------------
  def gera_passo_aleatorio(self) -> float:
    return float(np.random.randn(1)[0])*self.std_passo
  
  def gera_movimento_aleatorio_valido(self, solucao : np.ndarray[float]):
    vizinho = solucao.copy()

    for i in range(2):
      valido = False
      while valido is False:
        valor = self.gera_passo_aleatorio()
        v = vizinho[i] + valor#self.gera_passo_aleatorio()
        
        # Verifica se o vizinho está dentro dos limites
        if self.limite_inferior <= v <= self.limite_superior:
          vizinho[i] = v
          valido = True

    return vizinho
  
  @staticmethod
  def calcula_nova_temperatura(temperatura_atual : float, taxa_resfriamento : float):
    return max(0, temperatura_atual - taxa_resfriamento)
            