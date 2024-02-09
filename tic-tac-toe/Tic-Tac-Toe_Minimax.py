from random import randint
from functools import *
board = (1, 0, 0,
				0, 0, 0,
				0, 0, 0)

piece = {0 : ' ', 1 : 'X', 2 : 'O'}

def modify_board(board, pos, value):
	if pos == 0:
		return (value, ) + board[1:]
	elif pos == len(board) - 1:
		return board[:-1] + (value, )
	else:
		return board[:pos] + (value, ) + board[pos+1:]

def board_text(board):
	out ='-------------\n'
	for i in range(0, 9, 3):
		out += f'| {piece[board[i]]}'
		out += f' | {piece[board[i+1]]}'
		out += f' | {piece[board[i+2]]} |\n'
		out += f'----{i+1}---{i+2}---{i+3}\n'
	return out

def opposite_side(n):
	if n == 1:
		return 2
	else:
		return 1

def board_full(board):
	return 0 not in board

def heuristic(board, side):
	for i in range(3):
		if board[i] == board[i+3] == board[i+6] and board[i] != 0:
			if board[i] == side:
				return 1
			else:
				return -1
		if board[3*i] == board[3*i+1] == board[3*i+2] and board[3*i] != 0:
			if board[3*i] == side:
				return 1
			else:
				return -1
	if board[0] == board[4] == board[8] and board[0] != 0:
		if board[0] == side:
			return 1
		else:
			return -1
	if board[2] == board[4] == board[6] and board[2] != 0:
		if board[2] == side:
			return 1
		else:
			return -1
	return 0

def get_children(parent):
	children = []
	one = parent.count(1)
	two = parent.count(2)
	if one > two:
		marker = 2
	else:
		marker = 1
	for i in range(len(parent)):
		if parent[i] == 0:
			children.append(modify_board(parent, i, marker))
	return children

def gen_tree(board):
	global tree
	tree = dict()
	queue = [board]
	while len(queue) > 0:
		parent = queue.pop()
		if parent not in tree and heuristic(parent, 1) == 0:
			children = get_children(parent)
			tree[parent] = children
			queue += children
		elif heuristic(parent, 1) != 0:
			tree[parent] = []

heuristics = dict()
@cache
def minimax(node, do_max):
	global tree
	global heuristics
	if len(tree[node]) == 0:
		heuristics[node] = heuristic(node, 1)
		return heuristics[node]
	if do_max:
		v = [minimax(child, False) for child in tree[node]]
		heuristics[node] = max(v)
		return heuristics[node]
	else:
		v = [minimax(child, True) for child in tree[node]]
		heuristics[node] = min(v)
		return heuristics[node]

def max_child(parent):
	children = tree[parent]
	child, v = 0, -2
	for i in children:
		if (n := heuristics[i]) > v:
			child, v = i, n
	return child
		
gen_tree((0,0,0,0,0,0,0,0,0))
minimax((0,0,0,0,0,0,0,0,0), True)

print(board_text(board))
while True:
	while True:
		pos = int(input())
		if pos >= 1 and pos <= 9 and board[pos-1] == 0:
			board = modify_board(board, pos-1, 2)
			break
	board = max_child(board)
	print(board_text(board))
	if heuristic(board, 1) != 0 or 0 not in board:
		board = (0, 0, 0,
						0, 0, 0,
						0, 0, 0)
		print(board_text(board))

