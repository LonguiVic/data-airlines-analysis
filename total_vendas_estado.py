from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Category10_10


def plot_vendas_por_estado(vendas_por_estado):
    output_file("vendas_por_estado.html")

    # Ordenar os dados por total de vendas
    vendas_por_estado = vendas_por_estado.sort_values(by='Total de vendas', ascending=False)

    # Criar uma paleta de cores personalizada
    num_cores = len(Category10_10)
    cores_personalizadas = Category10_10 * (len(vendas_por_estado) // num_cores + 1)

    # Adicionar a coluna de cores ao DataFrame
    vendas_por_estado['color'] = cores_personalizadas[:len(vendas_por_estado)]

    # Criar um ColumnDataSource
    source = ColumnDataSource(vendas_por_estado)

    # Criar a figura
    p = figure(y_range=vendas_por_estado['estado'], height=600, width=1000, title="Total de Vendas por Estado",
               toolbar_location=None, tools="")

    # Adicionar barras horizontais
    rects = p.hbar(y='estado', right='Total de vendas', height=0.9, fill_color='color', source=source)

    # Configurações do gráfico
    p.xaxis.axis_label = "Total de Vendas"
    p.outline_line_color = None
    p.ygrid.grid_line_color = None

    # Adicionar hover tool
    hover = HoverTool(renderers=[rects], tooltips=[("Total de Vendas", "@{Total de vendas}{0,0}")])
    p.add_tools(hover)

    show(p)