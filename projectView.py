from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def hello():
    return render_template("index.html", title="title from python", text="soucy, P-A")

if __name__ == "__main__":
  app.run(debug=True)

"""
class AddProject
    called when the user use the form and enter the requiered field
    store the info in DB
    update the liste on the client side
Class EditProject
class DelProject