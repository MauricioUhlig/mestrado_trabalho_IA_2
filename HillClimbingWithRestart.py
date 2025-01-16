from AlgoritmoSolucionador import AlgoritmoSolucionador
from Problema import Problema
from HillClimbing import HillClimbing

from tqdm import tqdm

class HillClimbingWithRestart(AlgoritmoSolucionador):
  def __init__(self, problema : Problema, n_execucoes : int):
      super().__init__()
      self.problema = problema
      self.n_execucoes = n_execucoes

  def run(self):
    custo_melhor = None
    with tqdm(total=self.n_execucoes, colour='blue',
              desc='Iter: 0 - Cost: NaN') as pbar:

      for i in range(self.n_execucoes):
        temp = HillClimbing(self.problema)
        custo_atual, solucao_atual = temp.run()


        if custo_melhor == None or custo_atual < custo_melhor:
          custo_melhor = custo_atual
          solucao_melhor = solucao_atual
          self.problema.set_solucao(solucao_melhor)

        pbar.set_description(f'Iter: {i+1} - Cost: {custo_melhor:7.3f}')
        pbar.update(1)

    return custo_melhor, solucao_melhor