import dash
from dash import html, dcc
from plots import plot
import dash_daq as daq
import callbacks

app = dash.Dash(__name__, suppress_callback_exceptions=True)


def layout():
    fig = plot()
    return html.Div([
        dcc.Graph(figure = fig, className = "plot", id = "plot"),
        
        html.Div([
            dcc.Checklist(options = ["Fermat's Prime Squares", "Pythagorean Triples"], id = "display_options", value = ["Fermat's Prime Squares", "Pythagorean Triples"], className = "checklist"),
            dcc.Input(id = "max", value = 100, debounce = True, className = "text-field"),
            daq.ColorPicker(
                id = "prime_color",
                label = "Prime Color",
                value = dict(hex='#F1AD3E')
            ),

            daq.ColorPicker(
                id = "pythag_color",
                label = "Pythagorean Triple Color",
                value = dict(hex='#EF6E10')

            )
        ], className = "params-container")
        
    ], className = "layout")




if __name__ == '__main__':
    app.layout = layout()
    app.run(debug=True)
