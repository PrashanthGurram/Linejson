# Import nessecary parts from flask and faker to generate random    # name and email.
from flask import Flask, request, jsonify
from faker import Faker
from flask_cors import CORS
# To create and initialize a faker generator.
fake = Faker()

# Create the app object that will route our calls.
app = Flask(__name__)
CORS(app)
# Add a single endpoint that we can use as an API to accept GET and # POST requests.
@app.route("/", methods=["POST", "GET"])
def index():
    # fake to create random name and email
    # name = fake.name()
    # email = fake.email()
    response =[
   {
      "Product":"Latitude",
      "Price":1200,
      "Country":"U.K"
   },
   {
      "Product":"Precision",
      "Price":2400,
      "Country":"U.K"
   },
   {
      "Product":"Optiplex",
      "Price":3600,
      "Country":"U.K"
   },
   {
      "Product":"Precision",
      "Price":1600,
      "Country":"U.S"
   },
   {
      "Product":"Latitude",
      "Price":2600,
      "Country":"U.S"
   },
   {
      "Product":"Optiplex",
      "Price":3200,
      "Country":"U.S"
   },
   {
      "Product":"Latitude",
      "Price":1700,
      "Country":"Aus"
   },
   {
      "Product":"Optiplex",
      "Price":2500,
      "Country":"Aus"
   },
   {
      "Product":"Precision",
      "Price":3400,
      "Country":"Aus"
   },
   {
      "Product":"Optiplex",
      "Price":1200,
      "Country":"India"
   },
   {
      "Product":"Precision",
      "Price":1900,
      "Country":"India"
   },
   {
      "Product":"Latitude",
      "Price":2600,
      "Country":"India"
   }
]

    # return name and email as a JSON httpresponse using jsonify
    return jsonify(response)
# When run from command line, start the server.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')