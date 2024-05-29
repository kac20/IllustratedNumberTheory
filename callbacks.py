from dash import callback, Input, Output, State, Patch, no_update
from plots import plot

@callback(
    Output("plot", "figure"),
    Input("display_options", "value"),
    Input("max", "value"),
    Input("prime_color", "value"),
    Input("pythag_color", "value")
)
def set_display(selection, max, color1, color2):
    if selection == None or max == None or color1 == None or color2 == None:
        return no_update

    try:  #check that max is an int
        max = int(max)
    except:
        return no_update

    return plot(max = max, 
            pythag = "Pythagorean Triples" in selection, 
            primes = "Fermat's Prime Squares" in selection,
            prime_color = color1["hex"],
            pythag_color = color2["hex"])
    
