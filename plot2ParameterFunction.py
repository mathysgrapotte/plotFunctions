import plotly
import plotly.graph_objs as go
import numpy as np
import pandas as pd

# This functions builds a surface plot of a function of two variables using plotly
# The function is defined by the user

# Plotting functions that take as argument a function of two variables and the range of the function with a granualrity parameter
def plot2ParameterFunction(f, x_range, y_range, granularity=50, jupyter=False):
    # creating a meshgrid
    x_values = np.linspace(x_range[0], x_range[1], granularity)
    y_values = np.linspace(y_range[0], y_range[1], granularity)
    x,y = np.meshgrid(x_values, y_values)
    # defining the function
    z = f(x, y)

    # creating the surface plot
    data = [go.Surface(z=z, x=x, y=y)]

    # defining the layout
    layout = go.Layout(title='Surface plot of a function of two variables',
                       autosize=False,
                       width=800,
                       height=800,
                       margin=dict(l=65, r=50, b=65, t=90))

    # creating the figure
    fig = go.Figure(data=data, layout=layout)  
    # plotting the figure
    if jupyter:
        plotly.offline.iplot(fig)
    else:
        plotly.offline.plot(fig, filename='plot2ParameterFunction.html')

# testing the function
if __name__ == '__main__':
    # defining the function
    f = lambda x, y: x**2 + y**2
    # defining the range of the function
    x_range = [-10, 10]
    y_range = [-10, 10]
    # plotting the function
    plot2ParameterFunction(f, x_range, y_range)


