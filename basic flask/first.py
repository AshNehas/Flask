from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def index():
    name="Ashwini kailash mogal"
    list5=[1,2,3]
    return render_template('first.html', name=name,list5=list5)
 

if __name__=="__main__":
    app.run(debug=True)
