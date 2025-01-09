"""### Geração de gráficos"""

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from IPython.display import clear_output

"""## Visualização

### Plota Rotas
"""

# Plota a solução do roteamento das cidades
# usando a biblioteca PLOTLY
def plota_rotas(df_cidades: pd.DataFrame, ordem_cidades, algoritmo: str, custo_total : float):
    df_solucao = df_cidades.copy()
    df_solucao = df_solucao.reindex([i + 1 for i in ordem_cidades])

    X = df_solucao['X']
    Y = df_solucao['Y']
    cidades = list(df_solucao.index)

    # cria objeto gráfico
    fig = go.Figure()

    # Atualiza o layout com título, dimensões e legenda
    fig.update_layout(
        autosize=False,
        width=1000,
        height=500,
        showlegend=False,  # Exibe a legenda
        title=f"Rotas Geradas pelo Algoritmo: {algoritmo} | Custo Total: {custo_total:.2f}",  # Título dinâmico
        title_font=dict(size=16),
        title_x=0.5,  # Centraliza o título
    )

    # Adiciona as linhas e pontos para a rota
    fig.add_trace(go.Scatter(
        x=X,
        y=Y,
        text=cidades,
        textposition='bottom center',
        mode='lines+markers+text',
        marker=dict(color='blue', size=8),  # Define a cor e tamanho dos pontos
        line=dict(color='blue', width=2),  # Define a cor e espessura da linha
        name='Rota',  # Nome da linha na legenda
    ))

    # Adiciona linha da última para a primeira cidade para fechar o ciclo
    fig.add_trace(go.Scatter(
        x=X.iloc[[-1, 0]],
        y=Y.iloc[[-1, 0]],
        mode='lines+markers',
        marker=dict(color='red', size=8),  # Pontos com cor diferente
        line=dict(color='red', dash='dot', width=2),  # Linha pontilhada
        name='Fechamento da Rota',  # Nome na legenda
    ))

    # Adiciona os pontos individualmente para destaque
    fig.add_trace(go.Scatter(
        x=X,
        y=Y,
        mode='markers',
        marker=dict(color='green', size=10, symbol='circle'),  # Pontos em verde
        name='Cidades',  # Nome dos pontos na legenda
    ))

    fig.show()



def plot_path(cities_xy, cities_path, ax):

    # Reeordena as cidades pela ordem do caminho
    cities = cities_xy[cities_path]

    # Repete a primeira cidade para fechar o ciclo
    x = cities[:,0]
    y = cities[:,1]

    # Personalização do gráfico
    ax.set_xlabel('X (Longitude)')
    ax.set_ylabel('Y (Latitude)')
    ax.set_title('Caminho')
    

    # Plotagem das coordenadas interligadas com pontos vermelhos e linhas azuis
    ax.plot(x, y, color='blue', linestyle='-', linewidth=2)
    ax.plot(x, y, color='red', marker='o', markersize=8, linestyle='')
    ax.plot(x[[-1,0]], y[[-1,0]], color='orange', linestyle='-', linewidth=2)

def plot_distances(iteration_list, distance_list, best_distances, ax):

    x  = iteration_list
    y1 = distance_list
    y2 = best_distances

    # Personalização do gráfico
    ax.set_xlabel('Iterações')
    ax.set_ylabel('Distâncias (custos)')
    ax.set_title('Comprimento Total do caminho')

    ax.plot(x,y1, label='Atual')
    ax.plot(x,y2, label='Melhor')
    ax.legend()

def plot_acceptance_prob(iteration_list, accept_p_list, ax):

    x = iteration_list
    y = accept_p_list

    # Personalização do gráfico
    ax.set_xlabel('Iterações')
    ax.set_ylabel('Probabilidade')
    ax.set_title('Probabilidade de Aceitação')

    ax.set_ylim([0, 1.05])

    # Criar uma nova lista de cores com base nos valores de y
    xc, yc, colors = zip(*[(xi, yi, 'b') if yi==1.0 else (xi, yi, 'r') \
                           for xi, yi in enumerate(y)])

    ax.scatter(xc, yc, c=colors, s=2)

def plot_temperature(iteration_list, temperat_list, ax):

    x = iteration_list
    y = temperat_list

    # Personalização do gráfico
    ax.set_xlabel('Iterações')
    ax.set_ylabel('Temperatura')
    ax.set_title('Decaimento da Temperatura')

    ax.set_ylim([0, max(y)])

    ax.plot(x,y)

#----------------------------------------------------------------

def plot_axes_figure_sa(cities_xy, cities_path, iteration_list,
                     distance_list, best_distances,
                     accept_p_list, temperat_list):

    x = iteration_list
    y1 = distance_list
    y2 = best_distances
    y3 = accept_p_list
    y4 = temperat_list

    clear_output(wait=True)

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12,8))

    plot_path(cities_xy, cities_path, ax1)
    plot_distances      (x, y1, y2, ax2)
    plot_acceptance_prob(x, y3, ax3)
    plot_temperature    (x, y4, ax4)

    # Ajusta o espaçamento entre os subgráficos
    fig.tight_layout()

    plt.pause(0.001)

def plot_axes_figure_ga(cities_xy, cities_path, iteration_list,
                     distance_list, best_distances):

    x = iteration_list
    y1 = distance_list
    y2 = best_distances

    clear_output(wait=True)

    fig, ((ax1, ax2)) = plt.subplots(1, 2, figsize=(12,4))

    plot_path(cities_xy, cities_path, ax1)
    plot_distances      (x, y1, y2, ax2)

    # Ajusta o espaçamento entre os subgráficos
    fig.tight_layout()

    plt.pause(0.001)

#-----------------------------------------------------
#-----------------------------------------------------

"""### Boxplots"""

def boxplot_sorted(df, rot=90, figsize=(12,6), fontsize=20):
    df2 = df.T
    meds = df2.median().sort_values(ascending=False)
    axes = df2[meds.index].boxplot(figsize=figsize, rot=rot, fontsize=fontsize,
                                   boxprops=dict(linewidth=4, color='cornflowerblue'),
                                   whiskerprops=dict(linewidth=4, color='cornflowerblue'),
                                   medianprops=dict(linewidth=4, color='firebrick'),
                                   capprops=dict(linewidth=4, color='cornflowerblue'),
                                   flierprops=dict(marker='o', markerfacecolor='dimgray',
                                        markersize=12, markeredgecolor='black'),
                                   return_type="axes")

    axes.set_title("Cost of Algorithms", fontsize=fontsize)