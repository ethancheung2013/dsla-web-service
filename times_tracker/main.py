from flask import Flask, request, abort
app = Flask(__name__)
import json
from search import search

@app.route("/")
def hello():
    return "Welcome to the Data Science Web Service!"

@app.route("/search")
def search_articles():
    query = request.args.get('q')
    if query is None:
        abort(400) # bad request
    else:
        return json.dumps(list(search(query)))

if __name__ == "__main__":
    app.run(host ='0.0.0.0', debug = True)
