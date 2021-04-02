from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/hungryfoodie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Rider(db.Model):
    __tablename__ = "rider"

    RiderID = db.Column(db.Integer, unique=True, primary_key=True)
    RiderName = db.Column(db.String(100), nullable=False)
    VehicleNo = db.Column(db.String(100), nullable=False)
    RiderContact = db.Column(db.Integer, nullable=False)
    PostalCode = db.Column(db.Integer, nullable=False)

    def __init__(self, RiderID, RiderName, VehicleNo, RiderContact, PostalCode):
        self.RiderID = RiderID
        self.RiderName = RiderName
        self.VehicleNo = VehicleNo
        self.RiderContact = RiderContact
        self.PostalCode = PostalCode

    def json(self):
        return {"RiderId" : self.RiderID, "RiderName" : self.RiderName, "VehicleNo" : self.VehicleNo, "RiderContact" : self.RiderContact, "PostalCode" : self.PostalCode}

@app.route("/rider")
def get_all():
    riderlist = Rider.query.all()
    if len(riderlist):
        return jsonify(
            {
                "code" : 200,
                "data" : {
                    "riders" : [rider.json() for rider in riderlist]
                }
            }
        )
    return jsonify(
        {
            "code" : 404,
            "message" : "There are no riders."
        }
    ),404

@app.route("/rider/<string:RiderID>")
def find_by_riderID(RiderID):
    rider = Rider.query.filter_by(RiderID = RiderID).first()
    if(rider):
        return jsonify(
            {
                "code" : 200,
                "data" : rider.json()
            }
        )
    return jsonify(
        {
            "code" : 404,
            "message" : "Rider does not exists."
        }
    ),404

@app.route("/rider/<string:RiderID>", methods=["POST"])
def create_rider(RiderID):
    if (Rider.query.filter_by(RiderID = RiderID).first()):
        return jsonify(
            {
                "code" : 400,
                "data" : {
                    "RiderID" : RiderID
                },
                "message" : "Rider already exists."
            }
        ),400
    
    data = request.get_json()
    rider = Rider(RiderID, **data)

    try:
        db.session.add(rider)
        db.session.commit()
    except:
        return jsonify(
            {
                "code" : 500,
                "data" : {
                    "RiderID" : RiderID
                },
                "message" : "An error occurred when adding a rider."
            }
        ), 500
    
    return jsonify(
        {
            "code" : 201,
            "data" : rider.json()
        }, 201
    )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)