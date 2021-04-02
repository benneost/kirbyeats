from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root:root@localhost:3306/HungryFoodie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)  

class Rider(db.Model):
    __tablename__ = 'Rider'

    RiderID = db.Column(db.Integer, primary_key=True)
    RiderName = db.Column(db.String(100), nullable=False)
    VehicleNo = db.Column(db.String(100), nullable=False)
    RiderContact = db.Column(db.Integer,nullable=False)
    PostalCode = db.Column(db.Integer,nullable=False)

    def __init__(self, RiderID, RiderName, VehicleNo, RiderContact,PostalCode):
        self.RiderID = RiderID
        self.RiderName = RiderName
        self.VehicleNo = VehicleNo
        self.RiderContact = RiderContact
        self.PostalCode = PostalCode

    def json(self):
        return {"RiderID": self.RiderID, "RiderName": self.RiderName, "VehicleNo": self.VehicleNo, "RiderContact": self.RiderContact,
        "PostalCode": self.PostalCode}

@app.route("/rider/<string:RiderID>")
def riderinfodisplay(RiderID):
    riderinfo = Rider.query.filter_by(RiderID=RiderID).first()

    if riderinfo:
        return jsonify(
            {
                "code": 200,
                "data": riderinfo.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There is no such rider."
        }
    ), 404

# Update RiderName
@app.route("/ridereditname/<string:RiderID>", methods=['PUT'])
def update_ridername(RiderID):
    rider = Rider.query.filter_by(RiderID=RiderID).first()
    if rider:
        data = request.get_json()
        rider.RiderName = 'John Tan'
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": rider.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Update Error."
        }
    ), 404

# Update RiderContact
@app.route("/ridereditcontact/<string:RiderID>", methods=['PUT'])
def update_ridercontact(RiderID):
    rider = Rider.query.filter_by(RiderID=RiderID).first()
    if rider:
        data = request.get_json()
        rider.RiderContact = '87006969'
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": rider.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Update Error."
        }
    ), 404

# Update RiderPostalCode
@app.route("/ridereditpostalcode/<string:RiderID>", methods=['PUT'])
def update_riderpostalcode(RiderID):
    rider = Rider.query.filter_by(RiderID=RiderID).first()
    if rider:
        data = request.get_json()
        rider.PostalCode = '190283'
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": rider.json()
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