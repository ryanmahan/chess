from game.Board import Board;

gameBoard = Board();
print(gameBoard);

piece = gameBoard.getSpace(7, 7).piece;
piece.move(gameBoard, 5, 7);

print(gameBoard);

piece = gameBoard.getSpace(1, 4).piece
piece.move(gameBoard, 3, 4);

print(gameBoard)