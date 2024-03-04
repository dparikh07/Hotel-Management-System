from flask import Flask

testapp = Flask(__name__)

@testapp.route("/")

def home():
    return "Hello world!!"