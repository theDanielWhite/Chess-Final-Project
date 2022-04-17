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

    def valid_moves(self):
        return self.allPossibleMoves()

    def take_back(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.display[move.start_x_pos][move.start_y_pos] = move.moved_piece
            self.display[move.end_x_pos][move.end_y_pos] = move.captured_piece
            self.whiteToMove = not self.whiteToMove

    def allPossibleMoves(self):
        moves = []
        for row in range(len(self.display)):
            for col in range(len(self.display[row])):
                player_turn = self.display[row][col][0]
                if (player_turn == 'w' and self.whiteToMove) or (player_turn == 'b' and not self.whiteToMove):
                    piece = self.display[row][col][1]
                    if piece == 'P':
                        self.getPawnMoves(row, col, moves)
                    elif piece == 'R':
                        self.getRookMoves(row, col, moves)
                    elif self.display[row][col][1:3] == 'Kn':
                        self.getKnightMoves(row, col, moves)
                    elif piece == 'B':
                        self.getBishopMoves(row, col, moves)
                    elif piece == 'Q':
                        self.getQueenMoves(row, col, moves)
                    elif piece == 'K':
                        self.getKingMoves(row, col, moves)
        return moves

    def getPawnMoves(self, row, col, moves):
        if self.whiteToMove:
            if self.display[row-1][col] == "--":
                moves.append(MovePiece((row, col), (row-1, col), self.display))
                if row == 6 and self.display[row-2][col] == "--":
                    moves.append(MovePiece((row, col), (row-2, col), self.display))
            if col-1 >= 0:
                if self.display[row-1][col-1][0] == 'b':
                    moves.append(MovePiece((row, col), (row-1, col-1), self.display))
            if col+1 <= 7:
                if self.display[row-1][col+1][0] == 'b':
                    moves.append(MovePiece((row, col), (row-1, col+1), self.display))
        if not self.whiteToMove:
            if self.display[row+1][col] == "--":
                moves.append(MovePiece((row, col), (row+1, col), self.display))
                if row == 1 and self.display[row+2][col] == "--":
                    moves.append(MovePiece((row, col), (row+2, col), self.display))
            if col-1 >= 0:
                if self.display[row+1][col-1][0] == 'w':
                    moves.append(MovePiece((row, col), (row+1, col-1), self.display))
            if col+1 <= 7:
                if self.display[row+1][col+1][0] == 'w':
                    moves.append(MovePiece((row, col), (row+1, col+1), self.display))

    def getRookMoves(self, row, col, moves):
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
        enemyColor = "b" if self.whiteToMove else "w"
        for d in directions:
            for i in range(1, 8):
                final_x_pos = row + d[0] * i
                final_y_pos = col + d[1] * i
                if 0 <= final_x_pos <= 7 and 0 <= final_y_pos <= 7:
                    end_file = self.display[final_x_pos][final_y_pos]
                    if end_file == "--":
                        moves.append(MovePiece((row, col), (final_x_pos, final_y_pos), self.display))
                    elif end_file[0] == enemyColor:
                        moves.append(MovePiece((row, col), (final_x_pos, final_y_pos), self.display))
                        break
                    else:
                        break
                else:
                    break

    def getKnightMoves(self, row, col, moves):
        knightMoves = ((-2, 1), (-2, -1), (-1, -2), (1, -2), (2, 1), (2, -1), (-1, 2), (1, 2))
        allyColor = "w" if self.whiteToMove else "b"
        for m in knightMoves:
            final_x_pos = row + m[0]
            final_y_pos = col + m[1]
            if 0 <= final_x_pos <= 7 and 0 <= final_y_pos <= 7:
                end_file = self.display[final_x_pos][final_y_pos]
                if end_file[0] != allyColor:
                    moves.append(MovePiece((row, col), (final_x_pos, final_y_pos), self.display))

    def getBishopMoves(self, row, col, moves):
        directions = ((-1, 1), (-1, -1), (1, 1), (1, -1))
        enemy_color = "b" if self.whiteToMove else "w"
        for d in directions:
            for i in range(1, 8):
                final_x_pos = row + d[0] * i
                final_y_pos = col + d[1] * i
                if 0 <= final_x_pos <= 7 and 0 <= final_y_pos <= 7:
                    end_file = self.display[final_x_pos][final_y_pos]
                    if end_file == "--":
                        moves.append(MovePiece((row, col), (final_x_pos, final_y_pos), self.display))
                    elif end_file[0] == enemy_color:
                        moves.append(MovePiece((row, col), (final_x_pos, final_y_pos), self.display))
                        break
                    else:
                        break
                else:
                    break

    def getQueenMoves(self, row, col, moves):
        self.getRookMoves(row, col, moves)
        self.getBishopMoves(row, col, moves)

    def getKingMoves(self, row, col, moves):
        KingMoves = ((-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (1, -1), (1, 1))
        allyColor = "w" if self.whiteToMove else "b"
        for m in KingMoves:
            final_x_pos = row + m[0]
            final_y_pos = col + m[1]
            if 0 <= final_x_pos <= 7 and 0 <= final_y_pos <= 7:
                end_file = self.display[final_x_pos][final_y_pos]
                if end_file[0] != allyColor:
                    moves.append(MovePiece((row, col), (final_x_pos, final_y_pos), self.display))


class MovePiece:
    rowLibrary = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    inverse_rowLibrary = {rank: row for row, rank in rowLibrary.items()}  # Dictionary Comprehension, similar to list
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
        self.moveID = self.start_x_pos * 1000 + self.start_y_pos * 100 + self.end_x_pos * 10 + self.end_y_pos

    def getBoardLocation(self):
        # display moves in terminal for each piece, switch for more common notation
        return self.getRankColumn(self.start_x_pos, self.start_y_pos) + self.getRankColumn(self.end_x_pos,
                                                                                           self.end_y_pos)

    def getRankColumn(self, x, y):
        return self.inverse_colLibrary[y] + self.inverse_rowLibrary[x]

    def __eq__(self, other):
        if isinstance(other, MovePiece):
            return self.moveID == other.moveID
        return False
