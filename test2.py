from player import Player
from tactic import Tactic
from team import Team

from datetime import date
import random

greek_players = [
    Player("Nikos", "Papadopoulos", date(1992, 4, 15), "Greece", ["GK"]),
    Player("Giannis", "Kostas", date(1993, 7, 12), "Greece", ["DC", "DL"]),
    Player("Dimitris", "Petros", date(1995, 11, 8), "Greece", ["DC", "DR"]),
    Player("Stelios", "Stefanidis", date(1991, 5, 23), "Greece", ["DL", "DR"]),
    Player("Alexis", "Tsipras", date(1984, 9, 30), "Greece", ["CM", "ML"]),
    Player("Petros", "Anastasiou", date(1989, 12, 20), "Greece", ["CM", "MR"]),
    Player("Spiros", "Lefteris", date(1997, 6, 11), "Greece", ["CM"]),
    Player("Andreas", "Papandreou", date(1990, 8, 16), "Greece", ["CM"]),
    Player("Nikolas", "Georgiou", date(1988, 1, 9), "Greece", ["MR"]),
    Player("Kostas", "Manolas", date(1991, 6, 14), "Greece", ["ML"]),
    Player("Dimitris", "Giannoulis", date(1996, 5, 17), "Greece", ["CM", "ST"]),
    Player("Giorgos", "Karagounis", date(1977, 3, 6), "Greece", ["CM", "ST"]),
    Player("Angelos", "Basinas", date(1976, 1, 3), "Greece", ["CM"]),
    Player("Theodoros", "Zagorakis", date(1971, 10, 27), "Greece", ["CM"]),
    Player("Christos", "Tsiolis", date(1995, 5, 12), "Greece", ["ST"]),
]

grande_canton = Team(name="Grande Canton", country="Imaginary Land", owner="John Doe", manager="Jane Doe")

for player in greek_players:
    grande_canton.add_player(player)

grande_canton.display_tactic()

grande_canton.tactic.add_player_to_line(grande_canton.squad[2], "defenders")
grande_canton.tactic.add_player_to_line(grande_canton.squad[3], "defenders")
grande_canton.tactic.add_player_to_line(grande_canton.squad[4], "midfielders")
grande_canton.display_starting_11()
grande_canton.change_tactic_by_name('3-5-2')
grande_canton.display_tactic()


