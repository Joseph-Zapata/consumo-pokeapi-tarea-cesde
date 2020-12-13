from flask import Flask, render_template, url_for, redirect
import requests

app = Flask(__name__)
app.secret_key = "a2jia2sdi23"


@app.route('/')
def index():
    url = 'https://pokeapi.co/api/v2/pokemon'
    paramss = {'limit': '50'}

    res = requests.request('GET', url, params=paramss)
    if res.status_code == 200:
        body = res.json()
        total = body["count"]
        records = body["results"]
        return render_template('index.html', total=total, records=records)
    else:
        return render_template('error.html')


@app.route('/poke-detail/<id>')
def detail(id):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    res = requests.request('GET', url + id)
    if res.status_code == 200:
        body = res.json()
        name = body["name"]
        weight = body["weight"]
        height = body["height"]
        iden = body["id"]
        abilities = body["abilities"]
        tipo = body["types"]
        return render_template('detailed.html', name=name, weight=weight,
                               height=height, iden=iden, abilities=abilities, tipo=tipo)
    else:
        return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)
