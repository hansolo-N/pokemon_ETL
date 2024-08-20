import pandas as pd
import json
from datetime import datetime
import s3fs
import os
import requests


def get_pokemon():

    pokemon = []
    print('adding pokemon to pokedex , this may take a few minutes!')

    for id in range(1,152):
        try:
            resp = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(id))
            if resp.status_code == 200:
                data = resp.json()
                pokemon.append(data)

        except:
            print("pokemon not found of id: {}".format(id))

    print('pokemon added successfully')

    return pokemon


def get_pokemon_habitats():
    pokemon_habitats = []

    print('fetching pokemon habitats, this may take a few minutes!')
    
    for id in range(1,152):
        try:
            resp = requests.get('https://pokeapi.co/api/v2/pokemon-habitat/{}'.format(id))
            if resp.status_code == 200:
                data = resp.json()
                pokemon_habitats.append(data)

        except:
            print("pokemon not found of id: {}".format(id))

    print('pokemon habitats added successfully')

    return pokemon_habitats

def get_poke_berries():
    berries = []
    print('fetching berries , this may take a few minutes!')

    for id in range(1,66):
        try:
            resp = requests.get('https://pokeapi.co/api/v2/berry/{}'.format(id))
            if resp.status_code == 200:
                data = resp.json()
                berries.append(data)

        except:
            print("berry not found of id: {}".format(id))

    print('berries added successfully')

    return berries


def filter_pokemon_data(pokemonData):
    keys = ['id', 'name', 'base_experience', 'height', 'is_default', 'order', 'weight']

    # Use dictionary comprehension to gather data
    pokemon_data = {key: [pokemon[key] for pokemon in pokemonData] for key in keys}

    # Create DataFrame directly from the dictionary
    df = pd.DataFrame(pokemon_data)
    
    return df

def filterBerries(berryData):
    keys = ['id','name','growth_time','max_harvest','natural_gift_power','size','smoothness','soil_dryness']

    berry_data = {key: [berry[key] for berry in berryData] for key in keys}

    df = pd.DataFrame(berry_data)

    return df

def createDf(getFunc,filterFunc):
    data = getFunc()  
    df = filterFunc(data)
    return df


def getAllPokeData():
    pokemon_df = createDf(getFunc=get_pokemon,filterFunc=filter_pokemon_data)
    berries_df = createDf(getFunc=get_poke_berries,filterFunc=filterBerries)

    pokemon_df.to_csv('s3://nasrsolobucket/pokemon_data.csv')
    berries_df.to_csv('s3://nasrsolobucket/pokeBerry_data.csv')



