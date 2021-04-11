import paypalrestsdk
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#telling paypal who you are - clientID is what you get from the dashboard
paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "AQClcA27CsW6PpWZAyB__9lmiJUJtCtS2YS09XtdYmw8mhm7DJQ_eSIzJaGISFXzpsKIPlS3m9wWyuNG",
  "client_secret": "EPHj1WyiI9zsoBt9fyd1zB1xpQX6Eepakn3nk5f6fAY2cebIhitbvbRKpc75nqpLyV_N-kPrs6LTpH88" })

@app.route('/')
def index():
    return render_template('payment.html')

@app.route('/payment', methods=['POST'])
def payment():

    # paypalrestsdk.configure({
    # "mode": "sandbox", # sandbox or live
    # "client_id": "EBWKjlELKMYqRNQ6sYvFo64FtaRLRR5BdHEESmha49TM",
    # "client_secret": "EO422dn3gQLgDbuwqTjzrFgFtaRLRR5BdHEESmha49TM" })

    payment = paypalrestsdk.Payment({
    "intent": "sale",
    "payer": {
        "payment_method": "credit_card",
        "funding_instruments": [{
        "credit_card": {
            "type": "visa",
            "number": "4417119669820331",
            "expire_month": "11",
            "expire_year": "2018",
            "cvv2": "874",
            "first_name": "Joe",
            "last_name": "Shopper" }}]},
    "transactions": [{
        "item_list": {
        "items": [{
            "name": "item",
            "sku": "item",
            "price": "1.00",
            "currency": "USD",
            "quantity": 1 }]},
        "amount": {
        "total": "1.00",
        "currency": "USD" },
        "description": "This is the payment transaction description." }]})
    
    if payment.create():
        print('Payment Sucess!')
    else:
        print(payment.error)
    
    return jsonify({'paymentID': payment.id})

@app.route('/execute', methods=['POST'])
def execute():
    success = False
    payment = paypalrestsdk.Payment.find(request.form['paymentID'])

    if payment.execute({'payer_id': request.form['payerID']}):
        print('Execute success')
        success = True
    else:
        print(payment.error)
    return jsonify({'success':success})

    if payment.create():
        print("Payment created successfully")
    else:
        print(payment.error)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
