from flask import Flask

print __name__
app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

app.run(debug=True)