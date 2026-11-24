from flask import Flask, render_template, request
from analyzer import analyze_log
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    if request.method == "POST":
        if "logfile" in request.files:
            file = request.files["logfile"]
            if file.filename != "":
                filepath = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(filepath)
                results = analyze_log(filepath)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)