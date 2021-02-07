import chess;
from datetime import datetime;
import numpy as np;
from heuristics import randomHeuristic, number_of_attacking_squares, opposing_piece_sum, custom;
from alphabeta import alphabeta;

MODE = "DEBUG"

board = chess.Board();

player_input = input("Player color w/b\n")
player_is_white = "w" in player_input

move = { "value": 0, "move": None}
then = datetime.now()
start = datetime.now();

def get_player_move(board):
  uci_input = input("Enter your move in UCI format\n")
  if (uci_input == "eval"):
    restore = board.pop()
    for move in board.legal_moves:
      board.push(move)
      custom(True)(board);
      board.pop()
    board.push(restore)
  try:
    move = chess.Move.from_uci(uci_input);
    if (board.is_legal(move)):
      return move;
    else:
      print("illegal move, please try again")
      return get_player_move(board);
  except:
    print("invalid UCI, try again")
    return get_player_move(board);

while board.is_game_over() is False:
  print("moves: ", board.fullmove_number)
  print("time since last move: ", datetime.now() - then);
  print("time since start: ", datetime.now() - start)
  # print("current score: ", move["value"])
  print(board)

  then = datetime.now()
  if player_is_white:
    move = get_player_move(board);
  else:
    alpha_return = alphabeta(board, 4, np.inf * -1, np.inf, True, custom(False));
    move = alpha_return["move"]
  assert(board.is_legal(move))
  board.push(move)

  if not player_is_white:
    move = get_player_move(board);
  else:
    alpha_return = alphabeta(board, 4, np.inf * -1, np.inf, True, custom(False));
    move = alpha_return["move"]

  assert(board.is_legal(move))
  board.push(move);

print("moves: ", board.fullmove_number)
print("time since last move: ", datetime.now() - then);
print("time since start: ", datetime.now() - start)
# print("current score: ", move["value"])/
print(board)
print(board.result())