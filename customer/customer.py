from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/esd-customer'
#app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/esd-customer' or environ.get('customer_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Customer(db.Model):
    __tablename__ = 'customer'

    customerID = db.Column(db.String(64), nullable=False, primary_key = True)
    customerName = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(64), nullable=False)
    postalCode = db.Column(db.Integer, nullable=False)

    def __init__(self, customerID, customerName, phone, address, postalCode):
        self.customerID = customerID
        self.customerName = customerName
        self.phone = phone
        self.address = address
        self.postalCode = postalCode

    def json(self):
        return {"customerID": self.customerID, "customerName": self.customerName, "phone": self.phone, "address": self.address, "postalCode": self.postalCode}


@app.route("/delivery", methods=['GET'])
def get_all():
    customerlist = Customer.query.all()
    if len(customerlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "customers": [customer.json() for customer in customerlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no such customer."
        }
    ), 404


@app.route("/delivery/<string:customerID>")
def find_by_customerID(customerID):
    customer = Customer.query.filter_by(customerID=customerID).first()
    if customer:
        return jsonify(
            {
                "code": 200,
                "data": customer.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Customer not found."
        }
    ), 404


@app.route("/delivery/<string:customerID>", methods=['POST'])
def create_customer(customerID):
    if (Customer.query.filter_by(customerID=customerID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "customerID": customerID
                },
                "message": "Customer already exists."
            }
        ), 400
 
    data = request.get_json()
    customer = Customer(customerID, **data)

    try:
        db.session.add(customer)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "customerID": customerID
                },
                "message": "An error occurred creating the customer."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": customer.json()
        }
    ), 201


@app.route("/delivery/<string:customerID>", methods=['PUT'])
def update_customer(customerID):
    customer = Customer.query.filter_by(customerID=customerID).first()
    if customer:
        #customer.address = "OneNorth"
        #print(customer)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": customer.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "customerID": customerID
            },
            "message": "Customer not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(port=5000, debug=True)






