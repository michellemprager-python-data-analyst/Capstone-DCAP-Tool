from flask import Flask, render_template
import cleaner

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run")
def run_tool():
    cleaner.main()
    return "DCAP Tool ran successfully!"

if __name__ == "__main__":
    app.run(debug=True)

