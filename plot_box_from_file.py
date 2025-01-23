import pandas as pd
import plots

df = pd.read_csv('df_custos_tsp.csv', index_col='ALGORITMO')



plots.boxplot_sorted(df)

df = pd.read_csv('df_custos_rastrigin.csv', index_col='ALGORITMO')



plots.boxplot_sorted(df)

