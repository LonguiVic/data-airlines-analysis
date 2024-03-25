from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, HoverTool

def criar_grafico_top_10_clientes(clientes_lucrativos):
    output_file("top_10_clientes.html")
    fig = figure(title='Top 10 Clientes Mais Lucrativos', x_axis_label='Clientes', y_axis_label='Valor Total das Compras', 
               x_range=clientes_lucrativos.index[:10].astype(str).tolist(), height=600, width=1000)

    source = ColumnDataSource(data=dict(cliente=clientes_lucrativos.index[:10].astype(str), 
                                        valor=clientes_lucrativos['valor_total'][:10],
                                        nome_cliente=clientes_lucrativos['cliente_nome'][:10]))

    fig.scatter(x='cliente', y='valor', size=10, color='skyblue', legend_label='Clientes', source=source)

    hover = HoverTool(tooltips=[('Cliente', '@nome_cliente'), ('Valor Total', '@valor{0.00}')])
    fig.add_tools(hover)

    fig.xaxis.major_label_orientation = 1
    fig.yaxis.formatter.use_scientific = False

    show(fig)