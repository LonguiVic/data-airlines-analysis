from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool

def plot_sazonalidade_vendas(vendas_por_mes):
    output_file("sazonalidade_vendas.html")
    
    meses_abreviados = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    vendas_por_mes['Mês'] = vendas_por_mes['Mês'].apply(lambda x: meses_abreviados[x-1])

    p = figure(title='Sazonalidade de Vendas por Mês', x_axis_label='Mês', y_axis_label='Total de Vendas', x_range=vendas_por_mes['Mês'], height=600, width=1000)

    p.line(vendas_por_mes['Mês'], vendas_por_mes['valor_total'], line_width=2, color='green')
    p.scatter(vendas_por_mes['Mês'], vendas_por_mes['valor_total'], size=8, color='green', alpha=0.8)

    hover = HoverTool(tooltips=[('Mês', '@x'), ('Total de Vendas', '@y{0.0}')])
    p.add_tools(hover)

    show(p)