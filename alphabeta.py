import chess;
import numpy as np;

def alphabeta(board, depth, alpha, beta, maximizing, heuristic, verbose = False):
  if depth == 0 or board.is_game_over():
    return { "value": heuristic(board), "move": board.pop() };
  move_generator = board.legal_moves;
  moves = [move for move in move_generator];
  best_move = moves[0]
  if maximizing:
    value = np.inf * -1;
    for move in moves:
      child = board.copy();
      child.push(move);
      recursive_run = alphabeta(child, depth - 1, alpha, beta, False, heuristic)
      if verbose:
        print(child, recursive_run["value"])
      if (recursive_run["value"] > value):
        value = recursive_run["value"]
        alpha = int(np.maximum(value, alpha))
        best_move = move;
      if alpha >= beta:
        break;
    return { "value": value, "move": best_move }
  else:
    value = np.inf;
    for move in moves:
      child = board.copy();
      child.push(move);
      recursive_run = alphabeta(child, depth - 1, alpha, beta, True, heuristic)
      if (recursive_run["value"] < value):
        value = recursive_run["value"]
        beta = int(np.minimum(value, beta))
        best_move = move
      if beta <= alpha:
        break;
    return { "value": value, "move": best_move };