class Tactic:
    next_id = 1

    def __init__(self, name, requirements):
        self.tactic_id = Tactic.next_id  # Assign the next available ID
        Tactic.next_id += 1  # Increment the next available ID
        self.name = name
        self.requirements = requirements  # {'defenders': ['DL', 'DR', 'DC', 'DC'], 'midfielders': ['ML', 'MR', 'CM', 'CM'], 'attackers': ['SC', 'SC']}
        self.starting_11 = {
            'goalkeepers': [],
            'defenders': [],
            'midfielders': [],
            'attackers': []
        }
        self.debuffs = {
            'goalkeepers': 0,
            'defenders': 0,
            'midfielders': 0,
            'attackers': 0
        }

        self.substitutes = []

    def add_player_to_line(self, player, line):
        """Add a player to a specific line in the starting 11. Here we add a check
        in case a manager try to append to an already full line"""
        player_already_in = False
        for checkline in self.starting_11.values():
            if player in checkline:
                player_already_in = True

        if player_already_in == False:
            if line in self.starting_11:
                if line == "defenders":
                    if len(self.starting_11[line]) < int(self.name[2]):
                        self.starting_11[line].append(player)
                        self.check_debuffs(line)
                        print(f"Player {player.name} {player.surname} added to {line}.")
                    else:
                            print("Sorry, this line is full")
                elif line == "midfielders":
                    if len(self.starting_11[line]) < int(self.name[4]):
                            self.starting_11[line].append(player)
                            self.check_debuffs(line)
                            print(f"Player {player.name} {player.surname} added to {line}.")
                    else:
                            print("Sorry, this line is full")
                elif line == "attackers":
                    if len(self.starting_11[line]) < int(self.name[6]):
                            self.starting_11[line].append(player)
                            self.check_debuffs(line)
                            print(f"Player {player.name} {player.surname} added to {line}.")
                    else:
                            print("Sorry, this line is full")
                else:
                    if len(self.starting_11[line]) < 1:
                            self.starting_11[line].append(player)
                            self.check_debuffs(line)
                            print(f"Player {player.name} {player.surname} added to {line}.")
                    else:
                            print("Sorry, this line is full")
        else:
            print("Player already in starting eleven")

    def remove_player_from_line(self, player, line):
        """Remove a player from a specific line in the starting 11."""
        if line in self.starting_11 and player in self.starting_11[line]:
            self.starting_11[line].remove(player)
            self.check_debuffs(line)

    def add_player_to_subs(self, player):
        """Add a player to a specific line in the starting 11."""
        if len(self.substitutes) < 7:
            if player not in self.substitutes:
                for line in self.starting_11.values():
                    if player in line:
                        self.remove_player_from_line(player, "goalkeepers")
                        self.remove_player_from_line(player, "defenders")
                        self.remove_player_from_line(player, "midfielders")
                        self.remove_player_from_line(player, "attackers")
                self.substitutes.append(player)

    def remove_player_from_subs(self, player):
        """Add a player to a specific line in the starting 11."""
        self.substitutes.remove(player)

    def check_debuffs(self, line):
        """Check if a debuff should be applied to a specific line."""
        actual_positions = [player.positions for player in self.starting_11[line]]
        required_positions = self.requirements[line]

        self.debuffs[line] = 0  # Reset debuff for the line

        for pos in required_positions:
            if sum(pos in p for p in actual_positions) < required_positions.count(pos):
                self.debuffs[line] = -2  # Apply debuff
                break  # No need to check other positions in this line once a debuff is applied

    def get_debuff(self, line):
        """Returns the debuff value for a specific line."""
        return self.debuffs.get(line, 0)

    def transfer_players_to_new_tactic(self, new_tactic):
        players_to_move_to_squad = []

        for line in ['goalkeepers', 'defenders', 'midfielders', 'attackers']:
            new_line = new_tactic.starting_11[line]
            old_line = self.tactic.starting_11[line]

            # Empty the new tactic's line
            new_line.clear()

            for player in old_line:
                # If the player's positions meet the new tactic's requirements
                if any(pos in player.positions for pos in new_tactic.requirements[line]):
                    new_line.append(player)
                else:
                    players_to_move_to_squad.append(player)

            # Re-check for debuffs in the new tactic
            new_tactic.check_debuffs(line)

        # Move players that didn't fit the new tactic back to the team's squad
        for player in players_to_move_to_squad:
            self.squad.append(player)

# Here is the implementation of some tactics


def create_tactics(team_id):
    """Create and return a list of tactics unique to the team with the given ID."""
    tactics_list = []
    tactics_list.append(Tactic(f"{team_id}-4-4-2", {"goalkeepers": ["GK"], "defenders": ["DL", "DR", "DC", "DC"], "midfielders": ["ML", "MR", "CM", "CM"], "attackers": ["SC", "SC"]}))
    tactics_list.append(Tactic(f"{team_id}-4-5-1", {"goalkeepers": ["GK"],"defenders": ["DL", "DR", "DC", "DC"], "midfielders": ["ML", "MR", "DM", "CM", "CM"], "attackers": ["SC"]}))
    tactics_list.append(Tactic(f"{team_id}-4-3-3", {"goalkeepers": ["GK"],"defenders": ["DL", "DR", "DC", "DC"], "midfielders": ["ML", "MR", "CM"], "attackers": ["SC","SC", "SC"]}))
    tactics_list.append(Tactic(f"{team_id}-5-3-2",{"goalkeepers": ["GK"],"defenders": ["DL", "DR", "DC", "DC", "DC"], "midfielders": ["ML", "MR", "CM"],"attackers": ["SC", "SC"]}))
    tactics_list.append(Tactic(f"{team_id}-3-5-2",{"goalkeepers": ["GK"],"defenders": ["DL", "DR", "DC"], "midfielders": ["ML", "MR", "CM", "CM", "CM"],"attackers": ["SC", "SC"]}))
    tactics_list.append(Tactic(f"{team_id}-5-4-1",{"goalkeepers": ["GK"],"defenders": ["DL", "DR", "DC", "DC", "DC"], "midfielders": ["ML", "MR", "CM", "CM"],"attackers": ["SC"]}))
    return tactics_list
