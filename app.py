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
    # I have a Unique constraint on animal.name in db
    elif "Duplicate entry" in result:
        return "This animal name has already been recorded, please enter a unique animal name."

# Patch Request for Endpoint
@app.patch('/api/animals')
def patch_animal():
    new_animal_name = request.json.get('newAnimalName')
    current_animal_name = request.json.get('currentAnimalName')
    if current_animal_name == None:
        return "You must specify the animal you are updating."
    if new_animal_name == None:
        return "You must specify the updated animal name."
    result = run_statement("CALL patch_animal(?, ?)", [new_animal_name, current_animal_name])
    if result == None:
        return "Successfully updated animal name."
    else:
        return result

app.run(debug = True)