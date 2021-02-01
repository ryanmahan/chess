
class Space:
  piece = None;
  owner = None;

  def __init__(self, piece):
    self.piece = piece;
    if (piece is not None):
      self.owner = piece.owner;

  def __str__(self):
    if (self.piece is None):
      return "[ EMPTY ]";
    else:
      return "[" + str(self.piece) + "]";

  def setPiece(self, piece):
    self.piece = piece;
    if (piece is not None):
      self.owner = piece.owner;
    else:
      self.owner = None;

def isEmpty(space):
  return (space.owner is None and space.piece is None)