import chess;
from datetime import datetime;
import numpy as np;
from heuristics import randomHeuristic, number_of_attacking_squares, opposing_piece_sum, custom;

board = chess.Board();

move = { "value": 0, "move": None}
color = chess.WHITE;
then = datetime.now()
start = datetime.now();
while board.is_game_over() is False:
  print("moves: ", board.fullmove_number)
  print("time since last move: ", datetime.now() - then);
  print("time since start: ", datetime.now() - start)
  print("current score: ", move["value"])
  print(board)
  then = datetime.now()
  move = alphabeta(board, 3, np.inf * -1, np.inf, True, custom);
  assert(board.is_legal(move["move"]))
  board.push(move["move"]);
  color = not color;
  move = alphabeta(board, 1, np.inf * -1, np.inf, False, randomHeuristic);
  assert(board.is_legal(move["move"]))
  board.push(move["move"]);
  color = not color;

print("moves: ", board.fullmove_number)
print("time since last move: ", datetime.now() - then);
print("time since start: ", datetime.now() - start)
print("current score: ", move["value"])
print(board)
print(board.result())
