import flask
import datetime
app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    return flask.render_template(
        "main.html",
        message_time=datetime.datetime.now()
    )