import json, flask, os
import requests_oauthlib, requests
import random

foodurl = "https://api.spoonacular.com/recipes/random?cuisine=african?number=15&apiKey=b37e2c0b29534d18913727984e0481c9"
response = requests.get(foodurl)
json = response.json()

title = str(json['recipes'][0]['title'])
cooktime = str(json['recipes'][0]['readyInMinutes'])
url = str(json['recipes'][0]['sourceUrl'])
instructions = json['recipes'][0]['instructions']
ingredients_arrary = json['recipes'][0]["extendedIngredients"]
ingredients = []
x = random.randint(0,4)
y = random.randint(4,9)
z = random.randint(9,14)

for i in range(len(ingredients_arrary)):
    ingredients.append(ingredients_arrary[i]["original"])

twitterurl = "https://api.twitter.com/1.1/search/tweets.json?q=african%20africanfood&lang=en&result_type=mixed"

oauth = requests_oauthlib.OAuth1(
    "8RcjcUSIFpAZUPOs12MChqe3Y", 
    "WpPz4e8iTYEwY1aHvwcZCb3v2QdIHjfLvcwwxpRqCPHQMmv6ta",
    "1223247877645963265-Tcl68pUZcpUa6M43RMB4RuS8URIlM8",
    "G4AgehG0QbHwrNhUBuRbM7FJylLERBqrkozbVOUuRD7uK"
)

response = requests.get(twitterurl, auth=oauth)
jsonbody = response.json()
tweet1 = str(jsonbody["statuses"][x]["text"])
tweet2 = str(jsonbody["statuses"][y]["text"])
tweet3 = str(jsonbody["statuses"][z]["text"])

app = flask.Flask(__name__)
@app.route('/') 

def index(): 
    return flask.render_template(
        "index.html", 
        title = title, 
        url = url,
        instructions = instructions,
        ingredients = ingredients,
        tweet1 = tweet1,
        tweet2 = tweet2,
        tweet3 = tweet3,
        cooktime = cooktime
        )

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug = True
    )