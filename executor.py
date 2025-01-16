
import numpy as np
import pandas as pd
from Problema import Problema
from AlgoritmoSolucionador import AlgoritmoSolucionador
import copy
# Cria estruta de dados (DataFrame) para armazenar vários resultados
# diferentes e visualizá-los através de estatísticas

def cria_df_custos(algoritmos : list[AlgoritmoSolucionador], n_vezes) -> pd.DataFrame:

    nomes_algoritmos  = [a.get_name() for a in algoritmos]

    n_lin = len(nomes_algoritmos)
    n_col = n_vezes

    df_results = pd.DataFrame(np.zeros((n_lin, n_col)),
                              index=nomes_algoritmos)
    df_results.index.name='ALGORITMO'

    return df_results

# Executa N vezes para gerar estatísticas da variável custo
def executa_n_vezes(algoritmos : list[AlgoritmoSolucionador], n_vezes) -> tuple[pd.DataFrame, list]:

    # Cria DataFrame para armazenar os resultados
    df_custo = cria_df_custos(algoritmos, n_vezes)

    melhor_solucao_algoritmo : list[tuple] = []

    for algoritmo in algoritmos:
        
        melhor_solucao = None
        melhor_custo = float('inf')
        print(algoritmo.get_name())

        for i in range(n_vezes):
            algoritmo.reset() ## Realiza o reset para uma solucao não interferir na proxima

            custo, solucao = algoritmo.run()
            df_custo.loc[algoritmo.get_name(),i] = custo

            print(f'{custo:10.3f}  {solucao}')
            if(custo < melhor_custo):
                melhor_algo_temp_to_plot = copy.deepcopy(algoritmo)
                melhor_custo = custo
                melhor_solucao = solucao

        melhor_algo_temp_to_plot.plot()
        melhor_solucao_algoritmo += [(algoritmo.get_name(), melhor_custo, melhor_solucao)]
    return df_custo, melhor_solucao_algoritmo