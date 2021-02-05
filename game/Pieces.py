from game.Space import isEmpty;
from game.constants import BLACK, WHITE;
from functools import reduce;

class Piece:
  location = (None, None);
  owner = None;
  name = None;

  def __init__(self, owner, x, y):
    self.owner = owner;
    self.location = (x, y);

  def move(self, board, x, y):
    assert(self.can_move(board, x, y));
    board.setSpace(x, y, self)
    board.setSpace(self.location[0], self.location[1], None)
    self.location = (x, y)

  def can_move(self, board, x, y):
    return (self.location[0] is not x 
      and self.location[1] is not y);

  def __str__(self):
    return str(self.owner) + " " + str(self.name);

class Pawn(Piece):
  name = "PAWN"

  def can_move(self, board, x, y):
    return (
      isEmpty(board.getSpace(x, y))
      and super().can_move(board, x, y)
      and (
        (self.owner.color is BLACK 
          and (x is self.location[0] + 1
            or (self.location[0] is 1
              and x is self.location[0] + 2
            )
          )
        )
          or
        (self.owner.color is WHITE
          and (x is self.location[0] - 1
            or (self.location[0] is 6 
              and x is self.location[0] - 2
            )
          )
        )
      ) 
    );
  
  def get_possible(self, board):
    if (self.owner.color is BLACK):
      return [(x, self.location[1]) for self.location[0] + x in range(0, 2) if self.can_move(board, x, self.location[1])]
    else:
      return [(x, self.location[1]) for self.location[0] - x in range(0, 2) if self.can_move(board, x, self.location[1])]


class Rook(Piece):
  name = "ROOK"

  def can_move(self, board, x, y):
    if not super().can_move(self, board, x, y):
      return False;
    # linear movement test
    if not (self.location[0] is x or self.location[1] is y):
      return False;
    x_displacement = abs(x - self.location[0])
    y_displacement = abs(y - self.location[1])

    if (x_displacement is not 0):
      direction = (x - self.location[0])/x_displacement;
      return reduce(
        lambda x, y: x and y,
        [isEmpty(board.getSpace(check, self.location[1])) for check in range(self.location[0], abs(x - self.location[0]), direction)]
      );
    elif (y_displacement is not 0):
      direction = (y - self.location[1])/y_displacement;
      return reduce(
        lambda x, y: x and y, 
        [isEmpty(board.getSpace(check, self.location[1])) for check in range(self.location[0], abs(y - self.location[1]), direction)]
      );

class Bishop(Piece):
  name = "BISHOP"

  def can_move(self, board, x, y):
    if not (super().can_move(board, x, y)):
      return False;
    # diagonal movement test
    if not abs(self.location[0] - x) is not abs(self.location[1] - y):
      return False;

    x_displacement = abs(x - self.location[0])
    y_displacement = abs(y - self.location[1])
    x_direction = (x - self.location[0])/x_displacement;
    y_direction = (y - self.location[1])/y_displacement;

    occupied = [isEmpty(board.getSpace(x, y)) for x, y in list(zip(range(self.location[0], x_displacement, x_direction), range(self.location[1], y_displacement, y_direction)))]
    return reduce(lambda x, y: x and y, occupied);

  def move(self, board, x, y):
    assert(self.can_move(board, x, y))
      # TODO: NEITHER CAN QUEEN
      # TODO: They can land on pieces though
    super().move(board, x, y)

class Knight(Piece):
  name = "KNIGHT"

  def can_move(self, board, x, y):
    if not (super().can_move(board, x, y)):
      return False;

    x_displacement = abs(self.location[0] - x)
    y_displacement = abs(self.location[1] - y)
    return (
      (x_displacement is 2 and y_displacement is 1)
      or (x_displacement is 1 and y_displacement is 2)
    )

  def move(self, board, x, y):
    assert(self.can_move(board, x, y));
    super().move(board, x, y)

class King(Piece):
  name = "KING"

  def can_move(self, board, x, y):
    # TODO check for checks/checkmates
    displacement = self.location[0] - x + self.location[1] - y
    return displacement >= -2 and displacement <= 2

class Queen(Piece):
  name = "QUEEN"

  def move(self, board, x, y):
    assert(
      self.location[0] is x or
      self.location[1] is y or 
      (self.location[0] - x is self.location[1] - y)
    )
    super().move(board, x, y);

  def can_move(self, board, x, y):
    if not (self.location[0] is x
        or self.location[1] is y
        or (self.location[0] - x is self.location[1] - y)):
        return False;
    
    x_displacement = abs(self.location[0] - x)
    y_displacement = abs(self.location[1] - y)
    x_direction = (x - self.location[0])/x_displacement;
    y_direction = (y - self.location[1])/y_displacement;

    # x movement
    if (x_displacement is not 0 and y_displacement is 0):
      direction = (x - self.location[0])/x_displacement;
      return reduce(
        lambda x, y: x and y,
        [isEmpty(board.getSpace(check, self.location[1])) for check in range(self.location[0], x_displacement, direction)]
      );
    # y movement
    elif (y_displacement is not 0 and x_displacement is 0):
      direction = (y - self.location[1])/y_displacement;
      return reduce(
        lambda x, y: x and y, 
        [isEmpty(board.getSpace(check, self.location[1])) for check in range(self.location[0], y_displacement, direction)]
      );
    # diagonal movement
    else:
      occupied = [isEmpty(board.getSpace(x, y)) for x, y in list(zip(range(self.location[0], x_displacement, x_direction), range(self.location[1], y_displacement, y_direction)))]
      return reduce(lambda x, y: x and y, occupied);
