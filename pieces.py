# Class for the Chess Pieces: Subclasses are of each piece

class Piece:
    def __init__(self, team, role, image, alive=True):
        self.team = team
        self.type = role
        self.image = image
        self.alive = alive


    