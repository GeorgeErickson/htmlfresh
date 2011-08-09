from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import datetime, os

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
  
###############################################
#Routes
###############################################
@app.route('/')
def home():
  return render_template('home.html', title='home', page='home')  

if __name__ == '__main__':
    app.run()
    
application = app