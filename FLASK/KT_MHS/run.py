from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/') 
def index():
    return render_template('index.html') 

@app.route('/insert') 
def insert():
    return render_template('insert.html') 

@app.route('/list') 
def lists():
    return render_template('lists.html') 

@app.route('/login') 
def login():
    return render_template('login.html') 

if __name__ == "__main__":
    app.run(debug=True)