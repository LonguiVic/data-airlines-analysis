from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap

def criar_grafico_contagem_clientes_estado(data):
    # Definir a saída do arquivo (opcional)
    output_file("grafico_clientes_por_estado.html")

    # Criar uma fonte de dados a partir do DataFrame
    source = ColumnDataSource(data)

    # Definir uma paleta de cores personalizada com 24 cores
    paleta_cores = [
        "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b",
        "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", "#aec7e8", "#ffbb78",
        "#98df8a", "#ff9896", "#c5b0d5", "#c49c94", "#f7b6d2", "#c7c7c7",
        "#dbdb8d", "#9edae5", "#ad494a", "#8c6d31", "#7b4173", "#a55194"
    ]

    # Criar a figura
    p = figure(x_range=data['estado'], width = 1000, height=600, title="Contagem de Clientes por Estado",
               toolbar_location=None, tools="")

    # Adicionar barras verticais com cores específicas para cada estado
    p.vbar(x='estado', top='Quantidade de Clientes', width=0.9, source=source, 
           line_color='white', fill_color=factor_cmap('estado', palette=paleta_cores, factors=data['estado']))

    # Configurações estéticas
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.yaxis.axis_label = "Quantidade de Clientes"
    p.xaxis.axis_label = "Estado"
    p.xaxis.major_label_orientation = 1.2

    # Mostrar o gráfico
    show(p)