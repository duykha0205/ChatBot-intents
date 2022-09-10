from xml.etree.ElementTree import fromstring
from flask import Flask, jsonify, render_template, request
from gui import chatbot_response

appWeb = Flask(__name__)


@appWeb.get("/")
def index_get():
    return render_template("base.html")


@appWeb.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: CHECK IF TEXT IS VALID
    response = chatbot_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    appWeb.run(debug=True)