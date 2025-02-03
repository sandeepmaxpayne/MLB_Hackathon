import time
from flask import Flask, jsonify, render_template, request

from mlb_tip_generator import generate_tagline

app = Flask(__name__)

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
