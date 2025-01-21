from AlgoritmoSolucionador import AlgoritmoSolucionador
from Problema import Problema
import plots
import random
from tqdm import tqdm
class SimulatedAnnealing(AlgoritmoSolucionador):
  def __init__(self, problema : Problema, n_iter : int, n_rep : int, initial_temperature : float = 1000, cooling_rate : float = 0.997):
    super().__init__()
    self.n_iter = n_iter
    self.n_rep = n_rep
    self.problema = problema
    self.cooling_rate = cooling_rate
    self.initial_temperature = initial_temperature

    self.original_initial_temperature = initial_temperature

  def reset(self):
     self.initial_temperature = self.original_initial_temperature
     return super().reset()
  
  def passo_log(self):
     return self.n_iter / 100 # 1%

  def run(self):
    best_route = self.problema.solucao
    best_distance = self.problema.custo
    temperature = self.initial_temperature
    passo = self.passo_log()

    with tqdm(total=self.n_iter, colour='blue',
              desc=f'Iter: 0 - Cost: NaN - Temperature: {temperature:3.5f} - Best: {best_distance:7.3f}') as pbar:

      for iteration in range(self.n_iter):
          # numero de vizinhos a serem gerados e testados para cada iteração
          for i in range(self.n_rep):

              new_route = self.problema.gera_vizinho_aleatorio()
              new_distance = self.problema.calcula_custo(new_route)

              acceptance_prob = self.problema.calcula_probabilidade(new_distance, temperature)

              if random.random() < acceptance_prob:
                  self.problema.set_solucao(new_route, new_distance)
          if (iteration+1) % passo == 0:
            pbar.set_description(f'Iter: {iteration+1} - Cost: {self.problema.custo:7.3f} - Temperature: {temperature:3.5f} - Best: {best_distance:7.3f}')
            pbar.update(passo)

          temperature = self.problema.calcula_nova_temperatura(temperature, self.cooling_rate)


          #-----------------------------------------------
          if new_distance < best_distance:
              best_route = new_route
              best_distance = new_distance
              self.set_melhor_solucao(best_route, best_distance)

        # Implementacao para visualizacao apenas
          self.iteracoes += [iteration]
          self.custos  += [self.problema.custo]
          self.custo_melhor_solucao += [best_distance]
          self.probabilidades  += [acceptance_prob]
          self.temperaturas  += [temperature]


          # if iteration % 50 == 0:
          #   plot_axes_figure_sa(self.problema.coordenadas.to_numpy(), self.problema.solucao, iteration_list,
          #                   distance_list, best_distances,
          #                   accept_p_list, temperat_list)
        #-----------------------------------------------

    # plt.show()

    # plots.plot_axes_figure_sa(self.problema.coordenadas.to_numpy(), self.problema.solucao, iteration_list,
    #                 distance_list, best_distances,
    #                 accept_p_list, temperat_list)

    self.acumula_qtd_calculo_custo(self.problema.quantidade_calculo_custo)
    return best_distance, best_route