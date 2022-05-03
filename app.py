from flask import Flask, render_template
from waitress import serve

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('1.html')


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    serve(app, host='0.0.0.0', port=5000)
