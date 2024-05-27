import dash
from dash import html, dcc
from plots import plot

app = dash.Dash(__name__, suppress_callback_exceptions=True)


def layout():
    fig = plot()
    return html.Div([
        dcc.Graph(figure = fig)
    ])

if __name__ == '__main__':
    app.layout = layout()
    app.run(debug=True)
