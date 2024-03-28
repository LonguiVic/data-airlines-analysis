from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, HoverTool

def gerar_grafico_vendas_por_produto(vendas_por_produto):
    # Definir a saída do arquivo (opcional)
    output_file("grafico_vendas_por_produto.html")

    # Criar uma fonte de dados a partir do DataFrame
    source = ColumnDataSource(vendas_por_produto)

    # Criar a figura
    p = figure(x_range=vendas_por_produto['produto'], y_range=(0, 2000), width=1000, height=600, title="Total de Vendas por Produto",
               toolbar_location=None, tools="")

    # Adicionar tooltips
    tooltips = [("Produto", "@produto"), ("Total de Vendas", "@valor_total{0,0.00}")]

    # Adicionar barras verticais com tooltips
    p.vbar(x='produto', top='valor_total', width=0.9, source=source, 
           fill_alpha=0.6, line_color="white", legend_label="Produto", hover_fill_alpha=1.0,
           hover_fill_color='orange')

    # Adicionar HoverTool
    hover = HoverTool(tooltips=tooltips)
    p.add_tools(hover)

    # Configurações estéticas
    p.xgrid.grid_line_color = None
    p.yaxis.axis_label = "Total de Vendas"
    p.xaxis.axis_label = "Produto"

    # Mostrar o gráfico
    show(p)