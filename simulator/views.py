# import all necessary modules and plugins
from simulator import app
from flask import Flask, render_template, request, url_for, flash, redirect, jsonify
from pip._vendor import requests
from werkzeug.exceptions import abort


# routing index page
@app.route('/')
def index():
    return render_template('index.html')
  

# routing to post parameters from ussd to external api 
@app.route('/get_post_json', methods=['GET', 'POST'])
def get_post_json():

  # receive value from input field through ajax. *check form.js as reference*
  ussd_query = request.get_json().get("USSD_STRING")
  
  # split and convert ussd_query to a list of values
  ussd_codes = ussd_query.split("*")
  
  # specify the phone number to be used for testing purposes
  phone_number = "2348144149628"
  
  # **VERY IMPORTANT** Specify the particular api you want to test. 
  callback_url = "http://127.0.0.1:5001/api?"
  
  # the first part of the ussd_codes variable is the service code 
  service_code = ussd_codes[1]

  # the second part of the ussd_codes variable is the ussd_string   
  ussd_string = ussd_codes[2].strip("#")
  
  # turn all the variables above to key-value pairs * a dictionary *
  params = {"phoneNumber":phone_number,"USSD_STRING":ussd_string,"serviceCode":service_code}
  
  # send a request to your specified api as query string parameters
  post = requests.post(callback_url, params=params)
  
  # code to display feedback response from the api to confirm if it was successful
  # return "<p>"+post.text+"</p>"
  return render_template('index.html')
