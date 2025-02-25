from AlgoritmoSolucionador import AlgoritmoSolucionador
from Problema import Problema

class HillClimbing(AlgoritmoSolucionador):
  def __init__(self, problema : Problema):
      super().__init__()
      self.problema = problema

  def get_short_name(self) -> str:
    return 'HC'
  
  def run(self):

    # solucao inicial
    solucao_inicial = self.problema.solucao_aleatoria()
    # melhor solucao ate o momento
    solucao_melhor, custo_melhor = self.problema.obtem_melhor_vizinho(solucao_inicial)
    self.problema.set_solucao(solucao_melhor, custo_melhor)
    i = 0

    while True:
        # tenta obter um candidato melhor
        candidato_novo, custo_novo = self.problema.obtem_melhor_vizinho(solucao_melhor)
        #print(custo_melhor, custo_novo)

        self.iteracoes += [i]
        self.custos  += [custo_novo]
        
        if custo_novo < custo_melhor:
            custo_melhor   = custo_novo
            solucao_melhor = candidato_novo
            self.custo_melhor_solucao += [custo_melhor]
            self.problema.set_solucao(solucao_melhor, custo_melhor)
        else:
            self.custo_melhor_solucao += [custo_melhor]
            break   # custo nao melhorou, entao sai do while
        
        i+=1

    self.set_melhor_solucao(solucao_melhor, custo_melhor)
    self.acumula_qtd_calculo_custo(self.problema.quantidade_calculo_custo)
    return custo_melhor, solucao_melhor