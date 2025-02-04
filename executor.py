
import numpy as np
import pandas as pd
from AlgoritmoSolucionador import AlgoritmoSolucionador
import copy
import time
# Cria estruta de dados (DataFrame) para armazenar vários resultados
# diferentes e visualizá-los através de estatísticas

def cria_df(algoritmos : list[AlgoritmoSolucionador], n_vezes) -> pd.DataFrame:

    nomes_algoritmos  = [a.get_short_name() for a in algoritmos]

    n_lin = len(nomes_algoritmos)
    n_col = n_vezes

    df_results = pd.DataFrame(np.zeros((n_lin, n_col)),
                              index=nomes_algoritmos)
    df_results.index.name='ALGORITMO'

    return df_results

# Executa N vezes para gerar estatísticas da variável custo
def executa_n_vezes(algoritmos : list[AlgoritmoSolucionador], n_vezes : int, plot : bool = False, save_df : bool = True ) -> tuple[pd.DataFrame, list]:

    # Cria DataFrame para armazenar os resultados
    df_custos = cria_df(algoritmos, n_vezes)
    df_hit_func_objetivo = cria_df(algoritmos, n_vezes)
    df_tempo = cria_df(algoritmos, n_vezes)

    melhor_solucao_algoritmo : list[tuple] = []

    for algoritmo in algoritmos:
        
        melhor_solucao = None
        melhor_custo = float('inf')
        print(algoritmo.get_name())

        for i in range(n_vezes):
            start = time.time()
            algoritmo.reset() ## Realiza o reset para uma solucao não interferir na proxima

            custo, solucao = algoritmo.run()
            df_custos.loc[algoritmo.get_short_name(),i] = custo
            df_hit_func_objetivo.loc[algoritmo.get_short_name(),i] = algoritmo.quantidade_calculo_custo_acumulado

            print(f'{custo:10.3f}  {solucao}')
            if(custo < melhor_custo):
                melhor_algo_temp_to_plot = copy.deepcopy(algoritmo)
                melhor_custo = custo
                melhor_solucao = solucao
        
            stop = time.time()
            df_tempo.loc[algoritmo.get_short_name(),i] = (stop-start) * 10**3 # ms

        melhor_algo_temp_to_plot.plot(plot)
        melhor_solucao_algoritmo += [(algoritmo.get_short_name(), melhor_custo, melhor_solucao)]

    if(save_df):
        problem_name = algoritmos[0].problema.__class__.__name__
        df_solucao = pd.DataFrame(melhor_solucao_algoritmo,columns=["Algoritmo", "Custo", "Solucao"]).set_index("Algoritmo")
        df_custos.to_csv(f'df_custos_{problem_name}.csv')
        df_solucao.to_csv(f'df_solucao_{problem_name}.csv')
        df_hit_func_objetivo.to_csv(f'df_hit_func_objetivo_{problem_name}.csv')
        df_tempo.to_csv(f'df_tempo_{problem_name}.csv')

    return df_custos, melhor_solucao_algoritmo, df_hit_func_objetivo, df_tempo