from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template('index.html',name=name)
@app.route("/")
def index():
    items = ['item1', 'item2', 'item3']
    return render_template('template.html', items=items)

if __name__ == "__main__":
    app.run(debug=True)
