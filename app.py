from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello"

@app.route('/clockin/<abc>')
def clockin(abc):
    return render_template("index.html",name=abc)

if __name__ == '__main__':
    app.run(debug=True)
