import random

##########################################################

state = []
turnN = int
turnC = ''


def chess_reset():
    # reset the state of the game / your internal variables - note that this function is highly dependent on your implementation

    global turnN
    turnN = 1
    global turnC
    turnC = 'W'
    global state
    state = list('kqbnrppppp..........PPPPPRNBQK')

def chess_boardGet():
    # return the state of the game - one example is given below - note that the state has exactly 40 or 41 characters

    strOut = ''

    strOut += str(turnN)
    strOut += ' '
    strOut += turnC
    strOut += '\n'
    strOut += ''.join(state[0:5]) + '\n'
    strOut += ''.join(state[5:10]) + '\n'
    strOut += ''.join(state[10:15]) + '\n'
    strOut += ''.join(state[15:20]) + '\n'
    strOut += ''.join(state[20:25]) + '\n'
    strOut += ''.join(state[25:30]) + '\n'

    return strOut

def chess_boardSet(strIn):
    # read the state of the game from the provided argument and set your internal variables accordingly - note that the state has exactly 40 or 41 characters

    global state
    global turnC
    global turnN

    strIn = str(strIn)
    turnn, turnC, state[0:5], state[5:10], state[10:15], state[15:20], state[20:25], state[25:30] = list(strIn.split())
    turnN = int(turnn)


def chess_winner():
    # determine the winner of the current state of the game and return '?' or '=' or 'W' or 'B' - note that we are returning a character and not a string

    if not 'k' in state:
        return 'W'
    elif not 'K' in state:
        return 'B'
    elif turnN > 40:
        return '='

    return '?'


def chess_isValid(intX, intY):
    if intX < 0:
        return False

    elif intX > 4:
        return False

    if intY < 0:
        return False

    elif intY > 5:
        return False

    return True


def chess_isEnemy(strPiece):
    # with reference to the state of the game, return whether the provided argument is a piece from the side not on move - note that we could but should not use the other is() functions in here but probably

    if turnC == 'B':
        if strPiece.isupper():
            return True
    elif turnC == 'W':
        if strPiece.islower():
            return True
    return False


def chess_isOwn(strPiece):
    # with reference to the state of the game, return whether the provided argument is a piece from the side on move - note that we could but should not use the other is() functions in here but probably

    if turnC == 'B':
        if strPiece.islower():
            return True
    elif turnC == 'W':
        if strPiece.isupper():
            return True
    return False


def chess_isNothing(strPiece):
    # return whether the provided argument is not a piece / is an empty field - note that we could but should not use the other is() functions in here but probably

    if strPiece == '.':
        return True
    return False


def chess_eval():
    # with reference to the state of the game, return the the evaluation score of the side on move - note that positive means an advantage while negative means a disadvantage

    return 0


def chess_moves():
    # with reference to the state of the game and return the possible moves - one example is given below - note that a move has exactly 6 characters

    strOut = []

    strOut.append('a5-a4\n')
    strOut.append('b5-b4\n')
    strOut.append('c5-c4\n')
    strOut.append('d5-d4\n')
    strOut.append('e5-e4\n')
    strOut.append('b6-a4\n')
    strOut.append('b6-c4\n')

    return strOut


def chess_movesShuffled():
    # with reference to the state of the game, determine the possible moves and shuffle them before returning them- note that you can call the chess_moves() function in here

    return []


def chess_movesEvaluated():
    # with reference to the state of the game, determine the possible moves and sort them in order of an increasing evaluation score before returning them - note that you can call the chess_moves() function in here

    return []


def chess_move(strIn):
    # perform the supplied move (for example 'a5-a4\n') and update the state of the game / your internal variables accordingly - note that it advised to do a sanity check of the supplied move

    global state
    global turnC
    global turnN
    column = ['a', 'b', 'c', 'd', 'e']
    c = 0

    #separate the start and end position
    start, end = list(strIn.split('-'))

    #find the column for the start position
    while column[c] != start[0]:
        c += 1

    #calculate the position in the array
    position =29-(5*(int(start[1])-1)+ (4-c))

    #Check to make sure '.' is not selected
    if chess_isNothing(state[position]):
        return False

    #Check to make sure it is our own piece
    #if str(state[position]).isupper() and turnC == 'B':
     #   return False

    if chess_isEnemy(str(state[position])):
        return False

    #save the value of the selected peice
    piece = state[position]

    #replace the start position with '.'
    state[position] = '.'

    # find the column for the end position
    c = 0
    while column[c] != end[0]:
        c += 1

    # calculate the position in the array
    position =29-(5*(int(end[1])-1)+ (4-c))

    #Check to see if replacement with queen is needed
    if position < 5 and piece == 'P':
        state[position] = 'Q'
    elif position > 24 and piece == 'p':
        state[position] = 'q'
    else:
        state[position] = piece

    #change the turn number and turn color
    if turnC == 'W':
        turnC = 'B'
    elif turnC == 'B':
        turnC = 'W'
        turnN += 1


def chess_moveRandom():
    # perform a random move and return it - one example output is given below - note that you can call the chess_movesShuffled() function as well as the chess_move() function in here

    return 'c5-c4\n'


def chess_moveGreedy():
    # perform a greedy move and return it - one example output is given below - note that you can call the chess_movesEvaluated() function as well as the chess_move() function in here

    return 'c5-c4\n'


def chess_moveNegamax(intDepth, intDuration):
    # perform a negamax move and return it - one example output is given below - note that you can call the the other functions in here

    return 'c5-c4\n'


def chess_moveAlphabeta(intDepth, intDuration):
    # perform a alphabeta move and return it - one example output is given below - note that you can call the the other functions in here

    return 'c5-c4\n'


def chess_undo():
    # undo the last move and update the state of the game / your internal variables accordingly - note that you need to maintain an internal variable that keeps track of the previous history for this

    pass
