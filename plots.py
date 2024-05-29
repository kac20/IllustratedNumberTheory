
import plotly.graph_objects as go
from sum_of_squares import square_sum_prime, pythag_triples


"""
HELPER FUNCTION
fig - existing go.Figure()
data - a dictionary of the form {c:(a,b)} where a^2 + b^2 = c. b>a
color - color of these circles
name - legend name for these circles

Plots circles of radius c, and points (a,b)
"""
def plot_circles_points(fig, data, color, name):
    x_points,y_points = [], [] #save the points to plot on each circle

    # add a circle for each data point
    for c,(a,b)  in data.items():
        x_points.append(b)
        y_points.append(a)
        radius = c**.5
        fig.add_shape(
            type = "circle", xref="x", yref="y",
            x0 = -radius, x1 = radius,
            y0 = -radius, y1 = radius,
            line_color = color,
            fillcolor = None,
            line_width = .5,
            opacity = .8
        )

    # add markers for each point
    fig.add_trace(go.Scatter(x=x_points, 
                            y=y_points, 
                            customdata = [x**2 + y**2 for (x,y) in zip(x_points,y_points)],
                            mode="markers", 
                            marker_color= color, 
                            name = name,
                            hovertemplate='radius squared = %{customdata}<br>x:%{x}<br>y:%{y}<br>'))

    return fig


"""
########################################
        TIME TO  PLOT THE STUFF
########################################
"""
def plot(max = 100, pythag = True, primes = True, prime_color = "#F1AD3E", pythag_color = "#EF6E10"):
    fig = go.Figure()
    if primes:
        # compute / plot the primes = sum of 2 squares
        square_sum_data = square_sum_prime(max) #data is of the form {prime:(a,b)} where a^2 + b^2 = prime. b>a
        fig = plot_circles_points(fig , square_sum_data, color = prime_color, name = "primes square sums")
    if pythag:
        # compute / plot the pythagorean tripples
        pythag_triples_data = pythag_triples(max)
        fig = plot_circles_points(fig, pythag_triples_data, color =pythag_color, name = "pythag triples")


    # add markers for each point
    axis_bound = int(max**.5)


    #format the plot styling
    axis_style_params = {
        "range":[0, axis_bound],
        "tickmode":"array",
        "tickvals" :list(range(axis_bound)),
        'showticklabels': False,
        "gridcolor": "#FCF7F0",
        "zeroline":False
    }

    fig.update_xaxes(**axis_style_params)
    fig.update_yaxes(**axis_style_params)

    fig.update_layout(
        width = 700,
        height = 700,
        showlegend = False,
        plot_bgcolor = "#F5F0E9", 
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=20, b=20),
        hoverlabel=dict(
                bgcolor="#F5F0E9",
                font_size=10,
                font_family="Futura"
            
    ))

    return fig


#run the plot
# plot().show()