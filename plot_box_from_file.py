import pandas as pd
import plots

df = pd.read_csv('df_hit_func_objetivo_tsp.csv', index_col='ALGORITMO')



plots.boxplot_sorted(df,"Quantidade de acessos na função objetivo")

df = pd.read_csv('df_hit_func_objetivo_rastrigin.csv', index_col='ALGORITMO')



plots.boxplot_sorted(df,"Quantidade de acessos na função objetivo")

