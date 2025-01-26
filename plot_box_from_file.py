import pandas as pd
import plots

dados = [
            ['df_custos_tsp.csv','Custo dos algorítmos'],
            ['df_hit_func_objetivo_tsp.csv','Quantidade de acessos na função objetivo'],
            ['df_tempo_tsp.csv','Tempo de execução (ms)'],
            ['df_custos_rastrigin.csv','Custo dos algorítmos'],
            ['df_hit_func_objetivo_rastrigin.csv','Quantidade de acessos na função objetivo'],
            ['df_tempo_rastrigin.csv','Tempo de execução (ms)'],
        ]

for file, title in dados:
    df = pd.read_csv(file, index_col='ALGORITMO')
    plots.boxplot_sorted(df,title)
