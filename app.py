from flask import Flask, request
import json
from dbhelpers import run_statement

app = Flask(__name__)

# Get Request for Endpoint
@app.get('/api/animals')
def get_animals():
    result = run_statement("CALL get_animals()")
    if (type(result) == list):
        return json.dumps(result, default=str)
    else: 
        return "Sorry, something went wrong."

# Post Request for Endpoint
@app.post('/api/animals')
def post_animal():
    animal_name = request.json.get('animalName')
    if animal_name == None:
        return "You must specify an animal name."
    result = run_statement("CALL post_animal(?)", [animal_name])
    if result == None:
        return "Successfully added animal."
    else:
        return result

app.run(debug = True)