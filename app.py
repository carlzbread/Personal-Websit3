from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    """
    Renders the home page.
    """
    return render_template("index.html")

if __name__ == "__main__":
    # Run the Flask app
    app.run(host="0.0.0.0", port=80, debug=True)