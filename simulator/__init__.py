# typical way to initialize a flask app 
from flask import Flask, redirect, url_for, request, Response, jsonify

app = Flask(__name__)

from simulator import views