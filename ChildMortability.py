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
        html.H1(children="Child mortality Analytics",),
        html.P(
            children="Child mortality is defined as the number of children born alive that die before their 5th birthday. GDP per capita is adjusted for price changes over time and between countries (measured in international-$ in 2011 prices).",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Year"],
                        "y": data["Child mortality (Select Gapminder, v10) (2017)"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Child mortality Analytics for Afghanistan"},
            },
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)