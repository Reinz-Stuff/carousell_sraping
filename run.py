import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def myphotography():
    with open('Extraction/result.json') as f:
        data = json.load(f)

        return render_template('index.html', product=data)


if __name__ == '__main__':
    app.run(port=5002, debug=True)