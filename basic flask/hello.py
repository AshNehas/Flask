from flask import Flask
app = Flask(__name__)

@app.route("/hi/<name>")
def hello_ash(name):
    return 'HEllO World'+name

@app.route("/hi/<int:name1>")
def hello_ash2(name1):
    return 'roll no is %d' %name1


@app.route("/about")
def index1():
    return 'python workshop'

if __name__=="__main__":
    app.run(debug=True)
