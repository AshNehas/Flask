from flask import Flask,render_template
app = Flask(__name__)

@app.route("/result")
def table1():
    mydic={
    'maths':80,
    'c': 70,
    'java':60,
    }
    print (mydic)
    return render_template('table.html',result=mydic)
 

if __name__=="__main__":
    app.run(debug=True)
