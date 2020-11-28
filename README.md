# A USSD Simulator App to test USSD APIs

Need for an offline tool to test the functionallity of your ussd api running on your local machine. 
Built with Flask Jinja templates, JS/JQuery/Ajax, Bootstrap, Font Awesome and SweetAlerts. You will need to have Python/Anaconda locally installed on your machine before you can install Flask. The rest use CDNs to load them.

Don't have Python/Anaconda? No problem!

Access the online version at _______________________ (coming soon)

#### Please read the instructions below to understand how the app works and how you can configure it to work for you:

## 1. RUNNING ON YOUR LOCAL MACHINE

### To run on your local machine if you already have Python installed, run the following code:

*note: all these commands below should be done after you've downloaded the code to your local machine and you're inside the folder in your terminal

 -> pip install flask 
 -> python -m venv env
 -> env\Scripts\activate
 -> $env:FLASK_APP = "simulator"
 -> $env:FLASK_ENV = "development"
 -> flask run

 The app should be running now on http://127.0.0.1:5000/ if you've done all that is needed to do

### 2. HOW THE SIMULATOR WORKS

 The interface is a typical phone dialer interface with number from 0 - 9  and a button to send the ussd code.

 It accepts code in the format *service code*ussd string# e.g *384*98494947934399303#

 It then uses ajax to collect the value from the input field and send to flask which then seperates the code into two parameters. The first part the service code, and the second part the ussd string.

 The Callback url/API and Phone number is hard coded in the views.py file. 

 You should change the Callback url to the address of your API. **very important**

 You can decide to change the Phone number of leave it as is. It's just for testing purposes

 The four parameters are sent as query string to your specified API (Callback url) for further processing

 *note: You are only supposed to modify the views.py file. Please do not modify anything on the static folder unless you really know what you are doing.

 I hope this helps. Contact me at george.isiguzo@yahoo.com in case of any enquiry. Thank you.

 Thanks to https://codepen.io/azizurrahman/pen/YGKgro for the user interface.
