from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/hungryfoodie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Restaurant(db.Model):
    __tablename__ = "restaurant"

    RestaurantID = db.Column(db.Integer, unique = True, primary_key = True)
    RestaurantName = db.Column(db.String(100), nullable = False)
    RestaurantContact = db.Column(db.String(8), nullable = False)
    RestaurantAddress = db.Column(db.String(100), nullable = False)
    PostalCode = db.Column(db.Integer, nullable = False)

    def __init__(self, RestaurantID, RestaurantName, RestaurantContact, RestaurantAddress, PostalCode):
        self.RestaurantID = RestaurantID
        self.RestaurantName = RestaurantName
        self.RestaurantContact = RestaurantContact
        self.RestaurantAddress = RestaurantAddress
        self.PostalCode = PostalCode

    def json(self):
        return {"RestaurantID" : self.RestaurantID, "RestaurantName" : self.RestaurantName, "RestaurantContact" : self.RestaurantContact, "RestaurantAddress": self.RestaurantAddress, "PostalCode" : self.PostalCode}

@app.route("/restaurant")

def get_all():
    restaurantlist = Restaurant.query.all()
    if len(restaurantlist):
        return jsonify(
            {
                "code" : 200,
                "data" : {
                    "restaurants" : [restaurant.json() for restaurant in restaurantlist]
                }
            }
        )
    return jsonify(
        {
            "code" : 404,
            "message" : "There are no restaurants."
        }
    ), 404

@app.route("/restaurant/<string:RestaurantID>")

def find_by_restaurantID(RestaurantID):
    restaurant = Restaurant.query.filter_by(RestaurantID = RestaurantID).first()
    if restaurant:
        return jsonify(
            {
                "code" : 200,
                "data" : restaurant.json()
            }
        )
    return jsonify(
        {
            "code" : 404,
            "message" : "Restaurant not found."
        }
    ), 404

@app.route("/restaurant/<string:RestaurantID>", methods=["POST"])

def create_restaurant(RestaurantID):
    if (Restaurant.query.filter_by(RestaurantID = RestaurantID).first()):
        return jsonify(
            {
                "code" : 400,
                "data" : {
                    "RestaurantID" : RestaurantID
                },
                "message" : "Restaurant already exists."
            }
        ), 400
    
    data = request.get_json()
    restaurant = Restaurant(RestaurantID, **data)

    try:
        db.session.add(restaurant)
        db.session.commit()
    except:
        return jsonify(
            {
                "code" : 500,
                "data" : {
                    "restaurantID" : RestaurantID
                },
                "message" : "An error occurred creating the book."
            }
        ), 500

    return jsonify(
        {
            "code" : 201,
            "data" : restaurant.json()
        }
    ), 201

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=5000, debug=True)