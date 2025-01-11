from Problema import Problema
class AlgoritmoSolucionador:
  def __init__(self):
    self.problema : Problema = None

  def run(self) -> list:
    'Executa a solucao do algoritmo'
    pass
  def get_name(self) -> str:
    'Retorna o nome do algoritmo'
    return self.__class__.__name__
  
  def reset(self):
    'Realiza o reset para o original parametrizado em algoritmos que mudam algum parametro durante a execução'
    self.problema.reset()