"""
* 
* flask_example.py
* Author:
* Renato Jensen Filho
* 2016-09-08
* 
"""

from flask import Flask, render_template

application=Flask(__name__)

@application.route('/')
def home():
    return render_template("home.html")

@application.route('/about')
def about():
    return render_template("about.html")


if __name__=="__main__":
    application.run(debug=True)
