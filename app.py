from flask import Flask, render_template
import cleaner

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run')
def run_tool():
    result = cleaner.main()
    if "error" in result:
        return render_template('results.html', error=result["error"], success=False)
    return render_template('results.html', result=result, success=True)

if __name__ == "__main__":
    app.run(debug=True)
