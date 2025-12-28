from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)  # Enables real-time communication


@app.route("/")
def home():
    return render_template("homePages.html")

@app.route("/index")
def index_page():
    return render_template("indexPage.html")

@app.route("/intercom")
def intercom_page():
    return render_template("intercom.html")

# ----- Simulated intercom trigger -----
@app.route("/trigger_intercom/<intercom_name>/<message>")
def trigger_intercom(intercom_name, message):
    # Emit a real-time alert to all connected clients
    socketio.emit('intercom_alert', {'intercom': intercom_name, 'message': message})
    return f"Triggered intercom '{intercom_name}' with message: {message}"


@app.route("/instruction")
def instruction_page():
    return render_template("instructionPage.html")


if __name__ == "__main__":
    socketio.run(app, debug=True)
