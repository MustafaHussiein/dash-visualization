import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

data = pd.read_csv("child-mortality-gdp-per-capita.csv")
data = data.query("Entity == 'Afghanistan' and Code == 'AFG'")
data["Year"] = pd.Series(data["Year"])
data.sort_values("Year", inplace=True)

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="GDP per capita Analytics",),
        html.P(
            children="GDP per capita adjusted for price changes over time (inflation) and price differences between countries – it is measured in international-$ in 2011 prices.",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Year"],
                        "y": data["GDP per capita"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "GDP per capita Analytics for Afghanistan"},
            },
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)