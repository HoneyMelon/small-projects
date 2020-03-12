class Player:
    def __init__(self, name, playing, id):
        self.name = name
        self.playing = playing
        self.id = id
        self.scored = 0
        self.full = None
        self.won = False

    def scored_ball(self):
        self.scored += 1

    def get_x_position_for_ball(self):
        x = self.scored * 30 - 10
        if self.id == 2:
            x += 380
        return x

