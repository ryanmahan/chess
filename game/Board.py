from .Space import Space;
from .Player import Player;
from game.Pieces import Pawn, Rook, Bishop, Queen, King, Knight;
from game.constants import WHITE, BLACK;

def baseRow(player, x):
  pieceList = [
    Rook(player, x, 0), Knight(player, x, 1), Bishop(player, x, 2), Queen(player, x, 3),
    King(player, x, 4), Bishop(player, x, 5), Knight(player, x, 6), Rook(player, x, 7)
  ]
  return [Space(x) for x in pieceList]

def pawnRow(player, x):
  return [Space(Pawn(player, x, y)) for y in range(0, 8)]

class Board:
  players = (Player(WHITE), Player(BLACK))
  spaces = [[Space(None)]*8]*8
  def __init__(self):
    
    self.spaces = [baseRow(self.players[1], 0), pawnRow(self.players[1], 1)]
    for i in range(4):
      row = [Space(None) for x in range(8)]
      self.spaces.append(row)
    self.spaces += [pawnRow(self.players[0], 6), baseRow(self.players[0], 7)]


  def __str__(self):
    output = "";
    for row in self.spaces:
      output += "\n"
      for space in row:
        output += str(space) + "\t"
    return output;

  def setSpace(self, x, y, piece):
    print(x, y, piece, self.spaces[x][y-1].piece)
    print(self.getSpace(x, y))
    space = self.getSpace(x, y)
    space.setPiece(piece);
    return self.spaces;

  def getSpace(self, x, y):
    return self.spaces[x][y]