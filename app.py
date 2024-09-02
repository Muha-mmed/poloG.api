from flask import Flask
import random
from quotes import quotes
import os
# 4105 4000 2019 1423
app = Flask(__name__) 

#get all quotes
@app.route('/quotes')
def index():
    return quotes

#get single quote by it's id
@app.route('/quote/<int:id>')
def get_quote_by_id(id):
    for quote in quotes:
        if quote['id'] == id:
            return quote
    return {'error': 'quote not found'}

#get random quote
@app.route('/quote/rand_quote')
def get_random_quote():
    quote = random.choice(quotes)
    return quote    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
