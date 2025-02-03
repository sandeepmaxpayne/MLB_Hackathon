import time
from flask import Flask, jsonify, render_template, request
from dotenv import load_dotenv
import os
from mlb_tip_generator import generate_tagline
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)


# Get environment variables
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_data = request.form['user_input']
    result = generate_tagline(user_data)
   # return render_template('index.html', result=result)
    return jsonify(result=result)
if __name__ == '__main__':
    app.run(debug=True)
