from flask import Flask, request, jsonify, render_template
from google.generativeai import generate_text
import requests
import os

app = Flask(__name__)


# PALM_API_ENDPOINT = 'https://generativelanguage.googleapis.com/v1beta3/models/text-bison-001:generateText'
API_KEY = os.environ.get('MAKERSUITE_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/generate-poem', methods=['POST'])
# def generate_poem():
#     # Get the prompt from the request data
#     data = request.get_json()
#     prompt = data.get('prompt')
#     poem = generate_text(prompt=prompt)

#     # Return the generated poem as JSON
#     return jsonify({'poem': poem})


@app.route('/generate-poem', methods=['POST'])
def generate_poem():
    # Get the prompt from the request data
    data = request.get_json()
    prompt = data.get('prompt')
    poem = generate_text(prompt=prompt)

    payload = {
        'prompt': poem,
    }
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }

    response = requests.post(PALM_API_ENDPOINT, json=payload, headers=headers)

    # Check for a successful response and extract the poem
    if response.status_code == 200:
        poem_data = response.json()
        poem = poem_data.get('poem', 'No poem found')
    else:
        poem = 'Failed to generate poem'

    return jsonify({'poem': poem})

if __name__ == '__main__':
    app.run(debug=True)