class Player:
    next_id = 1  # Class-level variable to keep track of the next available ID

    def __init__(self, name, surname, dob, nationality, positions, team=None):
        self.number = 0
        self.player_id = Player.next_id  # Assign the next available ID
        Player.next_id += 1  # Increment the next available ID
        self.name = name
        self.surname = surname
        self.dob = dob
        self.nationality = nationality
        self.positions = positions
        self.team = team
        self.scores = {
            'control': 10,
            'marking': 10,
            'speed': 10,
            'passing': 10,
            'technique': 10,
            'crossing': 10,
            'decisions': 10,
            'heading': 10,
            'strength': 10,
            'tackling': 10,
            'finishing': 10,
            'stamina': 10,
        }

    def set_score(self, score_name, value):
        if score_name in self.scores:
            self.scores[score_name] = value
        else:
            print(f"Invalid score name: {score_name}")

    def calculate_transfer_value(self):
        # Placeholder for calculating the transfer value of the player
        pass

    def calculate_morale(self):
        # Placeholder for calculating the morale of the player
        pass

    def __str__(self):
        positions = ', '.join(self.positions)
        return (f" {self.name}"
                f" {self.surname}"
                f" (Number: {self.number}, DOB: {self.dob},"
                f" Nationality: {self.nationality}, Positions: {positions})"
                )
