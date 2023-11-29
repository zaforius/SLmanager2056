from tactic import create_tactics


class Team:
    next_id = 1

    def __init__(self, name, country, owner, manager):
        self.team_id = Team.next_id  # Assign the next available ID
        Team.next_id += 1  # Increment the next available ID
        self.name = name
        self.country = country
        self.owner = owner
        self.manager = manager
        self.squad = []  # Initialize as empty list
        self.balance = 1000000  # Set default balance to 1 million
        self.tactics_list = create_tactics(self.team_id)
        self.tactic = self.tactics_list[0]

    def add_player(self, player):
        """Adds a player to the team's squad."""
        self.squad.append(player)
        player.team = self  # Update player's team attribute
        player.number = max([player.number for player in self.squad]) + 1

    def remove_player(self, player):
        """Removes a player from the team's squad."""
        if player in self.squad:
            self.squad.remove(player)
            player.team = None  # Set player's team attribute to None

    def change_tactic_by_name(self, name):
        for tactic in self.tactics_list:
            if f"{self.team_id}-{name}" == tactic.name:
                self.tactic = tactic
                return
        print("Tactic with given name not found")

    def add_balance(self, amount):
        """Adds the specified amount to the team's balance."""
        self.balance += amount

    def subtract_balance(self, amount):
        """Subtracts the specified amount from the team's balance."""
        self.balance -= amount

    def display_squad(self):
        print(f"--- {self.name}'s Squad ---")
        for i, player in enumerate(self.squad):
            print(i, player)  # Assuming the Player class has a __str__ method

    def display_tactic(self):
        print(f"--- Current Tactic: {self.tactic.name[2:]} ---")

    def display_starting_11(self):
        print(f"--- Starting 11 for {self.tactic.name[2:]} ---")
        for line, players in self.tactic.starting_11.items():
            print(f"{line.capitalize()}:")
            for i, player in enumerate(players):
                print(f"  - {i} . {player}")  # Assuming the Player class has a __str__ method

    def display_substitutes(self):
        print(f"--- Substitutes for {self.tactic.name[2:]} ---")
        for i, player in enumerate(self.tactic.substitutes):
            print(f" {i} - {player}")

    def check_eleven(self):
        outfields = 0
        for line in self.tactic.starting_11.values():
            for player in line:
                outfields += 1
        return outfields == 11

    def auto_select_team(self):
        while not self.check_eleven():
            for player in self.squad:
                if len(self.tactic.starting_11["defenders"]) < int(self.tactic.name[2]):
                    if any(pos in player.positions for pos in ["DC", "DR", "DL"]):
                        self.tactic.add_player_to_line(player, "defenders")
                        continue  # Skip to next iteration

                if len(self.tactic.starting_11["midfielders"]) < int(self.tactic.name[4]):
                    if any(pos in player.positions for pos in ["CM", "MR", "ML"]):
                        self.tactic.add_player_to_line(player, "midfielders")
                        continue  # Skip to next iteration

                if len(self.tactic.starting_11["attackers"]) < int(self.tactic.name[6]):
                    if "ST" in player.positions:
                        self.tactic.add_player_to_line(player, "attackers")
                        continue  # Skip to next iteration

                if len(self.tactic.starting_11["goalkeepers"]) < 1:
                    if "GK" in player.positions:
                        self.tactic.add_player_to_line(player, "goalkeepers")
                        continue  # Skip to next iteration
            break  # Breaks the outer while loop




