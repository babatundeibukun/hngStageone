from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_SORT_KEYS']= False
data = {
  "slackUsername": "officialibk", "backend": True, "age": 26,
  "bio": "My name is Babatunde Ibukun, Nigerian, Masters student at UM6P, morocco"
}

@app.route('/',methods=['GET'])
def home_page():
    json_data= jsonify(data)
    return json_data


app.run(host='0.0.0.0', port=81)
