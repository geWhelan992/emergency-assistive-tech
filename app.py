from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/demo")
def demo_page():
    return render_template("demoPage.html")

@app.route("/intercom")
def intercom_page():
    return render_template("intercom.html")  # just your video page now

@app.route("/instruction")
def instruction_page():
    return render_template("instructionPage.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
