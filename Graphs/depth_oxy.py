import numpy as np
import csv
import pandas
from six.moves import zip
from bokeh.plotting import *
from bokeh.models import HoverTool, ColumnDataSource
from collections import OrderedDict
df1= pandas.DataFrame.from_csv('/home/pinar/DataSci15-MIT/Graphs/HOTS1.csv')
x = df1.depth
y = df1.oxy
TOOLS="resize,hover, save, crosshair,pan,wheel_zoom,box_zoom,reset,tap,previewsave,box_select,poly_select,lasso_select"
output_file("color_scatter.html", title="color_scatter.py example")
p = figure(tools=TOOLS,title = 'HOTS Chloropigment Concentration vs Temperature', x_axis_label="Temperature",y_axis_label = "Chlorophyl Concentration")
p.scatter(x,y, radius=2, fill_color="#FA5858", fill_alpha=0.6, line_color=None)
p.xaxis.axis_label = "Temperature"
p.yaxis.axis_label = "Chloropigment Concentration"
source = ColumnDataSource(
    data=dict(
        x=x,
        y=y,
        
    )
)
p.plot_width = 600
p.plot_height = 600
# p.rect('x', 'y', 0.9, 0.9, source=source,line_color=None)
hover = p.select(dict(type=HoverTool))
hover.tooltips = OrderedDict([
    ('Temperature', '@x'),
    ('concentration', '@y'),
])

show(p)  # open a browser