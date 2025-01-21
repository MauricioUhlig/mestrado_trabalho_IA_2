import numpy as np
import plots
from Problema import Problema
class AlgoritmoSolucionador:
  def __init__(self):
    self.problema : Problema = None
    self.custos: list[float] = []
    self.custo_melhor_solucao: list[float] = []
    self.iteracoes: list[int] = []
    self.temperaturas: list[float] = []
    self.probabilidades: list[float] = []
    self.melhor_solucao: np.ndarray[float] = None
    self.melhor_custo: float = None
    self.quantidade_calculo_custo_acumulado:int = 0

  def run(self) -> list:
    'Executa a solucao do algoritmo'
    pass
  def get_name(self) -> str:
    'Retorna o nome do algoritmo'
    return self.__class__.__name__
  
  def acumula_qtd_calculo_custo(self, qtd_calculo_custo:int):
    self.quantidade_calculo_custo_acumulado += qtd_calculo_custo

  def reset(self):
    'Realiza o reset para o original parametrizado em algoritmos que mudam algum parametro durante a execução'
    self.problema.reset()
    self.custos: list[float] = []
    self.custo_melhor_solucao: list[float] = []
    self.iteracoes: list[int] = []
    self.melhor_solucao: np.ndarray[float] = None
    self.melhor_custo: float = None
    self.temperaturas: list[float] = []
    self.quantidade_calculo_custo_acumulado:int = 0

  def set_melhor_solucao(self, solucao: np.ndarray[float], custo: float):
    self.melhor_solucao = solucao
    self.melhor_custo = custo

  def plot(self): 
    'Gera imagnes a partir dos metadados da execucao'
    print(f'\nQuantidade total de hits na funcao objetivo do algoritmo {self.get_name()}: {self.quantidade_calculo_custo_acumulado:_}\n')
    if self.problema.__class__.__name__ == "TSP":
      plots.plota_rotas(self.problema.coordenadas, self.melhor_solucao, self.get_name(), self.melhor_custo)

    elif self.problema.__class__.__name__ == "Rastrigin":
      # plots.plota_rotas(self.problema.coordenadas, self.melhor_solucao)
      print("Nao implementado ainda")

    else: 
      raise Exception(f'Plot não implementado para o problema {self.problema.__class__.__name__}')
    
    if self.iteracoes != []:
      plots.plot_distances(f'Evolução dos custos do algoritmo {self.get_name()}',self.iteracoes, self.custos, self.custo_melhor_solucao)
    
    if self.temperaturas != []:
      plots.plot_temperature(f'Decaimento da temperatura do algoritmo {self.get_name()}',self.iteracoes,self.temperaturas)
      
    if self.probabilidades != []:
      plots.plot_acceptance_prob(f'Probabilidade de aceitação do algoritmo {self.get_name()}',self.iteracoes,self.probabilidades)

    print(f'\n\nCUSTO: {self.melhor_custo} SOLUCAO: {self.melhor_solucao}\n\n')