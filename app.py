from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template

import google.generativeai as palm
import os

load_dotenv()

API_KEY = os.environ.get('MAKERSUITE_API_KEY')
palm.configure(api_key=API_KEY)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-poem', methods=['POST'])
def generate_poem():
    data = request.form
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({'error': 'Prompt text is required.'})
    poem = palm.generate_text(prompt=prompt).result
    return render_template('response.html', poem=poem)

if __name__ == '__main__':
    app.run(debug=True)