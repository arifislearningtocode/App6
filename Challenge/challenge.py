from flask import Flask, render_template
import pandas as pd

challenge = Flask(__name__)


@challenge.route('/')
def home():
    return render_template('home.html')


@challenge.route('/api/v1/<word>')
def api(word):
    filename = "dictionary.csv"
    df = pd.read_csv(filename, parse_dates=['word'])
    meaning = str(df.loc[df['word'] == word]['definition'].squeeze())
    return {
            "definition": meaning,
            "word": word
            }


challenge.run(debug=True, port=5001)
