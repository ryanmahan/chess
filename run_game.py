from game.Board import Board;
import chess;

board = chess.Board();

print(board)
print(board.legal_moves)
moveList = [move for move in board.legal_moves];
board.push(moveList[0])
print(board)
board.pop()
print(board)