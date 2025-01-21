from AlgoritmoSolucionador import AlgoritmoSolucionador
from Problema import Problema
from HillClimbing import HillClimbing
import copy

from tqdm import tqdm

class HillClimbingWithRestart(AlgoritmoSolucionador):
  def __init__(self, problema : Problema, n_execucoes : int):
      super().__init__()
      self.problema = problema
      self.n_execucoes = n_execucoes

  
  def passo_log(self):
     return 1 if self.n_execucoes <= 1000 else self.n_execucoes / 100 # 1%
  
  def run(self):
    custo_melhor = None
    passo = self.passo_log()
    with tqdm(total=self.n_execucoes, colour='blue',
              desc='Iter: 0 - Cost: NaN') as pbar:

      for i in range(self.n_execucoes):
        temp = HillClimbing(copy.deepcopy(self.problema))
        custo_atual, solucao_atual = temp.run()
        self.acumula_qtd_calculo_custo(temp.quantidade_calculo_custo_acumulado)


        if custo_melhor == None or custo_atual < custo_melhor:
          custo_melhor = custo_atual
          solucao_melhor = solucao_atual
          self.problema.set_solucao(solucao_melhor, custo_atual)
        if (i+1) % passo == 0:
          pbar.set_description(f'Iter: {i+1} - Cost: {custo_melhor:7.3f}')
          pbar.update(passo)
      
        self.iteracoes += [i]
        self.custos  += [custo_atual]
        self.custo_melhor_solucao += [custo_melhor]
    
    self.set_melhor_solucao(solucao_melhor, custo_melhor)
    return custo_melhor, solucao_melhor