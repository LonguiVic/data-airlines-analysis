# Importando as bibliotecas necessárias
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, HoverTool

def gerar_grafico_vendas_por_produto(dataframe):
    # Agrupando os dados por produto e somando as vendas
    vendas_por_produto = dataframe.groupby('produto')['valor_total'].sum().reset_index()

    # Criando uma fonte de dados para o Bokeh
    source = ColumnDataSource(vendas_por_produto)

    # Criando a figura
    p = figure(x_range=vendas_por_produto['produto'], height=600, width=1000, title="Vendas por Produto",
               toolbar_location=None, tools="")

    # Adicionando as barras do gráfico
    p.vbar(x='produto', top='valor_total', width=0.9, source=source)

    # Configurando os rótulos
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.xaxis.axis_label = "Produto"
    p.yaxis.axis_label = "Total de Vendas"

    # Adicionando tooltips
    tooltips = [("Produto", "@produto"), ("Total de Vendas", "@valor_total{$0.00}")]
    p.add_tools(HoverTool(tooltips=tooltips))

    # Exibindo o gráfico no navegador
    show(p)