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

    def makeMove(self, move):
        self.display[move.start_x_pos][move.start_y_pos] = "--"
        self.display[move.end_x_pos][move.end_y_pos] = move.moved_piece
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove


class MovePiece:
    rowLibrary = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    inverse_rowLibrary = {rank: row for row, rank in rowLibrary.items()}     # Dictionary Comprehension, similar to list
    # comprehension

    colLibrary = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    inverse_colLibrary = {letter: col for col, letter in colLibrary.items()}

    def __init__(self, start_pos, end_pos, board):
        self.start_x_pos = start_pos[0]
        self.start_y_pos = start_pos[1]
        self.end_x_pos = end_pos[0]
        self.end_y_pos = end_pos[1]
        self.moved_piece = board[self.start_x_pos][self.start_y_pos]
        self.captured_piece = board[self.end_x_pos][self.end_y_pos]

    def getBoardLocation(self):
        # display moves in terminal for each piece, switch for more common notation
        return self.getRankColumn(self.start_x_pos, self.start_y_pos) + self.getRankColumn(self.end_x_pos, self.end_y_pos)

    def getRankColumn(self, x, y):
        return self.inverse_colLibrary[y] + self.inverse_rowLibrary[x]
