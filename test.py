from player import Player
from team import Team

from datetime import date
import random

def random_scores():
    return {
        'control': random.randint(1, 20),
        'marking': random.randint(1, 20),
        'speed': random.randint(1, 20),
        'passing': random.randint(1, 20),
        'technique': random.randint(1, 20),
        'crossing': random.randint(1, 20),
        'decisions': random.randint(1, 20),
        'heading': random.randint(1, 20),
        'strength': random.randint(1, 20),
        'tackling': random.randint(1, 20),
        'finishing': random.randint(1, 20),
        'stamina': random.randint(1, 20),
    }

# List of 15 Greek Players
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

# Assigning random scores to each player
for player in greek_players:
    player.scores = random_scores()


grande_canton = Team(name="Grande Canton", country="Imaginary Land", owner="John Doe", manager="Jane Doe")

for player in greek_players:
    grande_canton.add_player(player)

grande_canton.display_squad()
print("\n")
grande_canton.display_tactic()
print("\n")
grande_canton.display_starting_11()
print("\n")
grande_canton.display_substitutes()
print("\n")

def manage_team(team):
    while True:
        print("\nManagement Menu:")
        print("1. Add players to the starting eleven")
        print("2. Add player to the substitutes")
        print("3. Remove players from the squad")
        print("4. Remove from substitutes")
        print("5. Change tactic")
        print("6. View starting 11")
        print("7. View substitutes")
        print("8. Remove from the starting eleven")
        print("9. Return to previous menu")

        choice = input("Choose an option: ")

        if choice == '1':
            while True:
                print("\n--- Add Players to Starting Eleven ---")
                team.display_squad()
                print("-"*20)
                print("\n")
                print("Current starting eleven \n")
                team.display_starting_11()
                print("\n")

                player_index_input = input(
                    "Choose players by index, separate multiple options by ',' or"
                    " type -1 to auto-select team, enter 'B' to go back: ")

                if player_index_input.lower() == 'b':
                    break

                player_list = player_index_input.split(',')
                for player_index_str in player_list:
                    try:
                        player_index = int(player_index_str)
                    except ValueError:
                        print("Invalid input. Please enter a numerical index.")
                        continue

                    if 0 <= player_index < len(team.squad):
                        player = team.squad[player_index]
                        while True:
                            print("\nWhich line do you want to add the player?")
                            lines = list(team.tactic.starting_11.keys())
                            for i, line in enumerate(lines):
                                print(f"{i + 1}. {line.capitalize()}")

                            line_index_input = input("Choose a line by index or 'B' to go back: ")
                            if line_index_input.lower() == 'b':
                                break

                            try:
                                line_index = int(line_index_input) - 1
                            except ValueError:
                                print("Invalid input. Please enter a numerical index.")
                                continue

                            if 0 <= line_index < len(lines):
                                line = lines[line_index]
                                team.tactic.add_player_to_line(player, line)

                                break
                            else:
                                print("Invalid line index.")
                    elif player_index == -1:
                        team.auto_select_team()
                        print("Auto complete ready, press b to go back")
                        player_index_input = input()
                        if player_index_input == 'b':
                            break
                    else:
                        print("Invalid player index.")


        elif choice == '2':

            while True:

                print("\n--- Add Player to Substitutes ---")

                team.display_squad()

                player_index_input = input("Choose a player by index or enter 'B' to go back: ")

                if player_index_input.lower() == 'b':
                    break

                try:

                    player_index = int(player_index_input)

                except ValueError:

                    print("Invalid input. Please enter a numerical index.")

                    continue

                if 0 <= player_index < len(team.squad):

                    player = team.squad[player_index]

                    team.tactic.add_player_to_subs(player)

                    print(f"Player {player.name} {player.surname} added to substitutes.")

                    break

                elif player_index == -1:

                    for player in team.squad:
                        presence = False
                        for line in team.tactic.starting_11.values():
                            if player in line:
                                presence = True
                        if presence == False:
                            team.tactic.add_player_to_subs(player)





                else:

                    print("Invalid player index.")


        elif choice == '3':

            while True:

                print("\n--- Remove Players from the squad ---")

                team.display_squad()

                player_index_input = input("Choose a player by index or enter 'B' to go back: ")

                if player_index_input.lower() == 'b':
                    break

                try:

                    player_index = int(player_index_input) - 1

                except ValueError:

                    print("Invalid input. Please enter a numerical index.")

                    continue

                if 0 <= player_index < len(team.squad):

                    player = team.squad.pop(player_index)

                    print(f"Player {player.name} {player.surname} removed from the squad.")

                    break

                else:

                    print("Invalid player index.")


        elif choice == '4':

            while True:

                print("\n--- Remove from Substitutes ---")

                team.display_substitutes()

                player_index_input = input("Choose a player by index or enter 'B' to go back: ")

                if player_index_input.lower() == 'b':
                    break

                try:

                    player_index = int(player_index_input) - 1

                except ValueError:

                    print("Invalid input. Please enter a numerical index.")

                    continue

                if 0 <= player_index < len(team.tactic.substitutes):

                    player = team.tactic.substitutes.pop(player_index)

                    print(f"Player {player.name} {player.surname} removed from substitutes.")

                    break

                else:

                    print("Invalid player index.")


        elif choice == '5':

            while True:

                print("\n--- Change Tactic ---")

                for i, tactic in enumerate(team.tactics_list):
                    print(f"{i + 1}. {tactic.name[2:]}")

                tactic_index_input = input("Choose a tactic by index or enter 'B' to go back: ")

                if tactic_index_input.lower() == 'b':
                    break

                try:

                    tactic_index = int(tactic_index_input) - 1

                except ValueError:

                    print("Invalid input. Please enter a numerical index.")

                    continue

                if 0 <= tactic_index < len(team.tactics_list):
                    # i neede to pass the tactic name with slicing because
                    # tactic change method takes the name like "4-4-2" but
                    # the actual tactic name is "team_id-4-4-2"
                    team.change_tactic_by_name(team.tactics_list[tactic_index].name[2:])

                    print(f"Tactic changed to {team.tactics_list[tactic_index].name[2:]}.")

                    break

                else:

                    print("Invalid tactic index.")


        elif choice == '6':

            while True:

                print("\n--- View Starting 11 ---")

                team.display_starting_11()
                print("\n")
                if team.check_eleven():
                    print("First team is full ")
                else:
                    print("!Positions in first team still available! ")

                go_back = input("Press 'B' to go back to the main menu or any other key to refresh: ")

                if go_back.lower() == 'b':
                    break


        elif choice == '7':

            while True:

                print("\n--- View Substitutes ---")

                team.display_substitutes()

                go_back = input("Press 'B' to go back to the main menu or any other key to refresh: ")

                if go_back.lower() == 'b':
                    break


        elif choice == '8':

            while True:

                print("\n--- Remove from the starting eleven ---")

                team.display_starting_11()

                selected_line = input(
                    "Select a line, 'G' for goalkeepers, 'D' for defenders, 'M' for midfielders, 'A' for attackers or 'B' to go back: ")

                if selected_line.lower() == 'b':
                    break

                if selected_line.lower() == 'g':

                    cline = 'goalkeepers'

                elif selected_line.lower() == 'd':

                    cline = 'defenders'

                elif selected_line.lower() == 'm':

                    cline = 'midfielders'

                elif selected_line.lower() == 'a':

                    cline = 'attackers'

                else:

                    print("Invalid option. Try again.")

                    continue

                player_index_input = input("Choose player index or 'B' to go back: ")

                if player_index_input.lower() == 'b':
                    continue

                try:

                    player_index = int(player_index_input)

                except ValueError:

                    print("Invalid input. Please enter a numerical index.")

                    continue

                if 0 <= player_index < len(team.tactic.starting_11[cline]):

                    team.tactic.remove_player_from_line(team.tactic.starting_11[cline][player_index], cline)

                    print("Player removed successfully.")

                    break

                else:

                    print("Invalid index. Try again.")

        elif choice == '9':
            print("Returning to the previous menu.")
            break

        else:
            print("Invalid choice. Please try again.")

manage_team(grande_canton)