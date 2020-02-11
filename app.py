import json, flask, os
import requests_oauthlib, requests
import random

#API KEYS
spoon_key = str(os.getenv('spoon_api_key'))
twit_key = os.getenv('twit_api_key')
twit_secret_key = str(os.getenv('twit_api_secret_key'))
twit_token = str(os.getenv('twit_api_token'))
twit_secret_token = str(os.getenv('twit_api_secret_token'))

foodurl = "https://api.spoonacular.com/recipes/random?cuisine=african?number=15&apiKey=b37e2c0b29534d18913727984e0481c9"
response = requests.get(foodurl)
json_food = response.json()

title = str(json_food['recipes'][0]['title'])
cooktime = str(json_food['recipes'][0]['readyInMinutes'])
url = str(json_food['recipes'][0]['sourceUrl'])
instructions = json_food['recipes'][0]['instructions']
ingredients_arrary = json_food['recipes'][0]["extendedIngredients"]
ingredients = []

x = random.randint(0,4)
y = random.randint(4,9)
z = random.randint(9,14)

for i in range(len(ingredients_arrary)):
    ingredients.append(ingredients_arrary[i]["original"])

twitterurl = "https://api.twitter.com/1.1/search/tweets.json?q=african%20africanfood&lang=en&result_type=mixed"
oauth = requests_oauthlib.OAuth1(
    "3KnuswndfL6QTaumOdSIinn28", 
    "zECfYUanM0TqociMqFojTYD0hoAQGU4wywERUU44Ux8CARKQZM",
    "1223247877645963265-6JO3MkFHj6sLTSpy1Htg5jcmH4FpCm",
    "grVs0ZjlduVocPsKS1FpHeUXnddD45TSc32y0RwHXdr7D"
    )
response = requests.get(twitterurl, auth=oauth)
tweets_json = response.json()

tweet1 = str(tweets_json["statuses"][x]["text"])
tweet2 = str(tweets_json["statuses"][y]["text"])
tweet3 = str(tweets_json["statuses"][z]["text"])

app = flask.Flask(__name__)
@app.route('/') 

def index(): 
    return flask.render_template(
        "index.html", 
        title = title, 
        url = url,
        tweet1 = tweet1,
        tweet2 = tweet2,
        tweet3 = tweet3,
        instructions = instructions,
        ingredients = ingredients,
        cooktime = cooktime
        )

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug = True
    )