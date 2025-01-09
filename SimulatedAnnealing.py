from AlgoritmoSolucionador import AlgoritmoSolucionador
from Problema import Problema
import plots
import random

class SimulatedAnnealing(AlgoritmoSolucionador):
  def __init__(self, problema : Problema, n_iter : int, n_rep : int, initial_temperature : float = 1000, cooling_rate : float = 0.2):
    self.n_iter = n_iter
    self.n_rep = n_rep
    self.problema = problema
    self.cooling_rate = cooling_rate
    self.initial_temperature = initial_temperature

  def run(self):
    best_route = self.problema.solucao
    best_distance = self.problema.custo
    temperature = self.initial_temperature

    #-----------------------------------------------
    iteration_list = []
    best_distances = []
    distance_list  = []
    accept_p_list  = []
    temperat_list  = []
    #-----------------------------------------------

    # with tqdm(total=self.n_iter*self.n_rep, colour='blue',
    #           desc=f'Iter: 0 - Cost: NaN - Temperature: {temperature:3.5f} - Best: {best_distance:7.3f}') as pbar:

    for iteration in range(self.n_iter):
        # numero de vizinhos a serem gerados e testados para cada iteração
        for i in range(self.n_rep):

            new_route = self.problema.gera_vizinho_aleatorio()
            new_distance = self.problema.calcula_custo(new_route)

            acceptance_prob = self.problema.calcula_probabilidade(new_distance, temperature)

            if random.random() < acceptance_prob:
                self.problema.set_solucao(new_route)

            # pbar.set_description(f'Iter: {iteration*self.n_rep+i+1} - Cost: {self.problema.custo:7.3f} - Temperature: {temperature:3.5f} - Best: {best_distance:7.3f}')
            # pbar.update(1)

        temperature *= self.cooling_rate


        #-----------------------------------------------
        if new_distance < best_distance:
            best_route = new_route
            best_distance = new_distance

      # Implementacao para visualizacao apenas
        iteration_list += [iteration]
        best_distances += [best_distance]
        distance_list  += [self.problema.custo]
        accept_p_list  += [acceptance_prob]
        temperat_list  += [temperature]

        # if iteration % 50 == 0:
        #   plot_axes_figure_sa(self.problema.coordenadas.to_numpy(), self.problema.solucao, iteration_list,
        #                   distance_list, best_distances,
        #                   accept_p_list, temperat_list)
      #-----------------------------------------------

    # plt.show()

    plots.plot_axes_figure_sa(self.problema.coordenadas.to_numpy(), self.problema.solucao, iteration_list,
                    distance_list, best_distances,
                    accept_p_list, temperat_list)

    return best_distance, best_route