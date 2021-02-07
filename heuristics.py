import numpy as np;
import chess;
from functools import reduce

piece_value_map = {
  1: 1, # pawn
  2: 3, # knight
  3: 3, # bishop
  4: 5, # rook
  5: 9, # queen
  6: 200 # king
}

def randomHeuristic(board):
  return np.random.randint(0, 1000);

def is_on_or_attacking(board, square, player = None):
  if (player == None):
    player = board.turn;
  return player == board.color_at(square) or board.is_attacked_by(player, square)

def number_of_attacking_squares(board):
  attacking = 0
  for square in chess.SQUARES:
    attacking += len(board.attackers(board.turn, square))
  return attacking;

def piece_sum(board, player):
  piece_sum = 0
  for piece_type in piece_value_map.keys():
    piece_sum += len(board.pieces(piece_type, player)) * piece_value_map[piece_type];
  return piece_sum

def dont_die(board):
  piece_sum = 0;
  for piece_type in piece_value_map.keys():
    squares = board.pieces(piece_type, board.turn)
    for square in squares:
      if (board.is_attacked_by(not board.turn, square)):
        piece_sum += piece_value_map[piece_type];
  return piece_sum

def protect_yourself(board, player):
  protect_sum = 0;
  for piece_type in piece_value_map.keys():
    squares = board.pieces(piece_type, player);
    for square in squares:
      if (board.is_attacked_by(player, square)):
        protect_sum += piece_value_map[piece_type];
  return protect_sum;

def check(board, danger = False):
  safe_checkers = 0
  if not danger:
    for square in board.checkers():
      if not board.is_attacked_by(not board.turn, square):
        safe_checkers += piece_value_map[board.piece_at(square)]
    return safe_checkers
  else:
    return len(board.checkers());

def checkmate(board):
  if board.is_checkmate():
    return 50;
  else:
    return 0;

def central_control(board, player):
  central_control = 0
  center = [chess.parse_square(alpha + str(number)) for alpha in ["b", "c", "d", "e", "f", "g"] for number in range(4, 6)]
  for square in center:
    if (is_on_or_attacking(board, square)):
      central_control += 1;
  return central_control;

def moves(board, player):
  if (player == board.turn):
    return board.legal_moves.count()
  restore = board.pop()
  moves = board.legal_moves.count()
  board.push(restore)
  return moves;

def doubled_pawns(board, player):
  pawns = [0]*8
  for square in board.pieces(chess.PAWN, player):
    pawns[chess.square_file(square)] += 1
  return reduce(lambda x, y: y + 1 if x >= 2 else y, pawns);

def isolated_pawns(board, player):
  isolated = 0
  pawns = [0]*10
  for square in board.pieces(chess.PAWN, player):
    pawns[chess.square_file(square) + 1] = True
  for i in range(1, len(pawns) - 1):
    if (pawns[i] and (not pawns[i-1] and not pawns[i+1])):
      isolated += 1;
  return isolated;

def blocked_pawns(board, player):
  blocked_pawns = 0
  direction = 0
  if player:
    direction = 1
  else:
    direction = -1
  for square in board.pieces(chess.PAWN, player):
    if board.color_at(chess.square(chess.square_file(square), chess.square_rank(square) + direction)) != player:
      blocked_pawns += 1;
  return blocked_pawns;
    
def claude_shannon(verbose = False):
  def heuristic(board):
    result = {
      "opposing piece sum": piece_sum(board, not board.turn) * -1,
      "player piece sum": piece_sum(board, board.turn),
      "opposing doubled pawns": doubled_pawns(board, not board.turn) * .5,
      "player doubled pawns": doubled_pawns(board, board.turn) * -.5,
      "opposing isolated pawns": isolated_pawns(board, not board.turn) * .5,
      "player isolated pawns": isolated_pawns(board, board.turn) * -.5,
      "opposing blocked pawns": blocked_pawns(board, not board.turn) * .5,
      "player blocked pawns": blocked_pawns(board, board.turn) * -.5,
      "legal moves": moves(board, board.turn) * .1,
      "legal moves": moves(board, not board.turn) * -.1
    }
    # if (board.fullmove_number < 10):
    if verbose:
      print(board);
      print(result);
      print(sum(result.values()))
      
    return sum(result.values());
  return heuristic;


def custom(verbose = False):
  def heuristic(board):
    result = {
      "opposing piece sum": piece_sum(board, not board.turn) * -1,
      "player piece sum": piece_sum(board, board.turn),
      "opposing doubled pawns": doubled_pawns(board, not board.turn) * .5,
      "player doubled pawns": doubled_pawns(board, board.turn) * -.5,
      "opposing isolated pawns": isolated_pawns(board, not board.turn) * .5,
      "player isolated pawns": isolated_pawns(board, board.turn) * -.5,
      "opposing blocked pawns": blocked_pawns(board, not board.turn) * .5,
      "player blocked pawns": blocked_pawns(board, board.turn) * -.5,
      "attacking squares": number_of_attacking_squares(board) * .7,
      "death_penalty": dont_die(board) * -2,
      "check": check(board, True),
      "checkmate": checkmate(board),
      "protect yourself": protect_yourself(board, board.turn) * 1.3,
      "expose enemy": -1 * protect_yourself(board, not board.turn),
      "self central control": central_control(board, board.turn),
      "opponent central control": central_control(board, not board.turn) * .7,
      "legal moves": moves(board, board.turn) * .1
    }
    # if (board.fullmove_number < 10):
    if verbose:
      print(board);
      print(result);
      print(sum(result.values()))
      
    return sum(result.values());
  return heuristic;
