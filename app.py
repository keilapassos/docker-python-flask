from flask import Flask

app = Flask(__name__)

@app.get("/")
def send_to_home_page():
    return "Home page here"