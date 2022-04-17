# Class for Chess Gameplay

import pygame as p
import chess_board
# import chess


width = 800
height = 800
board_dimension = 8  # rows and columns of the chess board
file_size = height // board_dimension
fps = 20
game_images = {}


def image_load():
    pieces = ['wP', 'wR', 'wKn', 'wB', 'wQ', 'wK', 'bP', 'bR', 'bKn', 'bB', 'bQ', 'bK']
    for piece in pieces:
        game_images[piece] = p.transform.scale(p.image.load("Pieces/ResizedImages/" + piece + ".png"),
                                               (file_size, file_size))


def main():
    p.init()
    screen = p.display.set_mode((width, height))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    game_state = chess_board.Board()
    legalMoves = game_state.valid_moves()
    moveMade = False
    image_load()
    game_run = True
    curr_file = ()
    click_pos = []
    while game_run:
        for e in p.event.get():
            if e.type == p.QUIT:
                game_run = False
            elif e.type == p.MOUSEBUTTONDOWN:
                position = p.mouse.get_pos()
                x_pos = position[0]//file_size
                y_pos = position[1]//file_size
                if curr_file == (y_pos, x_pos):
                    curr_file = ()
                    click_pos = []
                else:
                    curr_file = (y_pos, x_pos)
                    click_pos.append(curr_file)
                if len(click_pos) == 2:
                    move = chess_board.MovePiece(click_pos[0], click_pos[1], game_state.display)
                    print(move.getBoardLocation())
                    if move in legalMoves:
                        game_state.makeMove(move)
                        moveMade = True
                        curr_file = ()
                        click_pos = []
                    else:
                        click_pos = [curr_file]
            elif e.type == p.KEYDOWN:
                if e.key == p.K_BACKSPACE:
                    game_state.take_back()
                    moveMade = True
        if moveMade:
            legalMoves = game_state.valid_moves()
            moveMade = False
        disp_game(screen, game_state)
        clock.tick(fps)
        p.display.flip()


def disp_game(screen, game_state):
    dispBoard(screen)
    dispPieces(screen, game_state.display)


def dispBoard(screen):
    board_colors = [p.Color(255, 206, 158), p.Color(209, 139, 71)]
    for row in range(board_dimension):
        for col in range(board_dimension):
            color = board_colors[((row + col) % 2)]
            p.draw.rect(screen, color, p.Rect((col * file_size), row * file_size, file_size, file_size))


def dispPieces(screen, board):
    for row in range(board_dimension):
        for col in range(board_dimension):
            piece = board[row][col]
            if piece != "--":
                screen.blit(game_images[piece], p.Rect(col * file_size, row * file_size, file_size, file_size))


if __name__ == "__main__":
    main()
