import math

class Problema:
  def __init__(self):
     self.custo : float = 0
     self.solucao = None

     # Guardando valores originais para possibilitar o reset
     self.solucao_original = None
     self.custo_original = None

  def reset(self):
    'Apenas para dar reset na solução, para que todas as execuções iniciem com os mesmos parametros de entrada'
    self.custo = self.custo_original
    self.solucao = self.solucao_original

  def solucao_aleatoria(self):
    'Retorna solução aleatória para o problema'
    pass

  def obtem_melhor_vizinho(self, solucao_atual):
    'Retorna tupla com melhor solução e custo da melhor solução, comparada com a solução atual'
    pass

  def calcula_custo(self, solucao_atual):
    'Calcula o custo da solução atual fornecida'
    pass

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
        return math.exp((self.custo - novo_custo) / temperatura)

  def gera_problema_aleatorio(self, n_elementos : int):
    'Gera problema aleatório com `n_elementos` elementos para testes'
    pass

  def set_solucao(self, solucao):
    'Atribui a melhor solucao como solucao do problema'
    self.solucao = solucao
    self.custo = self.calcula_custo(solucao)