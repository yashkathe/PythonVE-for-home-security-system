from flask import Flask 
from flask import render_template
app = Flask(__name__)
app.debug =True #errors will be shown on terminal 

@app.route("/")
def hello():
    return render_template('hello.html' , message='Sem 4 mini project') 
    #this will look for the file hello.html and pass 'hello world' to
    #variable named message

@app.route("/example")
def example_route():
    return "This is an example route"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
