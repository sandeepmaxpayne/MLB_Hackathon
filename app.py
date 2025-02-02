import time
from flask import Flask, render_template, request

from mlb_tip_generator import generate_tagline

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_data = request.form['user_input']
    result = generate_tagline(user_data)
    time.sleep(5)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
