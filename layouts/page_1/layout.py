from dash import dcc, html


def layout_1():
    value = "length"

    layout = [
        html.H3("Write the text below"),
        dcc.Input(
            id="search-input",
            type="text",
            placeholder="Enter text",
            style={"width": "70%", "padding": "8px"},
        ),
        html.Button(
            "Get length",
            id="file-button",
            n_clicks=0,
            style={
                "padding": "6px 12px",
                "marginTop": "20px",
            },
        ),
        html.H3(
            "",
            id="results",
        ),
    ]
    return layout, value
