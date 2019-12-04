from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
@app.route("/home")
def home() :
    return render_template('index.html')

if __name__ == '__main__' :
    CORS(app)
    app.run(port= '8000', debug= True)
