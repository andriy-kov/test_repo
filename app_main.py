import dash
import dash_mantine_components as dmc
from dash import Input, Output, State, dash_table, dcc, html

app = dash.Dash(__name__, title="Проєкт Беринда [Ідентифікація мовців]")
app.config.suppress_callback_exceptions = True

# App layout
app.layout = html.Div(
    children=[
        html.Div(
            style={
                "maxWidth": "1200px",
                "margin": "20px auto",
                "padding": "20px",
                "borderRadius": "10px",
            },
            children=[
                html.H1(app.title, style={"textAlign": "center"}),
                html.Div(
                    style={
                        "textAlign": "start"
                    },  # https://developer.mozilla.org/en-US/docs/Web/CSS/text-align
                    children=[
                        html.H6("", id="model_alias"),
                    ],
                ),
                dmc.Tabs(
                    [
                        dmc.TabsList(
                            [
                                dmc.Tab("Search", value="search"),
                                dmc.Tab("Upload", value="upload"),
                                dmc.Tab("Compare", value="compare"),
                            ]
                        ),
                        dmc.TabsPanel(
                            [html.H3("Search")], value="search",
                        ),
                        dmc.TabsPanel(
                            [html.H3("Upload settings")], value="upload",
                        ),
                        dmc.TabsPanel(
                            [html.H3("Compare settings")], value="compare",
                        ),
                    ],
                ),
            ],
        ),
    ],
  style={"fontFamily": '"Courier New", monospace'},
)

@click.command()
@click.option("--debug", is_flag=True, default=False, help="Run in debug mode")
@click.option("--port", default=8070, help="Port to run the server on")
@click.option("--host", default="0.0.0.0", help="Host to run the server on")
def run_server(debug, port, host):

  app.run(debug=debug, port=port, host=host)

if __name__ == "__main__":
    run_server()                     
                              
