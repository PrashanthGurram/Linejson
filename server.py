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
      "Legend":"Latitude",
      "Data":1200,
      "Label":"U.K"
   },
   {
      "Legend":"Precision",
      "Data":2400,
      "Label":"U.K"
   },
   {
      "Legend":"Optiplex",
      "Data":3600,
      "Label":"U.K"
   },
   {
      "Legend":"Precision",
      "Data":1600,
      "Label":"U.S"
   },
   {
      "Legend":"Latitude",
      "Data":2600,
      "Label":"U.S"
   },
   {
      "Legend":"Optiplex",
      "Data":3200,
      "Label":"U.S"
   },
   {
      "Legend":"Latitude",
      "Data":1700,
      "Label":"Aus"
   },
   {
      "Legend":"Optiplex",
      "Data":2500,
      "Label":"Aus"
   },
   {
      "Legend":"Precision",
      "Data":3400,
      "Label":"Aus"
   },
   {
      "Legend":"Optiplex",
      "Data":1200,
      "Label":"India"
   },
   {
      "Legend":"Precision",
      "Data":1900,
      "Label":"India"
   },
   {
      "Legend":"Latitude",
      "Data":2600,
      "Label":"India"
   }
]

    # return name and email as a JSON httpresponse using jsonify
    return jsonify(response)
# When run from command line, start the server.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
