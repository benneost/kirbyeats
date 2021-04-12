from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import paypalrestsdk

app = Flask(__name__)
CORS(app)

paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "AQClcA27CsW6PpWZAyB__9lmiJUJtCtS2YS09XtdYmw8mhm7DJQ_eSIzJaGISFXzpsKIPlS3m9wWyuNG",
  "client_secret": "EPHj1WyiI9zsoBt9fyd1zB1xpQX6Eepakn3nk5f6fAY2cebIhitbvbRKpc75nqpLyV_N-kPrs6LTpH88" })

@app.route('/')
def index():
    return render_template('payment.html')

@app.route('/payment', methods=['POST'])
def payment():

    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"},
        "redirect_urls": {
            "return_url": "http://localhost:3306/payment/execute",
            "cancel_url": "http://localhost:3306/"},
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "testitem",
                    "sku": "12345",
                    "price": "500.00",
                    "currency": "USD",
                    "quantity": 1}]},
            "amount": {
                "total": "500.00",
                "currency": "USD"},
            "description": "This is the payment transaction description."}]})

    if payment.create():
        print('Payment success!')
    else:
        print(payment.error)

    return jsonify({'paymentID' : payment.id})

@app.route('/execute', methods=['POST'])
def execute():
    success = False

    payment = paypalrestsdk.Payment.find(request.form['paymentID'])

    if payment.execute({'payer_id' : request.form['payerID']}):
        print('Execute success!')
        success = True
    else:
        print(payment.error)

    return jsonify({'success' : success})

if __name__ == '__main__':
    app.run(port=5000, debug=True)