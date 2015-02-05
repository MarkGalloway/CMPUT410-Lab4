# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
app = Flask(__name__)

@app.route('/taskr')
def hello_world():
    return 'Hello, World!'



if __name__ == '__main__':
  app.run()