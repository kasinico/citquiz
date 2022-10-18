from flask import Flask

app = Flask(__name__) #an instance of clask




#routes ('@' is a decorator)
@app.route('/')
def index():
    return "Hello Uganda"


if __name__ == "__main__":
    app.run(debug=True)
