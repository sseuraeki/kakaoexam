import sys
import time

start_time = time.time()

assert len(sys.argv) >= 4, "Usage: python answer6.py [m] [n] [board]"

m = int(sys.argv[1]) # convert string system arg to int
n = int(sys.argv[2]) # convert string system arg to int

# convert string system arg to list
board = sys.argv[3]
if len(sys.argv) > 4:
	for i in range(4, len(sys.argv)):
		board += sys.argv[i]

board = board.split(",")
board = [x.strip("[").strip("]").strip() for x in board]

board = [list(x) for x in board]

def remove_block(board):
	target_blocks = []

	for row in range(m-1):
		for col in range(n-1):
			if board[row][col] == board[row+1][col] and board[row][col] == board[row][col+1] and board[row][col] == board[row+1][col+1] and board[row][col] != "empty":
				target_blocks.append([row,col])
				target_blocks.append([row,col+1])
				target_blocks.append([row+1,col])
				target_blocks.append([row+1,col+1])

	target_blocks = [list(x) for x in set(tuple(x) for x in target_blocks)]
	for target in target_blocks:
		row = target[0]
		col = target[1]
		board[row][col] = "ERASED"

	return board

def update_board(board):
	erased = 0
	for row in range(m):
		for col in range(n):
			if board[row][col] == "ERASED":
				if row == 0:
					board[row][col] = "empty"
				else:
					board[row][col] = board[row-1][col]
					board[row-1][col] = "empty"
				erased += 1
	return board, erased

def answer6(board):
	answer = 0
	erased = 1

	while erased > 0:
		board = remove_block(board)
		board, erased = update_board(board)
		answer += erased

	return answer

print(answer6(board))

end_time = time.time()
print(end_time - start_time, " seconds elapsed")