#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script

import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from datetime import datetime
import json
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root:root@localhost:3306/esd-order'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}
app.config['JSON_SORT_KEYS'] = False #json output will not be sorted

db = SQLAlchemy(app)

CORS(app)  

class Order(db.Model):
    __tablename__ = 'order'

    orderID = db.Column(db.Integer, primary_key=True)
    customerID = db.Column(db.Integer, nullable=False)
    restaurantID = db.Column(db.Integer, nullable=False)
    riderID = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(10), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    modified = db.Column(db.DateTime, nullable=False,
                         default=datetime.now, onupdate=datetime.now)

    def json(self):
        dto = {
            'orderID': self.orderID,
            'customerID': self.customerID,
            'restaurantID': self.restaurantID,
            'riderID': self.riderID,
            'status': self.status,
            'created': self.created,
            'modified': self.modified
        }

        dto['order_item'] = []
        for oi in self.order_item:
            dto['order_item'].append(oi.json())

        return dto


class Order_Item(db.Model):
    __tablename__ = 'order_item'

    itemID = db.Column(db.Integer, primary_key=True)
    orderID = db.Column(db.ForeignKey(
        'order.orderID', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    foodID = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    # orderID = db.Column(db.String(36), db.ForeignKey('order.orderID'), nullable=False)
    # order = db.relationship('Order', backref='order_item')
    order = db.relationship(
        'Order', primaryjoin='Order_Item.orderID == Order.orderID', backref='order_item')

    def json(self):
        return {'itemID': self.itemID, 'orderID': self.orderID, 'foodID': self.foodID, 'quantity': self.quantity}


@app.route("/order")
def get_all():
    orderlist = Order.query.all()
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


@app.route("/order/<string:orderID>")
def find_by_orderID(orderID):
    order = Order.query.filter_by(orderID=orderID).first()
    if order:
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
                "orderID": orderID
            },
            "message": "Order not found."
        }
    ), 404


@app.route("/order", methods=['POST'])
def create_order():
    customerID = request.json.get('customerID', None)
    order = Order(customerID=customerID, status='NEW')

    cart_item = request.json.get('cart_item')
    for item in cart_item:
        order.order_item.append(Order_Item(
            book_id=item['book_id'], quantity=item['quantity']))

    try:
        db.session.add(order)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the order. " + str(e)
            }
        ), 500
    
    print(json.dumps(order.json(), default=str)) # convert a JSON object to a string and print
    print()

    return jsonify(
        {
            "code": 201,
            "data": order.json()
        }
    ), 201


@app.route("/order/<string:orderID>", methods=['PUT'])
def update_order(orderID):
    try:
        order = Order.query.filter_by(orderID=orderID).first()
        if not order:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "orderID": orderID
                    },
                    "message": "Order not found."
                }
            ), 404

        # update status
        data = request.get_json()
        if data['status']:
            order.status = data['status']
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": order.json()
                }
            ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "orderID": orderID
                },
                "message": "An error occurred while updating the order. " + str(e)
            }
        ), 500


if __name__ == '__main__':
    print("This is flask for KirbyEats" + os.path.basename(__file__) + ": manage orders ...")
    app.run(host='0.0.0.0', port=5001, debug=True)
