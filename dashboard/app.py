from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import os
os.chdir('C:/Users/User/Desktop/Marketing/Marketing-Analytics/dashboard')
app = Dash(__name__)

df = pd.read_csv('export_dataset.csv')

fig = px.bar(df, x="version", y="minutes_play", color="day_1_active", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='A/B test'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)