import numpy as np;
import chess;

piece_value_map = {
  1: 1, # pawn
  2: 3, # knight
  3: 3, # bishop
  4: 5, # rook
  5: 9, # queen
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

def opposing_piece_sum(board):
  piece_sum = 0
  for piece_type in piece_value_map.keys():
    piece_sum += len(board.pieces(piece_type, not board.turn)) * piece_value_map[piece_type];
  return piece_sum

def dont_die(board):
  piece_sum = 0;
  for piece_type in piece_value_map.keys():
    squares = board.pieces(piece_type, board.turn)
    for square in squares:
      if (board.is_attacked_by(not board.turn, square)):
        piece_sum += piece_value_map[piece_type];
  return piece_sum

def protect_yourself(board):
  protect_sum = 0;
  for piece_type in piece_value_map.keys():
    squares = board.pieces(piece_type, board.turn);
    for square in squares:
      if (board.is_attacked_by(board.turn, square)):
        protect_sum += piece_value_map[piece_type];
  return protect_sum;

def check(board):
  return len(board.checkers()) * 2;

def central_control(board, player):
  central_control = 0
  center = [chess.parse_square(alpha + str(number)) for alpha in ["b", "c", "d", "e", "f", "g"] for number in range(4, 6)]
  for square in center:
    if (is_on_or_attacking(board, square)):
      central_control += 1;
  return central_control;

def custom(verbose = False):
  def heuristic(board):

    opposing = opposing_piece_sum(board);
    attacking = number_of_attacking_squares(board);
    death_penalty = dont_die(board);
    result = {
      "opposing piece sum": opposing_piece_sum(board),
      "attacking squares": number_of_attacking_squares(board),
      "death_penalty": dont_die(board) * -1,
      "check": check(board),
      "protect yourself": protect_yourself(board),
      "self central control": central_control(board, board.turn),
      "opponent central control": central_control(board, not board.turn)
    }
    # if (board.fullmove_number < 10):
    if verbose:
      print(board);
      print(result);
      print(sum(result.values()))
      
    return sum(result.values());
  return heuristic;
