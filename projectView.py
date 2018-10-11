from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Lorem ipsum dolor sit amet"

if __name__ == "__main__":
  app.run()
