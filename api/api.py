import flask
from flask import request, jsonify
from utils import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]



@app.route('/', methods=['GET'])
def home():
    return "<h1>home page</h1>"

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/runner', methods=['GET'])
def system_runner():
    if 'cmd' in request.args:
        cmd = request.args['cmd']
    else:
        return "Unknown query parameter"
    # perform_sys_call('adahome')
    return perform_sys_call(cmd)

    

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    #check if an ID is provided as part of the url.
    #if it is provided, proceed with the flow else display an error message

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    
    results = []

    for book in books:
        if book['id'] == id:
            results.append(book)

    return jsonify(results)

app.run()

