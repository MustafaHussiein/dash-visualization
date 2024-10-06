import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

data = pd.read_csv("economic-inequality-gini-index.csv")
data = data.query("Entity == 'Argentina' and Code == 'ARG'")
data["Year"] = pd.Series(data["Year"])
data.sort_values("Year", inplace=True)

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="economic-inequality-Analytics",),
        html.P(
            children="Gini index measures the extent to which the distribution of income (or, in some cases, consumption expenditure) among individuals or households within an economy deviates from a perfectly equal distribution. A Lorenz curve plots the cumulative percentages of total income received against the cumulative number of recipients, starting with the poorest individual or household. The Gini index measures the area between the Lorenz curve and a hypothetical line of absolute equality, expressed as a percentage of the maximum area under the line. Thus a Gini index of 0 represents perfect equality, while an index of 100 implies perfect inequality.",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Year"],
                        "y": data["GINI index (World Bank estimate)"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "economic-inequality-Analytics for Argentina"},
            },
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)