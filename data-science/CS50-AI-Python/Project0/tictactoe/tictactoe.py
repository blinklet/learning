"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    For this problem, we’ve chosen to represent the board as a list of 
    three lists (representing the three rows of the board), where each 
    internal list contains three values that are either X, O, or EMPTY.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    The player function should take a board state as input, and return
    which player’s turn it is (either X or O).
    * In the initial game state, X gets the first move. Subsequently, the 
    player alternates with each additional move.
    * Any return value is acceptable if a terminal board is provided as 
    input (i.e., the game is already over).
    """
    
    x_player = 0
    o_player = 0
    
    for row in board:
        x_player += row.count(X)
        o_player += row.count(O)
        
    if x_player > o_player:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    * Each action should be represented as a tuple (i, j) where i corresponds 
    to the row of the move (0, 1, or 2) and j corresponds to which cell in 
    the row corresponds to the move (also 0, 1, or 2).
    * Possible moves are any cells on the board that do not already have an X 
    or an O in them.
    * Any return value is acceptable if a terminal board is provided as input.
    """
    
    all_actions = set()
    
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                all_actions.add((i,j))
    
    return all_actions
                

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    The result function takes a board and an action as input, and should 
    return a new board state, without modifying the original board.
    * If action is not a valid action for the board, your program should 
    raise an exception.
    * The returned board state should be the board that would result from 
    taking the original input board, and letting the player whose turn it 
    is make their move at the cell indicated by the input action.
    * Importantly, the original board should be left unmodified: since Minimax 
    will ultimately require considering many different board states during 
    its computation. This means that simply updating a cell in board itself 
    is not a correct implementation of the result function. You’ll likely 
    want to make a deep copy of the board first before making any changes.
    """
    
    play = player(board)  # X or O
    row, cell = action
    
    new_board = copy.deepcopy(board)
    
    if action not in actions(new_board):
        raise RuntimeError("Invalid action")
    else:
        new_board[row][cell] = play
        
    return new_board
        
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    The winner function should accept a board as input, and return the 
    winner of the board if there is one.
    * If the X player has won the game, your function should return X. 
    If the O player has won the game, your function should return O.
    * One can win the game with three of their moves in a row horizontally, 
    vertically, or diagonally.
    * You may assume that there will be at most one winner (that is, 
    no board will ever have both players with three-in-a-row, since that 
    would be an invalid board state).
    * If there is no winner of the game (either because the game is in 
    progress, or because it ended in a tie), the function should 
    return None.
    """
    
    board_size = len(board) # generalizing board size (must be square)
    
    # Is there a winner in the rows?
    rows = board
    for row in rows:
        if row.count(X) == board_size:
            return X
        elif row.count(O) == board_size:
            return O
	    
    # Is there a winner in the columns?	    
    columns = []
    for j in range(board_size):
        col = []
        for i in range(board_size):
            col.append(board[i][j])
        columns.append(col)
    for column in columns:
        if column.count(X) == board_size:
            return X
        elif column.count(O) == board_size:
            return O    
    
    # Is there a winner in the diagonals?	 
    diagonals = []
    diag = []
    for i, j in enumerate(range(board_size)):
        diag.append(board[i][j])
    diagonals.append(diag)
    diag = []
    for i, j in enumerate(reversed(range(board_size))):
        diag.append(board[i][j])
    diagonals.append(diag)    
    for diagonal in diagonals:
        if diagonal.count(X) == board_size:
            return X
        elif diagonal.count(O) == board_size:
            return O     


   
    # No winner found
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    The terminal function should accept a board as input, and return a 
    boolean value indicating whether the game is over.
    * If the game is over, either because someone has won the game or 
    because all cells have been filled without anyone winning, the 
    function should return True.
    * Otherwise, the function should return False if the game is still 
    in progress.
    """
    
    # Is board full?
    if len(actions(board)) == 0:
        return True
    
    # did someone win?
    if winner(board):
        return True
        
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    The utility function should accept a terminal board as input 
    and output the utility of the board.
    * If X has won the game, the utility is 1. If O has won the 
    game, the utility is -1. If the game has ended in a tie, 
    the utility is 0.
    * You may assume utility will only be called on a board if 
    terminal(board) is True.
    """
    
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
        

def minimax2(board):
    """
    Returns the optimal action for the current player on the board.
    The minimax function should take a board as input, and return the optimal 
    move for the player to move on that board.
    * The move returned should be the optimal action (i, j) that is one of 
    the allowable actions on the board. If multiple moves are equally optimal, 
    any of those moves is acceptable.
    * If the board is a terminal board, the minimax function should return None.
    """
    
    if terminal(board):
        score = utility(board)
        return None
    
    
    
    if player(board) == X:  # X is maximizing player
        print("XXXXX")
        value = -2
        next_board = copy.deepcopy(board)
        for action in actions(next_board):
            
        
        
        
        
            next_board = result(next_board, action)
            next_action = minimax(next_board)
            if terminal(next_board):
                continue
            else:
                next_value = max(value, utility(next_board))
                print("X Values", value, next_value)
                if next_value > value:
                    value = next_value
                    best_action = action
                    print("Best X Action", best_action)   
                return best_action        
    else: # O player is minimizing player
        print("OOOOO")
        value = 2
        next_board = copy.deepcopy(board)
        for action in actions(next_board):
            next_board = result(next_board, action)
            next_action = minimax(next_board)
            if next_action == None:
                continue
            else:
                next_value = min(value, utility(next_board))
                print("O Values", value, next_value)
                if next_value < value:
                    value = next_value
                    best_action = action
                    print("Best O Action", best_action)
                return best_action
    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    The minimax function should take a board as input, and return the optimal 
    move for the player to move on that board.
    * The move returned should be the optimal action (i, j) that is one of 
    the allowable actions on the board. If multiple moves are equally optimal, 
    any of those moves is acceptable.
    * If the board is a terminal board, the minimax function should return None.
    """
    
    def max_score(board):
    
        if terminal(board):
            score = utility(board)
            return score
            
        score = -2  # "negative infinity" is -2 in this game
        for move in actions(board):
            nextboard = result(board, move)
            score = max(score, min_score(nextboard))
        return score
    
    def min_score(board):
    
        if terminal(board):
            score = utility(board)
            return score
            
        score = 2  # "infinity" is 2 in this game
        for move in actions(board):
            nextboard = result(board, move)
            score = min(score, max_score(nextboard))
        return score
    
    print(board)
    if player(board) == X:  # maximizer
        print("XXXXX")
        score = -2  # "negative infinity" is -2 in this game
        evaluated_moves = []
        print(actions(board))
        for action in actions(board):
            next_board = result(board, action)
            next_score = min_score(next_board)
            evaluated_moves.append((next_score, action))
        print("X:   ", evaluated_moves)
        for move in evaluated_moves:
            if move[0] > score:
                score = move[0]
                best_move = move[1]
        return best_move
          
    if player(board) == O:  # minimizer
        print("OOOOO")
        score = 2  # "infinity" is 2 in this game
        evaluated_moves = []
        for action in actions(board):
            next_board = result(board, action)
            next_score = max_score(next_board)
            evaluated_moves.append((next_score, action))
        print("O:   ", evaluated_moves)
        for move in evaluated_moves:
            if move[0] < score:
                score = move[0]
                best_move = move[1]
        return best_move


def minimax5(board):
    """
    Returns the optimal action for the current player on the board.

    'X' Player is trying to maximise the score, 'O' Player is trying to minimise it
    """

    global actions_explored
    actions_explored = 0

    def max_player(board, best_min = 10):
      """ Helper function to maximise score for 'X' player.
          Uses alpha-beta pruning to reduce the state space explored.
          best_min is the best result
      """

      global actions_explored

      # If the game is over, return board value
      if terminal(board):
        return (utility(board), None)

      # Else pick the action giving the max value when min_player plays optimally
      value = -10
      best_action = None


      # Get set of actions and then select a random one until list is empty:
      action_set = actions(board)

      while len(action_set) > 0:
        action = random.choice(tuple(action_set))
        action_set.remove(action)

        # A-B Pruning skips calls to min_player if lower result already found:
        if best_min <= value:
          break

        actions_explored += 1
        min_player_result = min_player(result(board, action), value)
        if min_player_result[0] > value:
          best_action = action
          value = min_player_result[0]

      return (value, best_action)


    def min_player(board, best_max = -10):
      """ Helper function to minimise score for 'O' player """

      global actions_explored

      # If the game is over, return board value
      if terminal(board):
        return (utility(board), None)

      # Else pick the action giving the min value when max_player plays optimally
      value = 10
      best_action = None

      # Get set of actions and then select a random one until list is empty:
      action_set = actions(board)

      while len(action_set) > 0:
        action = random.choice(tuple(action_set))
        action_set.remove(action)

        # A-B Pruning skips calls to max_player if higher result already found:
        if best_max >= value:
          break

        actions_explored += 1
        max_player_result = max_player(result(board, action), value)
        if max_player_result[0] < value:
          best_action = action
          value = max_player_result[0]

      return (value, best_action)


    # If the board is terminal, return None:
    if terminal(board):
      return None

    if player(board) == 'X':
      print('AI is exploring possible actions...')
      best_move = max_player(board)[1]
      print('Actions explored by AI: ', actions_explored)
      return best_move
    else:
      print('AI is exploring possible actions...')
      best_move = min_player(board)[1]
      print('Actions explored by AI: ', actions_explored)
      return best_move
    
    
    
    
    
    
    
    
