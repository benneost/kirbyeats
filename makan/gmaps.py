from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import requests
import smtplib 

app = Flask(__name__)

CORS(app)




# API key
# api_file = open("api-key.txt", "r")
# api_key = api_file.readline()
# api_file.close()
api_key = "AIzaSyDeWOuGGRp5f4LIa2HC2jL0qcKLJeB82WE"

# home address input
home = "Singapore 520334"
# input("Enter a home address\n") 
  
# work address input
# work = input("Enter a work address\n") 
  
# base url
# url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

# get response
# r = requests.get(url + "origins=" + home + "&destinations=" + work + "&key=" + api_key) 
 
# return time as text and as seconds
# time = r.json()["rows"][0]["elements"][0]["duration"]["text"]       
# seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]
  
# print the travel time
# print("\nThe total travel time from home to work is", time)

@app.route('/gmaps/<string:destination>', methods=['GET', 'POST'])
def calculate_time(destination):
    origin = "Singapore 529757"
    api_key = "AIzaSyDeWOuGGRp5f4LIa2HC2jL0qcKLJeB82WE"

    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&"
    r = requests.get(url + "origins=" + home + "&destinations=" + destination + "&key=" + api_key) 

    time = r.json()["rows"][0]["elements"][0]["duration"]["text"]       
    distance = r.json()["rows"][0]["elements"][0]["distance"]["text"]       
    # seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]

    return jsonify(
        {
            "code" : 200,
            "data" : {
                "time" : time,
                "distance" : distance
            }
        }
    )

if __name__ == "__main__":
    app.run(port=5007, debug=True)