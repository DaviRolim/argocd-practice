from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>I am really enjoying to learn kubernetes and CI/CD tools. Go DevOps</h1>'


if __name__ == "__main__":
    app.run(debug=True)
