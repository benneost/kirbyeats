from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/esd-rider'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Rider(db.Model):
    __tablename__ = "rider"

    riderID = db.Column(db.Integer, unique=True, primary_key=True)
    riderName = db.Column(db.String(100), nullable=False)
    vehicleNo = db.Column(db.String(100), nullable=False)
    ridercontact = db.Column(db.Integer, nullable=False)
    postalcode = db.Column(db.Integer, nullable=False)

    def __init__(self, riderID, riderName, vehicleNo, ridercontact, postalcode):
        self.riderID = riderID
        self.riderName = riderName
        self.vehicleNo = vehicleNo
        self.ridercontact = ridercontact
        self.postalcode = postalcode

    def json(self):
        return {"RiderId" : self.riderID, "riderName" : self.riderName, "vehicleNo" : self.vehicleNo, "ridercontact" : self.ridercontact, "postalcode" : self.postalcode}

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

@app.route("/rider/<string:riderID>")
def find_by_riderID(riderID):
    rider = Rider.query.filter_by(riderID = riderID).first()
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

@app.route("/rider/<string:riderID>", methods=["POST"])
def create_rider(riderID):
    if (Rider.query.filter_by(riderID = riderID).first()):
        return jsonify(
            {
                "code" : 400,
                "data" : {
                    "riderID" : riderID
                },
                "message" : "Rider already exists."
            }
        ),400
    
    data = request.get_json()
    rider = Rider(riderID, **data)

    try:
        db.session.add(rider)
        db.session.commit()
    except:
        return jsonify(
            {
                "code" : 500,
                "data" : {
                    "riderID" : riderID
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