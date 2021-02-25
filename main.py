import flask
import datetime
app = flask.Flask(__name__)
import pandas as pd
from icecream import ic
import plotly.graph_objects as go
import plotly.express as px

@app.route('/')
def hello_world():

    df = pd.read_csv("data/data.csv")
    ic(df.sort_values(by=['cases_weekly'], ascending=True))
    # ic(df.groupby(by=['countriesAndTerritories']))
    # fig = px.bar(df, x='dateRep', y='cases_weekly') # cases_weekly
    fig = px.bar(df, x='countriesAndTerritories', y='cases_weekly') # cases_weekly
    
    fig.write_html('COVID chart', auto_open=True)
    fig.show()

    return flask.render_template(
        "main.html",
        message_time=datetime.datetime.now()
    )

if __name__ == '__main__':
    app.run(debug=True)
    hello_world()