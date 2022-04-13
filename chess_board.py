# Class for Chess Board

class Board:
    def __init__(self):
        self.display = [
            ["bR", "bKn", "bB", "bQ", "bK", "bB", "bKn", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wKn", "wB", "wQ", "wK", "wB", "wKn", "wR"]
        ]
        self.whiteToMove = True
        self.moveLog = []
