"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def InitialState():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def GetPlayer(board):
    """
    Returns player who has the next turn on a board.
    """
    xCount = sum(row.count(X) for row in board)
    oCount = sum(row.count(O) for row in board)
    return X if (xCount==oCount) else O;
    

def GetActions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(x,y) for x in range(3) for y in range(3) if board[x][y] == EMPTY}

def GetResult(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not EMPTY:
        raise ValueError("Invalid Action: position occupied")
    
    newBoard = copy.deepcopy(board)
    newBoard[action[0]][action[1]] = GetPlayer(board)
    return newBoard

def GetWinner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for x in range(3):
        if board[x][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    return None

def IsTerminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if GetWinner(board) is not None:
        return True
    if all(cell is not EMPTY for row in board for cell in row):
        return True
    return False

def GetUtility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = GetWinner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    return 0

def Minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if IsTerminal(board):
        return None

    currentPlayer = GetPlayer(board)

    if currentPlayer == X:
        value, move = MaxValue(board)
    else:
        value, move = MinValue(board)

    return move

def MaxValue(board):
    """
    Helper function for Minimax, calculates max value for X.
    """
    if IsTerminal(board):
        return GetUtility(board), None

    v = -math.inf
    bestMove = None
    for action in GetActions(board):
        minVal, _ = MinValue(GetResult(board, action))
        if minVal > v:
            v = minVal
            bestMove = action
    return v, bestMove

def MinValue(board):
    """
    Helper function for Minimax, calculates min value for O.
    """
    if IsTerminal(board):
        return GetUtility(board), None

    v = math.inf
    bestMove = None
    for action in GetActions(board):
        maxVal, _ = MaxValue(GetResult(board, action))
        if maxVal < v:
            v = maxVal
            bestMove = action
    return v, bestMove