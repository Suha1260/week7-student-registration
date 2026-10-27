
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("registration.html")

@app.route("/success", methods=["POST"])
def success():
    return render_template(
        "success.html",
        name=request.form["name"],
        sid=request.form["sid"],
        email=request.form["email"],
        phone=request.form["phone"],
        year=request.form["year"]
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
