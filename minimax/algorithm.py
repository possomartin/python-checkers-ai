from copy import deepcopy
import pygame

RED = (255,0,0)
WHITE = (255, 255, 255)

def minimax(position, depth, max_player, game):
    #we set the color depending on the parameter
    if max_player == RED:
        player_color = RED
    else:
        player_color = WHITE    

    if depth == 0 or position.winner() != None: # We use until depth of 0 to calculate the best play
        return position.evaluate(), position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        #print('All Moves >', get_all_moves(position, player_color, game))
        for move in get_all_moves(position, player_color, game):
            evaluation = minimax(move, depth-1, False, game)[0] #we get minEvaluation value for the best move
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        #print('All Moves >', get_all_moves(position, player_color, game))
        for move in get_all_moves(position, player_color, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        return minEval, best_move


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game): # we get all valid moves from each piece, then we store all posibles moves from board to an array
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        #print('Valid Moves', valid_moves)
        for move, skip in valid_moves.items():
            draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves


def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    #board.draw(game.win)
    #pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
    #game.draw_valid_moves(valid_moves.keys())
    #pygame.display.update()
    #pygame.time.delay(100)