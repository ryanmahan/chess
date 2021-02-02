from game.Space import isEmpty;
from game.constants import BLACK, WHITE;

class Piece:
  location = (None, None);
  owner = None;
  name = None;

  def __init__(self, owner, x, y):
    self.owner = owner;
    self.location = (x, y);

  def move(self, board, x, y):
    board.setSpace(x, y, self)
    board.setSpace(self.location[0], self.location[1], None)
    self.location = (x, y)

  def __str__(self):
    return str(self.owner) + " " + str(self.name);

class Pawn(Piece):
  name = "PAWN"

  def move(self, board, x, y):
    assert(isEmpty(board.getSpace(x, y)));
    if self.owner.color is BLACK:
      assert(
        x is self.location[0] + 1 or
        self.location[0] is 1 and x is self.location[0] + 2
      )
    elif self.owner.color is WHITE:
      assert(
        x is self.location[0] - 1 or
        self.location[0] is 6 and x is self.location[0] - 2
      )
    super().move(board, x, y);

class Rook(Piece):
  name = "ROOK"

  def move(self, board, x, y):
    assert(self.location[0] is x or self.location[1] is y)
    super().move(board, x, y)

class Bishop(Piece):
  name = "BISHOP"

  def move(self, board, x, y):
    assert(self.location[0] - x is self.location[1] - y)
    # if (self.location[0] is not x):
      # TODO: ROOK CANT MOVE THROUGH PIECES
      # TODO: NEITHER CAN QUEEN
      # TODO: They can land on pieces though
    super().move(board, x, y)

class Knight(Piece):
  name = "KNIGHT"

  def move(self, board, x, y):
    x_displacement = abs(self.location[0] - x)
    y_displacement = abs(self.location[1] - y)
    assert(
      (x_displacement is 2 and y_displacement is 1) or
      (x_displacement is 1 and y_displacement is 2)
    )
    super().move(board, x, y)

class King(Piece):
  name = "KING"

  def move(self, board, x, y):
    displacement = self.location[0] - x + self.location[1] - y
    assert(displacement >= -2 and displacement <= 2)
    super().move(board, x, y)

class Queen(Piece):
  name = "QUEEN"

  def move(self, board, x, y):
    assert(
      self.location[0] is x or
      self.location[1] is y or 
      (self.location[0] - x is self.location[1] - y)
    )
    super().move(board, x, y);
