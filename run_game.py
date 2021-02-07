import chess;
from datetime import datetime;
import numpy as np;
from heuristics import claude_shannon, custom;
from alphabeta import alphabeta

board = chess.Board();

turn = lambda x: "White" if x else "Black";
then = datetime.now()
start = datetime.now();

def stats(board):
  print("moves: ", board.fullmove_number)
  print("turn: ", turn(board.turn))
  print("time since last move: ", datetime.now() - then);
  print("time since start: ", datetime.now() - start)
  print("current score: ", move["value"])
  print(board)
  then = datetime.now()

move = { "value": 0, "move": None}
color = chess.WHITE;

while board.is_game_over() is False:
  stats()
  move = alphabeta(board, 3, np.inf * -1, np.inf, True, custom(False));
  assert(board.is_legal(move["move"]))
  board.push(move["move"]);
  stats()
  move = alphabeta(board, 4, np.inf * -1, np.inf, False, claude_shannon(False));
  assert(board.is_legal(move["move"]))
  board.push(move["move"]);

stats()
