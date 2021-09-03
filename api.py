from flask import Flask
from flask import jsonify
import requests
import geocoder
import json

app = Flask(__name__)


@app.route("/")
def weatherForMe():
    currentLocation = geocoder.ip('me').latlng
    response = json.loads(requests.get('https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&hourly=temperature_2m&temperature_unit=fahrenheit'.format(currentLocation[0], currentLocation[1])).text)
    times = response.get('hourly').get('time')
    temps = response.get('hourly').get('temperature_2m')
    g = geocoder.osm([currentLocation[0], currentLocation[1]], method='reverse')
    tempsTime = {}
    tempsTime['address'] = g.json['address']
    weather = {}
    for idx in range(len(times)):
        weather[times[idx]] = temps[idx]
    tempsTime['weather'] = weather
    return jsonify(tempsTime)

@app.route("/<latitude>/<longitude>")
def ecweatherForGiven(latitude,longitude):
    response = json.loads(requests.get('https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&hourly=temperature_2m&temperature_unit=fahrenheit'.format(latitude, longitude)).text)
    times = response.get('hourly').get('time')
    temps = response.get('hourly').get('temperature_2m')
    g = geocoder.osm([latitude, longitude], method='reverse')
    tempsTime = {}
    tempsTime['address'] = g.json['address']
    weather = {}
    for idx in range(len(times)):
        weather[times[idx]] = temps[idx]
    tempsTime['weather'] = weather
    return jsonify(tempsTime)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)