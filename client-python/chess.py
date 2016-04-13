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
    piece = ['k', 'q', 'b', 'r', 'n', 'p']
    n = 0
    point = 0
    a = 1

    while n < 30:
        if turnC == 'B':
            a = -1
        if state[n] == piece[5]:
            point -= 10*a
        elif state[n] == piece[5].upper():
            point += 10*a
        elif state[n] == piece[4]:
            point -= 1000*a
        elif state[n] == piece[4].upper():
            point += 1000*a
        elif state[n] == piece[3]:
            point -= 500*a
        elif state[n] == piece[3].upper():
            point += 500*a
        elif state[n] == piece[2]:
            point -= 200*a
        elif state[n] == piece[2].upper():
            point += 200*a
        elif state[n] == piece[1]:
            point -= 50000*a
        elif state[n] == piece[1].upper():
            point += 50000*a
        elif state[n] == piece[0]:
            point -= 1000000*a
        elif state[n] == piece[0].upper():
            point += 1000000*a
        n += 1

    return point


def chess_moves():
    # with reference to the state of the game and return the possible moves - one example is given below - note that a move has exactly 6 characters

    strOut = []
    letters = ['a', 'b', 'c', 'd', 'e']
    n = 0

    while n < 30:
        if chess_isOwn(state[n]):
            row = 6 - (n / 5)
            column = n % 5
            start = letters[column] + str(row)

            #possible moves for pawns
            if state[n] == 'P' or state[n] == 'p':
                if turnC == 'W':
                    if chess_isNothing(str(state[n - 5])):
                        end = letters[column] + str(row + 1)
                        strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(str(state[n - 4])):
                        end = letters[(column) + 1] + str(row + 1)
                        strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(str(state[n - 6])):
                        end = letters[(column) - 1] + str(row + 1)
                        strOut.append(start + '-' + end + '\n')
                elif turnC == 'B':
                    if chess_isNothing(str(state[n - 5])):
                        end = letters[column] + str(row - 1)
                        strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(str(state[n - 4])):
                        end = letters[(column) - 1] + str(row - 1)
                        strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(str(state[n - 6])):
                        end = letters[(column) + 1] + str(row - 1)
                        strOut.append(start + '-' + end + '\n')

            #possible moves for rook
            elif state[n] == 'R' or state[n] == 'r':
                #Move to right
                a = column + 1
                m = n + 1
                while a < 5 and not chess_isOwn(str(state[m])):
                    end = letters[a] + str(row)
                    strOut.append(start + '-' + end + '\n')
                    a += 1
                    m += 1
                #move to left
                a = column - 1
                m = n - 1
                while a > -1 and not chess_isOwn(str(state[m])):
                    end = letters[a] +str(row)
                    strOut.append(start + '-' + end + '\n')
                    m -= 1
                    a -= 1
                a = row + 1
                m = n - 5
                #move up
                while a < 7 and not chess_isOwn(str(state[m])):
                    end = letters[column] + str(a)
                    strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(str(state[m])):
                        a = 7
                    a += 1
                    m -= 5
                a = row - 1
                m = n + 5
                # move down
                while a > 0 and not chess_isOwn(str(state[m])):
                    end  = letters[column] + str(a)
                    strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(str(state[m])):
                         a = 0
                    a -= 1
                    m += 5

            #possible moves for knight
            elif state[n] == 'N' or state[n] == 'n':
                r = row
                a = 0
                m = n
                while a < 2:
                    #move up left and right
                    if not chess_isOwn(state[m - 11]) and r + 2 < 7 and -1 < column - 1 + (a * 2) < 5:
                        end = letters[column - 1 + (a * 2)] + str(r + 2)
                        strOut.append(start + '-' + end + '\n')
                    #move down left and right
                    if m < 16 and not chess_isOwn(state[m + 9]) and 0 < r - 2 and -1 < column - 1 + (a * 2) < 5:
                        end = letters[column - 1 + + (a * 2)] + str(r - 2)
                        strOut.append(start + '-' + end + '\n')
                    #move left and right up
                    if not chess_isOwn(state[n - 7 + (a * 4)]) and r + 1 < 7 and -1 < column - 2 + (a * 4) < 5:
                        end = letters[column - 2 + (a * 4)] + str(r + 1)
                        strOut.append(start + '-' + end + '\n')
                    #move left and right down
                    if not chess_isOwn(state[n - 7 + (a * 4)]) and 0 < r - 1 and -1 < column - 2 + (a * 4) < 5:
                        end = letters[column - 2 + (a * 4)] + str(r - 1)
                        strOut.append(start + '-' + end + '\n')
                    a += 1
                    m += 2

            #possible moves for king
            elif state[n] == 'K' or state[n] == 'k':
                a = -1
                while a < 2:
                    # move left up and down
                    if column - 1 > -1 and 0 < row + a < 7 and not chess_isOwn(state[n - 1 - (a * 5)]):
                        end = letters[column - 1] + str(row + a)
                        strOut.append(start + '-' + end + '\n')
                    #move right up and down
                    if column + 1 < 5 and 0 < row + a < 7 and not chess_isOwn(state[n + 1 - (a * 5)]):
                            end = letters[column + 1] + str(row + a)
                            strOut.append(start + '-' + end + '\n')
                    #move up and down
                    if 0 < row + a < 7 and not a == 0 and not chess_isOwn(state[n - (a * 5)]):
                            end = letters[column] + str(row + a)
                            strOut.append(start + '-' + end + '\n')
                    a += 1

            #possible moves for Bishop
            elif state[n] == 'B' or state[n] == 'b':
                a = -1
                while a < 2:
                    # move left up and down
                    if column - 1 > -1 and 0 < row + a < 7 and not chess_isOwn(state[n - 1 - (a * 5)]):
                        end = letters[column - 1] + str(row + a)
                        strOut.append(start + '-' + end + '\n')
                        # move cross
                        if not a == 0 and -1 < column - 2 and chess_isNothing(state[n - 1 - (a * 5)]) and 0 < row + (a * 2) < 7 and not chess_isOwn(state[n - 2 - (a * 10)]):
                            end = letters[column - 2] + str(row + (a * 2))
                            strOut.append(start + '-' + end + '\n')
                    # move right up and down
                    if column + 1 < 5 and 0 < row + a < 7 and not chess_isOwn(state[n + 1 - (a * 5)]):
                        end = letters[column + 1] + str(row + a)
                        strOut.append(start + '-' + end + '\n')
                        #move cross
                        if not a == 0 and chess_isNothing(state[n + 1 - (a * 5)]) and column + 2 < 5 and 0 < row + (a * 2) < 7 and not chess_isOwn(state[n + 2 - (a * 10)]):
                            end = letters[column + 2] + str(row + (a * 2))
                            strOut.append(start + '-' + end + '\n')
                    # move up and down
                    if 0 < row + a < 7 and not a == 0 and not chess_isOwn(state[n - (a * 5)]):
                        end = letters[column] + str(row + a)
                        strOut.append(start + '-' + end + '\n')
                    a += 1

            # possible moves for Queen
            elif state[n] == 'Q' or state[n] == 'Q':
                a = -1
                while a < 2 and -1 < n + 1 - (a * 5) < 30:
                    # move right up and down
                    if column + 1 < 5 and 0 < row + (a * (-1)) < 7 and not chess_isOwn(state[n + 1 - (a * 5)]):
                        end = letters[column + 1] + str(row + (a * (-1)))
                        strOut.append(start + '-' + end + '\n')
                        #move cross
                        if not a == 0 and chess_isNothing(state[n + 1 - (a * 5)]) and column + 2 < 5 and 0 < row + (a * (-2)) < 7 and chess_isOwn(state[n + 2 - (a * 10)]):
                            end = letters[column + 2] + str(row + (a * (-2)))
                            strOut.append(start + '-' + end + '\n')
                    # move left up and down
                    if column - 1 > -1 and 0 < row + (a * (-1)) < 7 and not chess_isOwn(state[n - 1 - (a * 5)]):
                        end = letters[column - 1] + str(row - (a * (-1)))
                        strOut.append(start + '-' + end + '\n')
                        #move cross
                        if not a == 0 and column - 2 and chess_isNothing(state[n - 1 - (a * 5)]) and 0 < row - (a * (-2)) < 7 and chess_isOwn(state[n - 2 - (a * 10)]):
                            end = letters[column + 2] + str(row + (a * (-2)))
                            strOut.append(start + '-' + end + '\n')
                    a += 1
                a = row + 1
                m = n - 5
                # move up
                while a < 7 and not chess_isOwn(str(state[m])):
                    end = letters[column] + str(a)
                    strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(str(state[m])):
                        a = 7
                    a += 1
                    m -= 5
                a = row - 1
                m = n + 5
                # move down
                while a > 0 and not chess_isOwn(str(state[m])):
                    end = letters[column] + str(a)
                    strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(str(state[m])):
                        a = 0
                    a -= 1
                    m += 5


        n += 1

    print strOut
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
    if str(state[position]).isupper() and turnC == 'B':
        return False

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
