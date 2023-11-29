import json
from player import Player

players = []

with open('players.json', 'r') as file:
    data = json.load(file)
    for row in data:
        player = Player(
            row['name'],
            row['surname'],
            row['dob'],
            row['nationality'],
            row['positions'],
            row['team']
        )
        for score, value in row['scores'].items():
            player.set_attribute(score, value)

        players.append(player)