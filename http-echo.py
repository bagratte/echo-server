import flask


app = flask.Flask(__name__)

@app.route('/', defaults={'path': '/'})
@app.route('/<path:path>')
def index(path):
    print(flask.request.headers, flush=True)
    return flask.Response(status=200)
