from flask import Flask, render_template

challenge = Flask(__name__)


@challenge.route('/')
def home():
    return render_template('home.html')


@challenge.route('/api/v1/<word>')
def api(word):
    return {
            "definition": word.upper(),
            "word": word
            }


if __name__ == "__main__":
    challenge.run(debug=True, port=5001)
