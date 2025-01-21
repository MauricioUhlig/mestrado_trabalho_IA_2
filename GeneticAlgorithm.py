from AlgoritmoSolucionador import AlgoritmoSolucionador
from Problema import Problema
from PopulacaoProblema import PopulacaoProblema
import random
import plots

class GeneticAlgorithm(AlgoritmoSolucionador):
    def __init__(self, problema: Problema, tamanho_populacao: int = 20, n_geracoes: int = 100, taxa_mutacao: float = 0.1):
        super().__init__()
        self.problema = problema
        self.tamanho_populacao = tamanho_populacao
        self.n_geracoes = n_geracoes
        self.taxa_mutacao = taxa_mutacao

    def mutacao(self, individuo: Problema):
        """
        Realiza mutação no indivíduo, trocando dois genes de posição aleatoriamente.
        """
        if random.random() < self.taxa_mutacao:
            individuo.gera_mutacao()



    def run(self):
        # Gera a população inicial
        populacao = PopulacaoProblema(self.problema, self.tamanho_populacao)
        populacao.gera_populacao()
        self.acumula_qtd_calculo_custo(populacao.get_quantidade_calculo_custo())

        # with tqdm(total=self.n_geracoes, colour='blue',
        #       desc=f'Iter: 0 - Cost: NaN') as pbar:
        # Executa as gerações
        for geracao in range(self.n_geracoes):
            nova_populacao = PopulacaoProblema(self.problema, self.tamanho_populacao)

            for i in range(self.tamanho_populacao // 2):
                # Seleção
                p1 = populacao.selecao()
                p2 = populacao.selecao()

                # Crossover
                filho1 = p1.calcula_crossover(p2)
                filho2 = p2.calcula_crossover(p1)

                #print(f'crossover \npais:[\n{p1.solucao}, \n{p2.solucao}]\nfilhos:[\n{filho1.solucao},\n{filho2.solucao}]')

                # Mutação
                self.mutacao(filho1)
                self.mutacao(filho2)

                # Adiciona os filhos à nova população
                nova_populacao.append(filho1)
                nova_populacao.append(filho2)

            # Atualiza a população com a nova geração
            populacao = nova_populacao
            self.acumula_qtd_calculo_custo(populacao.get_quantidade_calculo_custo())
            
            # Calcula os custos da nova população
            melhor_custo = min(populacao.populacao, key=lambda ind: ind.custo)
            # pbar.set_description(f'Iter: {geracao+1} Cost: {melhor_custo.custo:7.3f}')
            # pbar.update(1)

            # Implementacao para visualizacao apenas
            self.iteracoes += [geracao]
            self.custos  += [melhor_custo.custo]
            self.custo_melhor_solucao += [min(self.custos)]

            # if (geracao+1) % 10 == 0:
        # plots.plot_axes_figure_ga(melhor_custo.coordenadas.to_numpy(), melhor_custo.solucao, iteration_list,
        #                 distance_list, best_distances)

        # Retorna o melhor indivíduo
        melhor_individuo = min(populacao.populacao, key=lambda ind: ind.custo)
        self.set_melhor_solucao(melhor_individuo.solucao, melhor_individuo.custo)
        return melhor_individuo.custo, melhor_individuo.solucao
