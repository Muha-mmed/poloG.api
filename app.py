from flask import Flask, jsonify
from flask_cors import CORS
import random
from quotes import quotes

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/quotes')
def index():
    return jsonify(quotes)

@app.route('/quote/<int:id>')
def get_quote_by_id(id):
    for quote in quotes:
        if quote['id'] == id:
            return jsonify(quote)
    return jsonify({'error': 'quote not found'})

@app.route('/quote/rand_quote')
def get_random_quote():
    quote = random.choice(quotes)
    return jsonify(quote)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
