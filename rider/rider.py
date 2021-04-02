from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root:root@localhost:3306/esd-rider'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)  

class Rider(db.Model):
    __tablename__ = 'rider'

    riderID = db.Column(db.Integer, primary_key=True)
    riderName = db.Column(db.String(100), nullable=False)
    vehicleNo = db.Column(db.String(8), nullable=False)
    phone = db.Column(db.String(8),nullable=False)
    location = db.Column(db.String(6),nullable=False)

    def __init__(self, riderID, riderName, vehicleNo, phone,location):
        self.riderID = riderID
        self.riderName = riderName
        self.vehicleNo = vehicleNo
        self.phone = phone
        self.location = location

    def json(self):
        return {"riderID": self.riderID, "riderName": self.riderName, "vehicleNo": self.vehicleNo, "phone": self.phone,
        "location": self.location}

@app.route("/rider/<string:riderID>")
def riderinfodisplay(riderID):
    riderdata = Rider.query.filter_by(riderID=riderID).first()

    if riderdata:
        return jsonify(
            {
                "code": 200,
                "data": riderdata.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There is no such rider."
        }
    ), 404

# Update RiderName
@app.route("/ridereditname/<string:riderID>", methods=['PUT'])
def update_ridername(riderID):
    riderdata = Rider.query.filter_by(riderID=riderID).first()
    if riderdata:
        data = request.get_json()
        riderdata.riderName = 'John Tan'
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": riderdata.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Update Error."
        }
    ), 404

# Update RiderVehicle
@app.route("/ridereditvehicle/<string:riderID>", methods=['PUT'])
def update_ridervehicle(riderID):
    riderdata = Rider.query.filter_by(riderID=riderID).first()
    if riderdata:
        data = request.get_json()
        riderdata.vehicleNo = 'SGX1234'
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": riderdata.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Update Error."
        }
    ), 404

# Update RiderContact
@app.route("/ridereditcontact/<string:riderID>", methods=['PUT'])
def update_ridercontact(riderID):
    riderdata = Rider.query.filter_by(riderID=riderID).first()
    if riderdata:
        data = request.get_json()
        riderdata.phone = '87006969'
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": riderdata.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Update Error."
        }
    ), 404

# Update RiderPostalCode
@app.route("/ridereditpostalcode/<string:riderID>", methods=['PUT'])
def update_riderpostalcode(riderID):
    riderdata = Rider.query.filter_by(riderID=riderID).first()
    if riderdata:
        data = request.get_json()
        riderdata.location = '190283'
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": riderdata.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Update Error."
        }
    ), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000, debug=True)

# if __name__ == '__main__':
#     app.run(host="0.0.0.0",port=5000, debug=True)

# In the VS Code terminal, run the app by entering: 
# set dbURL=mysql+mysqlconnector://root@localhost:3306/HungryFoodie python3 rider.py
# export for macbook 

# build docker image 
# docker build -t auyongtingting/rider:1.0 ./
# docker run -p 5000:5000 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/rider auyongtingting/rider:1.0	