from flask import Flask, redirect, url_for, request, render_template, session

app = Flask(__name__)
#code to create flask application

@app.route('/', methods=['GET'])  #indicate the route we want to create 
def index():
    return render_template('index.html')