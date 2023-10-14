# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 23:59:18 2023

@author: trevb
"""

from shiny import App, ui, render, reactive
import mandelbrot
#from matplotlib import pyplot as plt
import seaborn as sns

app_ui = ui.page_fluid(
    
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_slider('x',"X Range", value=(-1,1), min=-2, max = 2, step = 0.1),
            ui.input_slider('y',"Y Range", value=(-1,1), min=-2, max = 2, step = 0.1),
            ui.input_slider('depth',"Depth", value=10, min=1, max = 50),
            ui.input_slider('resolution',"Resolution", value=100, min=10, max = 500),
            ui.input_action_button('plot','Plot!'),
        ),
        ui.panel_main(
            ui.output_plot('mandelbrot_plot'),
        ),
    ),    
    
    
    )



def server(input, output, session):
    @output
    @render.plot
    def mandelbrot_plot():
        input.plot()
        with reactive.isolate():
            results, x_label, y_label = mandelbrot.calculate(input.x(),(input.y()[1],input.y()[0]),
                                           input.resolution(),input.depth())
            return sns.heatmap(results.transpose())
    
app = App(app_ui, server)

