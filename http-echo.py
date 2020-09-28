import flask


app = flask.Flask(__name__)

@app.route('/', defaults={'path': '/'}, methods=('GET', 'POST'))
@app.route('/<path:path>', methods=('GET', 'POST'))
def index(path):
    print(flask.request.headers, flush=True),
    return flask.Response(status=200)
