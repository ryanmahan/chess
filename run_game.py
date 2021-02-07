import chess;
from datetime import datetime;
import numpy as np;
from heuristics import claude_shannon, custom;
from alphabeta import alphabeta

board = chess.Board();

move = { "value": 0, "move": None}
color = chess.WHITE;
then = datetime.now()
start = datetime.now();
while board.is_game_over() is False:
  print("moves: ", board.fullmove_number)
  print("turn: ", board.turn)
  print("time since last move: ", datetime.now() - then);
  print("time since start: ", datetime.now() - start)
  print("current score: ", move["value"])
  print(board)
  then = datetime.now()
  move = alphabeta(board, 3, np.inf * -1, np.inf, True, custom(False));
  assert(board.is_legal(move["move"]))
  board.push(move["move"]);
  print("moves: ", board.fullmove_number)
  print("turn: ", board.turn)
  print("time since last move: ", datetime.now() - then);
  print("time since start: ", datetime.now() - start)
  print("current score: ", move["value"])
  print(board)
  color = not color;
  move = alphabeta(board, 4, np.inf * -1, np.inf, False, claude_shannon(False));
  assert(board.is_legal(move["move"]))
  board.push(move["move"]);
  color = not color;

print("moves: ", board.fullmove_number)
print("time since last move: ", datetime.now() - then);
print("time since start: ", datetime.now() - start)
print("current score: ", move["value"])
print(board)
print(board.result())
