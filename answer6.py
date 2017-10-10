import sys

board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
board = [list(x) for x in board]


for row in range(m):
	for col in range(n):
		if board[m][n] == board[m+1][n] and board[m][n] == board[m][n+1] and board[m][n] == board[m+1][n+1]:
			board[m][n] = "EMPTY"
			board[m+1][n] = "EMPTY"
			board[m][n+1] = "EMPTY"
			board[m+1][n+1] = "EMPTY"


