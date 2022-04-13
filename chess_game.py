# Class for Chess Gameplay

import pygame as p
import chess_board


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
    image_load()
    game_run = True
    while game_run:
        for e in p.event.get():
            if e.type == p.QUIT:
                game_run = False
            elif e.type == p.MOUSEBUTTONDOWN:
                position = p.mouse.get_pos()

        disp_game(screen, game_state)
        clock.tick(fps)
        p.display.flip()


def disp_game(screen, game_state):
    dispBoard(screen)
    dispPieces(screen, game_state.display)


def dispBoard(screen):
    board_colors = [p.Color(255, 228, 196), p.Color(205, 133, 63)]
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
