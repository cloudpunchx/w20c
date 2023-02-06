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

app.run(debug = True)