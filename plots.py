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
def plota_rotas(df_cidades: pd.DataFrame, ordem_cidades, algoritmo: str = None, custo_total : float = None):
    print(ordem_cidades)
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



def plot_distances(title, iteration_list, distance_list, best_distances):
    trace_current = go.Scatter(x=iteration_list, y=distance_list, mode='lines',
                                line=dict(color='blue', width=2), name='Atual')
    trace_best = go.Scatter(x=iteration_list, y=best_distances, mode='lines',
                             line=dict(color='green', width=2), name='Melhor')

    fig = go.Figure()
    fig.add_trace(trace_current)
    fig.add_trace(trace_best)

    fig.update_layout(
        title=title,
        xaxis_title='Iterações',
        yaxis_title='Custos',
        showlegend=True
    )

    fig.show()

def plot_acceptance_prob(title, iteration_list, accept_p_list):
    colors = ['blue' if p == 1.0 else 'red' for p in accept_p_list]

    trace = go.Scatter(x=iteration_list, y=accept_p_list, mode='markers',
                       marker=dict(color=colors, size=6), name='Probabilidade')

    fig = go.Figure()
    fig.add_trace(trace)

    fig.update_layout(
        title=title,
        xaxis_title='Iterações',
        yaxis_title='Probabilidade',
        yaxis=dict(range=[0, 1.05]),
        showlegend=False
    )
    fig.show()

def plot_temperature(title, iteration_list, temperat_list):
    trace = go.Scatter(x=iteration_list, y=temperat_list, mode='lines',
                       line=dict(color='purple', width=2), name='Temperatura')

    fig = go.Figure()
    fig.add_trace(trace)

    fig.update_layout(
        title=title,
        xaxis_title='Iterações',
        yaxis_title='Temperatura',
        yaxis=dict(range=[0, max(temperat_list)]),
        showlegend=False
    )
    fig.show()
#-----------------------------------------------------
#-----------------------------------------------------

"""### Boxplots"""

# def boxplot_sorted(df, rot=90, figsize=(12,6), fontsize=20):
#     df2 = df.T
#     meds = df2.median().sort_values(ascending=False)
#     axes = df2[meds.index].boxplot(figsize=figsize, rot=rot, fontsize=fontsize,
#                                    boxprops=dict(linewidth=4, color='cornflowerblue'),
#                                    whiskerprops=dict(linewidth=4, color='cornflowerblue'),
#                                    medianprops=dict(linewidth=4, color='firebrick'),
#                                    capprops=dict(linewidth=4, color='cornflowerblue'),
#                                    flierprops=dict(marker='o', markerfacecolor='dimgray',
#                                         markersize=12, markeredgecolor='black'),
#                                    return_type="axes")

#     axes.set_title("Cost of Algorithms", fontsize=fontsize)

# def boxplot_sorted(df, rot=90, figsize=(12, 6), fontsize=20):
#     df2 = df.T
#     meds = df2.median().sort_values(ascending=False)
#     sorted_df = df2[meds.index]

#     fig = go.Figure()

#     for col in sorted_df.columns:
#         fig.add_trace(go.Box(
#             y=sorted_df[col],
#             name=col,
#             boxmean=True,
#             line=dict(width=4, color='cornflowerblue'),
#             whiskerwidth=0.5,
#             marker=dict(color='dimgray', size=12, line=dict(color='black', width=1)),
#             median=dict(line=dict(width=4, color='firebrick'))
#         ))

#     fig.update_layout(
#         title="Cost of Algorithms",
#         title_font_size=fontsize,
#         xaxis=dict(title="Algorithms", tickangle=rot, title_font_size=fontsize),
#         yaxis=dict(title="Values", title_font_size=fontsize),
#         boxmode='group',
#         template="plotly_white",
#         width=figsize[0] * 100,  # Convert figsize to approximate pixels
#         height=figsize[1] * 100
#     )

#     return fig
def boxplot_sorted(df, title,rot=90, figsize=(12,6), fontsize=20):
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

    axes.set_title(title, fontsize=fontsize)
    plt.show()