from flask import Flask, jsonify, request # imports objects from Flask model
import json
app = Flask(__name__) # defines the app using flask

with open('languages.json', 'r') as file: 
    data = json.load(file)

# Imports fake programing language database
languages = data["languages"]


@app.route("/", methods=['GET'])
# tests if app is working
def test():
    return jsonify({'message' : 'Programming Language API'})

""" GET REQUESTS """

@app.route("/lang", methods=['GET'])
# returns all languages in languages list
def returnLangs():
    return jsonify({'languages' : languages})


@app.route("/lang/<string:name>", methods=['GET'])
# returns a selected language from the language list based on endpoint
def returnOne(name):
    langs = [i for i in languages]
    for i in languages:
        if name == i["name"]:
            return jsonify({"language" : i})

    return jsonify({"message" : "Lanugage not found in database"}), 404

""" POST REQUESTS """

@app.route("/lang", methods=['POST'])
# Adds a Language to the language database

def addLang():
    newLang = {"name" : request.json["name"]}
    languages.append(newLang)
    return jsonify(languages)
        

if __name__ == "__main__":
    app.run(debug=True, port=8080) # runs app in debug mode