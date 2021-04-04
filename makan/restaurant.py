from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/esd-restaurant'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Restaurant(db.Model):
    __tablename__ = "restaurant"

    restaurantID = db.Column(db.Integer, unique = True, primary_key = True)
    restaurantName = db.Column(db.String(100), nullable = False)
    restaurantContact = db.Column(db.String(8), nullable = False)
    restaurantAddress = db.Column(db.String(100), nullable = False)
    postalCode = db.Column(db.Integer, nullable = False)

    def __init__(self, restaurantID, restaurantName, restaurantContact, restaurantAddress, postalCode):
        self.restaurantID = restaurantID
        self.restaurantName = restaurantName
        self.restaurantContact = restaurantContact
        self.restaurantAddress = restaurantAddress
        self.postalCode = postalCode

    def json(self):
        return {"restaurantID" : self.restaurantID, "restaurantName" : self.restaurantName, "restaurantContact" : self.restaurantContact, "restaurantAddress": self.restaurantAddress, "postalCode" : self.postalCode}

class Food(db.Model):
    __tablename__ = "food"

    foodID = db.Column(db.Integer, unique = True, primary_key = True)
    restaurantID = db.Column(db.Integer, nullable = False)
    foodName = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(100), nullable = False)
    price = db.Column(db.Float, nullable = False)

    def __init__(self, foodID, restaurantID, foodName, description, price):
        self.foodID = foodID
        self.restaurantID = restaurantID
        self.foodName = foodName
        self.restaurantAddress = restaurantAddress
        self.postalCode = postalCode

    def json(self):
        return {"foodID" : self.foodID, "restaurantID" : self.restaurantID, "foodName" : self.foodName, "description": self.description, "price" : self.price}

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

@app.route("/restaurant/<string:restaurantID>")

def find_by_restaurantID(restaurantID):
    restaurant = Restaurant.query.filter_by(restaurantID = restaurantID).first()
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

@app.route("/restaurant/<string:restaurantID>", methods=["POST"])

def create_restaurant(restaurantID):
    if (Restaurant.query.filter_by(restaurantID = restaurantID).first()):
        return jsonify(
            {
                "code" : 400,
                "data" : {
                    "restaurantID" : restaurantID
                },
                "message" : "Restaurant already exists."
            }
        ), 400
    
    data = request.get_json()
    restaurant = Restaurant(restaurantID, **data)

    try:
        db.session.add(restaurant)
        db.session.commit()
    except:
        return jsonify(
            {
                "code" : 500,
                "data" : {
                    "restaurantID" : restaurantID
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
    app.run(host = "0.0.0.0", port=5005, debug=True)