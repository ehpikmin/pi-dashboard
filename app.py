from flask import Flask, render_template, jsonify
import psutil

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/stats")
def stats():
    return jsonify(
        cpu=psutil.cpu_percent(interval=0.5),
        memory=psutil.virtual_memory().percent,
    )

if __name__ == "__main__":
    app.run(debug=True, port=5001)
