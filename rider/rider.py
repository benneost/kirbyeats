from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root:root@localhost:3306/HungryFoodie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)  

class FoodOrder(db.Model):
    __tablename__ = 'FoodOrder'

    FoodOrderID = db.Column(db.String(13), primary_key=True)
    CustomerID = db.Column(db.String(64), nullable=False)
    RiderID = db.Column(db.Float(precision=2), nullable=False)
    DateTime = db.Column(db.Integer)
    RestaurantID = db.Column(db.Integer)
    FoodID = db.Column(db.Integer)
    Price = db.Column(db.Integer)
    Status = db.Column(db.Integer)

    def __init__(self, FoodOrderID, CustomerID, RiderID, DateTime,RestaurantID,FoodID,Price,Status):
        self.FoodOrderID = FoodOrderID
        self.CustomerID = CustomerID
        self.RiderID = RiderID
        self.DateTime = DateTime
        self.RestaurantID = RestaurantID
        self.FoodID = FoodID
        self.Price = Price
        self.Status = Status

    def json(self):
        return {"FoodOrderID": self.FoodOrderID, "CustomerID": self.CustomerID, "RiderID": self.RiderID, "DateTime": self.DateTime,
        "RestaurantID": self.RestaurantID, "FoodID": self.FoodID, "Price": self.Price, "Status": self.Status}

@app.route("/riderorders")
def get_all():
    orderlist = FoodOrder.query.all()
    if len(orderlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "orders": [order.json() for order in orderlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no orders."
        }
    ), 404

@app.route("/riderorders/<string:RiderID>")
def find_by_riderID(RiderID):
    orderlist = FoodOrder.query.filter_by(RiderID=RiderID).all()
    if len(orderlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "orders": [order.json() for order in orderlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Order not found."
        }
    ), 404

# Upon the collection of the food from the restaurant, the rider click on "Collected Food"
@app.route("/riderpickup/<string:FoodOrderID>", methods=['PUT'])
def update_pickuporder(FoodOrderID):
    order = FoodOrder.query.filter_by(FoodOrderID=FoodOrderID).first()
    if order:
        data = request.get_json()
        # if data['Status']:
        #     FoodOrder.Status = data['Status']
        order.Status = 'Delivering'
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": order.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "FoodOrderID": FoodOrderID
            },
            "message": "Order not found."
        }
    ), 404

# Upon the delivery of the food to the customer, the rider click on "Delivered"
@app.route("/riderdeliver/<string:FoodOrderID>", methods=['PUT'])
def update_deliverorder(FoodOrderID):
    order = FoodOrder.query.filter_by(FoodOrderID=FoodOrderID).first()
    if order:
        data = request.get_json()
        # if data['Status']:
        #     FoodOrder.Status = data['Status']
        order.Status = 'Delivered'
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": order.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "FoodOrderID": FoodOrderID
            },
            "message": "Order not found."
        }
    ), 404

# TBC - NOT CONFIRM IF IT IS ONE OF THE FUNCTIONS WE ARE IMPLEMENTING
# @app.route("/addrider/", methods=['POST'])
# def create_rider():

#     ###### data = request.get_json()
#     ###### print(data)
#     ###### apptDateTime = request.json.get('apptDateTime', None)
#     ###### apptStatus = request.get_json('apptStatus')
#     newR = newRider(RiderName='Christopher', VehicleNo='SGDH2626', RiderContact='90906966', PostalCode='163013')

#     try:
#         db.session.add(newR)
#         db.session.commit()
#     except Exception as e:
#         return jsonify(
#             {
#                 "code": 500,
#                  "data": {
#                      "RiderName": RiderName,
#                      "VehicleNo": VehicleNo,
#                      "RiderContact": RiderContact,
#                      "PostalCode": PostalCode
#                 },
#                 "message": "An error occurred adding a new rider. " + str(e)
#             }
#         ), 500

#     return jsonify(
#         {
#             "code": 201,
#             "data": appt.json()
#         }
#     ), 201

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000, debug=True)

# In the VS Code terminal, run the app by entering: 
# set dbURL=mysql+mysqlconnector://root@localhost:3306/HungryFoodie python3 rider.py
# export for macbook 

# build docker image 
# docker build -t auyongtingting/rider:1.0 ./
# docker run -p 5000:5000 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/rider auyongtingting/rider:1.0	