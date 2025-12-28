from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("homePages.html")

@app.route("/index")
def index_page():
    return render_template("indexPage.html")

@app.route("/intercom")
def intercom_page():
    return render_template("intercom.html")  # just your video page now

@app.route("/instruction")
def instruction_page():
    return render_template("instructionPage.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
