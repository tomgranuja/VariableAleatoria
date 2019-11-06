#!/usr/bin/env python3
#-*- coding:utf-8 -*-


from bokeh.plotting import figure
from bokeh.models import SingleIntervalTicker, Arrow, OpenHead

class Plot():
    def __init__(self, dim=(800,400),
               prange={'x':(-12,12),'y':(-6,6)},
               grid=1, mticks=1,
               police_at=(0,0), cross_at=(1,0), 
               title='Movimiento en el mapa.'):
        self.pl = figure(width=dim[0], height=dim[1],
                         x_range=prange['x'], y_range=prange['y'],
                         title=title)
        ticker = SingleIntervalTicker(interval=grid, num_minor_ticks=mticks)
        self.pl.axis.ticker = ticker
        self.pl.grid.ticker = ticker
        self.pl.xaxis.major_label_text_font_size = '14px'
        self.pl.yaxis.major_label_text_font_size = '14px'
        self.cross(x=cross_at[0], y=cross_at[1])
        self.police(x=police_at[0], y=police_at[1])
        
    def cross(self, x=0, y=0):
        self.pl.cross(x=[x], y=[y],
                      size=20, line_width=2, color='red')
    
    def police(self, x=0, y=0):
        self.pl.image_url(url=['comisaria.svg'],
                          x=[x], y=[y] ,
                          w=[0.75], h=[0.75], anchor='center')
    
    def trace(self, points, color='cornflowerblue',
              lw=3, la=0.8, arrow_size=15):
        x, y = points.T
        end = OpenHead(line_color=color, size=arrow_size,
                       line_width=lw, line_alpha=la)
        self.pl.line(x=x, y=y, color=color, line_width=lw, line_alpha=la)
        self.pl.add_layout(Arrow(end=end,
                                 x_start=x[-2],y_start=y[-2],
                                 x_end=x[-1], y_end=y[-1],
                                 line_color=color, line_width=lw, 
                                 line_alpha=0))
        
        

def ag_plot(ag, dim=(800,400)):
    p = figure(width=dim[0], height=dim[1],
               title='Distribución de la distancia en cuadras')
    ticker = SingleIntervalTicker(interval=2, num_minor_ticks=2)
    p.xaxis.ticker = ticker
    p.xgrid.ticker = ticker
    p.xaxis.axis_label = 'Distancia a la comisaría en cuadras'
    p.yaxis.axis_label = 'Número de maneras posibles'
    p.xaxis.major_label_text_font_size = '14px'
    p.yaxis.major_label_text_font_size = '14px'
    p.vbar(x=ag.cuadras, width=0.01, bottom=0, 
           top=ag['caminos posibles'], color="firebrick")
    return p

    

if __name__ == '__main__':
    pass
