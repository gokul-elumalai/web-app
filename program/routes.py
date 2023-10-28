import requests

from program import app
from flask import render_template, request


VALID_COLOURS = ['red', 'blue', 'yellow', 'green', 'black']

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/100Days')
def p100Days():
    return render_template('100Days.html')


@app.route('/chuck')
def chuck():
    joke = get_chuck_joke()
    return render_template('chuck.html', joke=joke)


@app.route('/advice')
def advice():
    sentence = get_advice()
    return render_template('advice.html', advice=sentence)


@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    pokemon = []

    if request.method == "POST" and 'pokecolour' in request.form:
        colour = request.form.get('pokecolour')
        if colour in VALID_COLOURS:
            pokemon = get_poke_colours(colour)
    return render_template('pokemon.html', pokemon=pokemon)


def get_chuck_joke():
    r = requests.get('https://api.chucknorris.io/jokes/random')
    data = r.json()
    return data['value']


def get_advice():
    r = requests.get('https://api.adviceslip.com/advice')
    data = r.json()
    return data['slip']['advice']


def get_poke_colours(colour):
    r = requests.get('https://pokeapi.co/api/v2/pokemon-color/' + colour.lower())
    pokedata = r.json()
    pokemons = []

    for i in pokedata['pokemon_species'][:5]:
        pokemon = {'name': i['name']}
        r1 = requests.get(i['url'])
        pokemon_stats = r1.json()
        pokemon['habitat'] = pokemon_stats['habitat']['name']
        pokemon['Legendary'] = pokemon_stats['is_legendary']

        r2 = requests.get(pokemon_stats['evolution_chain']['url'])
        evolution_stats = r2.json()['chain']['evolves_to']
        species = [i['species']['name'] for i in evolution_stats]

        pokemon['evolution'] = ' -> '.join(species)

        pokemons.append(pokemon)

    return pokemons
