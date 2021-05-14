import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=["Get"])
def predict():

    """Let's Predict the rating of the Restaurant
    This is using docstrings for specifications.
    ---
    parameters:

      - name: online_order
        in: query
        type: int
        #required: true
      - name: book_table
        in: query
        type: int
        #required: true
      - name: votes
        in: query
        type: int
        #required: true
      - name: location
        in: query
        type: int
        #required: true
      - name: rest_type
        in: query
        type: int
        #required: true
      - name: cuisines
        in: query
        type: int
        #required: true
      - name: cost
        in: query
        type: float
        #required: true
      - name: menu_item
        in: query
        type: int
        #required: true
    responses:
        200:
            description: The output values

    """


    online_order = request.args.get("online_order")
    book_table = request.args.get("book_table")
    votes = request.args.get("votes")
    location = request.args.get("location")
    rest_type = request.args.get("rest_type")
    cuisines = request.args.get("cuisines")
    cost = request.args.get("cost")
    menu_item = request.args.get("menu_item")
    prediction = model.predict([[online_order, book_table, votes, location, rest_type, cuisines, cost, menu_item]])


    output = round(prediction[0], 1)
    return "Your Rating is " + str(output)

if __name__ == "__main__":
    app.run(debug=True)


