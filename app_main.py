import click
import dash
import dash_mantine_components as dmc
from dash import html

from layouts.page_1.callbacks import register_cb_1
from layouts.page_1.layout import layout_1
from layouts.page_2.layout import layout_2
from layouts.page_3.layout import layout_3

app = dash.Dash(__name__, title="My project", suppress_callback_exceptions=True)
tab_names = ["Length", "Upload", "Compare"]

tab_1_layout, tab_1_val = layout_1()
tab_2_layout, tab_2_val = layout_2()
tab_3_layout, tab_3_val = layout_3()

# App layout
app.layout = dmc.MantineProvider(
    theme={"colorScheme": "light"},
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
                    id="tabs",
                    value=tab_1_val,
                    children=[
                        dmc.TabsList(
                            [
                                dmc.TabsTab(tab_names[0], value=tab_1_val),
                                dmc.TabsTab(tab_names[1], value=tab_2_val),
                                dmc.TabsTab(tab_names[2], value=tab_3_val),
                            ],
                        ),
                        dmc.TabsPanel(
                            tab_1_layout,
                            value=tab_1_val,
                        ),
                        dmc.TabsPanel(
                            tab_2_layout,
                            value=tab_2_val,
                        ),
                        dmc.TabsPanel(
                            tab_3_layout,
                            value=tab_3_val,
                        ),
                    ],
                ),
            ],
        ),
    ],
)

register_cb_1(app)


@click.command()
@click.option("--debug", is_flag=True, default=False, help="Run in debug mode")
@click.option("--port", default=8070, help="Port to run the server on")
@click.option("--host", default="0.0.0.0", help="Host to run the server on")
def run_server(debug, port, host):
    app.run(debug=debug, port=port, host=host)


if __name__ == "__main__":
    run_server()
