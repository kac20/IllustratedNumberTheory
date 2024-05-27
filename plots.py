
import plotly.graph_objects as go
from christmastheorem import square_sum_prime


fig = go.Figure()

# compute the primes = sum of 2 squares
square_sum_data = square_sum_prime(500) #data is of the form {prime:(a,b)} where a^2 + b^2 = prime. b>a

x_points,y_points = [], []

# add a circle for each prime
for prime,(a,b)  in square_sum_data.items():
    x_points.append(b)
    y_points.append(a)
    radius = prime **.5
    fig.add_shape(
        type = "circle", xref="x", yref="y",
        x0 = -radius, x1 = radius,
        y0 = -radius, y1 = radius,
        line_color = "LightSeaGreen",
        fillcolor = None,
        layer = "below"
    )

# add markers for each point
fig.add_trace(go.Scatter(x=x_points, y=y_points, mode="markers", marker_color= "black"))
axis_bound = int(max(square_sum_data.keys())**.5) +1


#format the axes
fig.update_xaxes(range = [0, axis_bound], tickmode = 'array',tickvals = list(range(axis_bound)))
fig.update_yaxes(range = [0, axis_bound], tickmode = 'array',tickvals = list(range(axis_bound)))
fig.update_layout(width=800, height=800)
fig.show()