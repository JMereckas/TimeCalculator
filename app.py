from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "hwllo Justas "

@app.route('/clockin/<abc>')
def clockin(abc):
    return abc

if __name__ == '__main__':
    app.run(debug=True)
