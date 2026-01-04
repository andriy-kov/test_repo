from dash import Input, Output, State


def register_cb_1(app):
    @app.callback(
        Output("results", "children"),
        Input("file-button", "n_clicks"),
        State("search-input", "value"),
        prevent_initial_call=True,
    )
    def len_def(n_clicks, query):
        return f"The length is {len(query)}"
