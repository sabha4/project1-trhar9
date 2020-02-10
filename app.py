import json, flask, os
import requests_oauthlib, requests

url = "https://api.spoonacular.com/recipes/random?apiKey=1b2c6332c94c4f27ae541fbef839174f"
response = requests.get(url)
json = response.json()

title = str(json['recipes'][0]['title'])
url = str(json['recipes'][0]['sourceUrl'])
instructions = json['recipes'][0]['analyzedInstructions'][0]['steps']
steps = []

for i in range(len(instructions)):
    steps.append(instructions[i]['step'])

app = flask.Flask(__name__)
@app.route('/') 

def index(): 
    return title

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug = True
    )