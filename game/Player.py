class Player:
  color = None;

  def __init__(self, color):
    self.color = color;

  def __str__(self):
    return self.color