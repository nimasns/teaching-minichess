import random
import time
##########################################################

#board
state = []
#turn count
turnN = int
#turn color
turnC = ''
#move made array
mLog = []
#hit log
mPlog = []
#number of the moves made
mlCounter = -1
#Undo flag
mlFlag = 0
#p transition to q
PtoQlog = []
#timelimit
timelimit = 0
timecounter = 0
timecache = 0

def chess_reset():
    # reset the state of the game / your internal variables - note that this function is highly dependent on your implementation

    global turnN
    turnN = 1
    global turnC
    turnC = 'W'
    global state
    state = list('kqbnrppppp..........PPPPPRNBQK')
    global mLog
    mLog = []
    global mPlog
    mPlog = []
    global mlCounter
    mlCounter = -1
    global mlFlag
    mlFlag = 0
    global PtoQlog
    PtoQlog = []
    global timecounter
    timecounter = 0
    global timelimit
    timelimit = 0

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
    global mLog
    global mPlog
    global mlCounter
    global mlFlag
    global PtoQlog
    mLog = []
    mPlog = []
    mlCounter = -1
    mlFlag = 0
    PtoQlog = []
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
            point -= 1*a
        elif state[n] == piece[5].upper():
            point += 1*a
        elif state[n] == piece[4]:
            point -= 5*a
        elif state[n] == piece[4].upper():
            point += 5*a
        elif state[n] == piece[3]:
            point -= 10*a
        elif state[n] == piece[3].upper():
            point += 10*a
        elif state[n] == piece[2]:
            point -= 20*a
        elif state[n] == piece[2].upper():
            point += 20*a
        elif state[n] == piece[1]:
            point -= 50*a
        elif state[n] == piece[1].upper():
            point += 50*a
        elif state[n] == piece[0]:
            point -= 100*a
        elif state[n] == piece[0].upper():
            point += 100*a
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
                    if chess_isNothing(state[n - 5]):
                        end = letters[column] + str(row + 1)
                        strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(state[n - 4]) and (n - 4) % 5 == column + 1:
                        end = letters[column + 1] + str(row + 1)
                        strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(state[n - 6]) and (n - 6) % 5 == column - 1:
                        end = letters[column - 1] + str(row + 1)
                        strOut.append(start + '-' + end + '\n')
                elif turnC == 'B':
                    if chess_isNothing(state[n + 5]):
                        end = letters[column] + str(row - 1)
                        strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(state[n + 4]) and (n + 4) % 5 == column - 1:
                        end = letters[column - 1] + str(row - 1)
                        strOut.append(start + '-' + end + '\n')
                    if n + 6 < 30 and chess_isEnemy(state[n + 6]) and (n + 6) % 5 == column + 1:
                        end = letters[column + 1] + str(row - 1)
                        strOut.append(start + '-' + end + '\n')

            #possible moves for rook
            elif state[n] == 'R' or state[n] == 'r':
                #Move to right
                a = column + 1
                m = n + 1
                while a < 5 and not chess_isOwn(state[m]):
                    end = letters[a] + str(row)
                    strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(state[m]):
                        a = 5
                    a += 1
                    m += 1
                #move to left
                a = column - 1
                m = n - 1
                while a > -1 and not chess_isOwn(state[m]):
                    end = letters[a] +str(row)
                    strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(state[m]):
                        a = 0
                    m -= 1
                    a -= 1
                a = row + 1
                m = n - 5
                #move up
                while a < 7 and not chess_isOwn(state[m]):
                    end = letters[column] + str(a)
                    strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(state[m]):
                        a = 7
                    a += 1
                    m -= 5
                a = row - 1
                m = n + 5
                # move down
                while a > 0 and not chess_isOwn(state[m]):
                    end  = letters[column] + str(a)
                    strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(state[m]):
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
                    if m < 21 and not chess_isOwn(state[m + 9]) and 0 < r - 2 and -1 < column - 1 + (a * 2) < 5:
                        end = letters[column - 1 + (a * 2)] + str(r - 2)
                        strOut.append(start + '-' + end + '\n')
                    #move left and right up
                    if not chess_isOwn(state[n - 7 + (a * 4)]) and r + 1 < 7 and -1 < column - 2 + (a * 4) < 5:
                        end = letters[column - 2 + (a * 4)] + str(r + 1)
                        strOut.append(start + '-' + end + '\n')
                    #move left and right down
                    if n + 7 - (a * 4) < 30 and not chess_isOwn(state[n + 7 - (a * 4)]) and 0 < r - 1 and -1 < column + 2 - (a * 4) < 5:
                        end = letters[column + 2 - (a * 4)] + str(r - 1)
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
                        if a == 0:
                            if not chess_isEnemy(state[n - 1 - (a * 5)]):
                                end = letters[column - 1] + str(row + a)
                                strOut.append(start + '-' + end + '\n')
                        else:
                            end = letters[column - 1] + str(row + a)
                            strOut.append(start + '-' + end + '\n')
                        # move cross
                        m = n - 2 - (a * 10)
                        while not a == 0 and chess_isNothing(state[m + 1 + (a * 5)]) and -1 < m < 30 and m % 5 < column:
                            if not chess_isOwn(state[m]) and 6 - (m / 5) > 0:
                                end = letters[m % 5] + str(6 - (m / 5))
                                strOut.append(start + '-' + end + '\n')
                            if chess_isEnemy(state[m]):
                                m == 0
                            m = m - 1 - (a * 5)
                    # move right up and down
                    if column + 1 < 5 and 0 < row + a < 7 and not chess_isOwn(state[n + 1 - (a * 5)]):
                        if a == 0:
                            if not chess_isEnemy(state[n + 1 - (a * 5)]):
                                end = letters[column + 1] + str(row + a)
                                strOut.append(start + '-' + end + '\n')
                        else:
                            end = letters[column + 1] + str(row + a)
                            strOut.append(start + '-' + end + '\n')
                        #move cross
                        m = n + 2 - (a * 10)
                        while not a == 0 and chess_isNothing(state[m - 1 + (a * 5)]) and m < 30 and m % 5 > column:
                            if not chess_isOwn(state[m]) and 6 - (m / 5) < 7 :
                                end = letters[m % 5] + str(6 - (m / 5))
                                strOut.append(start + '-' + end + '\n')
                            if chess_isEnemy(state[m]):
                                m == 100
                            m = m + 1 - (a * 5)
                    # move up and down
                    if 0 < row + a < 7 and not a == 0 and chess_isNothing(state[n - (a * 5)]):
                        end = letters[column] + str(row + a)
                        strOut.append(start + '-' + end + '\n')
                    a += 1

            # possible moves for Queen
            elif state[n] == 'Q' or state[n] == 'q':
                a = -1
                while a < 2:
                    # move left up and down
                    if column - 1 > -1 and 0 < row + a < 7 and not chess_isOwn(state[n - 1 - (a * 5)]):
                        end = letters[column - 1] + str(row + a)
                        strOut.append(start + '-' + end + '\n')
                        # move cross
                        m = n - 2 - (a * 10)
                        while not a == 0 and chess_isNothing(state[m + 1 + (a * 5)]) and -1 < m < 30 and m % 5 < column:
                            if not chess_isOwn(state[m]) and 6 - (m / 5) > 0:
                                end = letters[m % 5] + str(6 - (m / 5))
                                strOut.append(start + '-' + end + '\n')
                            if chess_isEnemy(state[m]):
                                m == 0
                            m = m - 1 - (a * 5)
                        m = n - 2
                        #Move left all the way
                        while a == 0 and chess_isNothing(state[m + 1]) and -1 < m and m % 5 < column:
                            if not chess_isOwn(state[m]):
                                end = letters[m % 5] + str(row)
                                strOut.append(start + '-' + end + '\n')
                            if chess_isEnemy(state[m]):
                                m == 0
                            m -= 1
                    # move right up and down
                    if  column + 1 < 5 and 0 < row + a < 7 and not chess_isOwn(state[n + 1 - (a * 5)]):
                        end = letters[column + 1] + str(row + a)
                        strOut.append(start + '-' + end + '\n')
                        #move cross
                        m = n + 2 - (a * 10)
                        while not a == 0 and chess_isNothing(state[m - 1 + (a * 5)]) and m < 30 and m % 5 > column:
                            if not chess_isOwn(state[m]) and 6 - (m / 5) < 7:
                                end = letters[m % 5] + str(6 - (m / 5))
                                strOut.append(start + '-' + end + '\n')
                            if chess_isEnemy(state[m]):
                                m == 100
                            m = m + 1 - (a * 5)
                        m = n + 2
                        #move right all the way
                        while a == 0 and chess_isNothing(state[m - 1]) and m < 30 and m % 5 > column:
                            if not chess_isOwn(state[m]):
                                end = letters[m % 5] + str(6 - (n / 5))
                                strOut.append(start + '-' + end + '\n')
                            if chess_isEnemy(state[m]):
                                m == 30
                            m += 1
                    a += 1
                a = row + 1
                m = n - 5
                # move up
                while a < 7 and not chess_isOwn(state[m]):
                    end = letters[column] + str(a)
                    strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(state[m]):
                        a = 7
                    a += 1
                    m -= 5
                a = row - 1
                m = n + 5
                # move down
                while a > 0 and not chess_isOwn(state[m]):
                    end = letters[column] + str(a)
                    strOut.append(start + '-' + end + '\n')
                    if chess_isEnemy(state[m]):
                        a = 0
                    a -= 1
                    m += 5


        n += 1

    return strOut

def chess_movesShuffled():
    # with reference to the state of the game, determine the possible moves and shuffle them before returning them- note that you can call the chess_moves() function in here
    movelist = chess_moves()
    random.shuffle(movelist)
    return movelist

def chess_movesEvaluated():
    # with reference to the state of the game, determine the possible moves and sort them in order of an increasing evaluation score before returning them - note that you can call the chess_moves() function in here

    movelist = chess_movesShuffled()
    score = []
    newlist = []

    for move in movelist:
        chess_move(move)
        score.append(chess_eval())
        chess_undo()

    length = len(score)

    for i in range(0, length):
        value = min(score)
        index = score.index(value)
        newlist.append(movelist[index])

        del score[index]
        del movelist[index]

    return newlist

def chess_move(strIn):
    # perform the supplied move (for example 'a5-a4\n') and update the state of the game / your internal variables accordingly - note that it advised to do a sanity check of the supplied move

    global state
    global turnC
    global turnN
    global mlFlag
    global mlCounter
    global mLog
    global mPlog
    column = ['a', 'b', 'c', 'd', 'e']
    c = 0

    #separate the start and end position
    start, end = list(strIn.split('-'))

    #find the column for the start position
    while column[c] != start[0]:
        c += 1

    #calculate the position in the array
    Oposition =29 - (5 * (int(start[1]) - 1) + (4 - c))

    #Check to make sure '.' is not selected
    if chess_isNothing(state[Oposition]):
        return False

    #Check to make sure it is our own piece
    if str(state[Oposition]).isupper() and turnC == 'B' and mlFlag == 0:
        return False

    if chess_isEnemy(state[Oposition]) and mlFlag == 0:
        return False

    #save the value of the selected peice
    piece = state[Oposition]

    #replace the start position with '.'
    state[Oposition] = '.'

    # find the column for the end position
    c = 0
    while column[c] != end[0]:
        c += 1

    # calculate the position in the array
    position = 29 - (5 * (int(end[1]) - 1) + (4 - c))

    if mlFlag == 0:
        mLog.append(str(strIn))
        mlCounter += 1
        mPlog.append(str(state[position]))

        #Check to see if replacement with queen is needed
        if position < 5 and piece == 'P':
            state[position] = 'Q'
            PtoQlog.append(mlCounter)
        elif position > 24 and piece == 'p':
            state[position] = 'q'
            PtoQlog.append(mlCounter)
        else:
            state[position] = piece

        #change the turn number and turn color
        if turnC == 'W':
            turnC = 'B'
        elif turnC == 'B':
            turnC = 'W'
            turnN += 1
    else:
        # Check to see if replacement with queen is needed
        state[position] = piece
        state[Oposition] = mPlog[mlCounter]

        # Check to see if replacement with pawn is needed
        length = len(PtoQlog)
        for i in range(0, length):
            if mlCounter == PtoQlog[i]:
                if piece.islower():
                    state[position] = 'p'
                    del PtoQlog[i]
                elif piece.isupper():
                    state[position] = 'P'
                    del PtoQlog[i]

        # change the turn number and turn color
        if turnC == 'W':
            turnC = 'B'
            turnN -= 1
        elif turnC == 'B':
            turnC = 'W'

        mlFlag = 0
        mLog.pop()
        mPlog.pop()
        mlCounter -= 1

def chess_moveRandom():
    #perform a random move and return it - one example output is given below - note that you can call the chess_movesShuffled() function as well as the chess_move() function in here
    movelist = chess_movesShuffled()
    chess_move(movelist[0])
    return movelist[0]

def chess_moveGreedy():
    # perform a greedy move and return it - one example output is given below - note that you can call the chess_movesEvaluated() function as well as the chess_move() function in here
    movelist = chess_movesEvaluated()
    chess_move(movelist[0])
    return movelist[0]

def chess_moveNegamax(intDepth, intDuration):
    # perform a negamax move and return it - one example output is given below - note that you can call the the other functions in here
    best = ''
    score = -500
    global timelimit
    timelimit = time.time() + 6.2

    if intDepth == 0:
        return

    if intDuration <= 3.0:
        return chess_moveGreedy()

    count = 1
    while count < 10000:
        for move in chess_movesShuffled():
            chess_move(move)
            temp = -chess_Negamax(count)
            chess_undo()

            if time.time() >= timelimit:
                break

        count += 1

        if time.time() >= timelimit:
            break

        if temp > score:
            best = move
            score = temp

    chess_move(best)
    return best

def chess_Negamax(depth):
    #Negamax function to assist chess_moveNegamax

    global timecounter
    global timecache
    timecounter += 1

    if timecounter > 1000:
        timecounter = 0
        timecache = time.time()

    if timecache >= timelimit:
        return 0

    if depth == 0 or chess_winner() != '?':
        return chess_eval()

    score = -500
    for move in chess_movesShuffled():
        chess_move(move)
        score = max(score, -chess_Negamax(depth - 1))
        chess_undo()

    return score

def chess_moveAlphabeta(intDepth, intDuration):
    # perform a alphabeta move and return it - one example output is given below - note that you can call the the other functions in here
    best = ''
    alpha = -500
    beta = 500
    global timelimit
    timelimit = time.time() + 6.2

    if intDepth == 0:
        return

    if intDuration <= 3.0:
        return chess_moveGreedy()

    count = 1
    while count < 10000:
        for move in chess_movesEvaluated():
            chess_move(move)
            temp = -chess_Alphabeta(count, -beta, -alpha)
            chess_undo()

            if temp > alpha:
                best = move
                alpha = temp

            if time.time() >= timelimit:
                break

        count += 1

        if time.time() >= timelimit:
            break

    chess_move(best)
    return best

def chess_Alphabeta(depth, alpha, beta):

    global timecounter
    global timecache
    timecounter += 1

    if timecounter > 1000:
        timecounter = 0
        timecache = time.time()

    if timecache >= timelimit:
        return 0

    if depth == 0 or chess_winner() != '?':
        return chess_eval()

    score = -500
    for move in chess_movesEvaluated():
        chess_move(move)
        score = max(score, -chess_Alphabeta(depth - 1, -beta, -alpha))
        chess_undo()

        alpha = max(alpha, score)

        if alpha >= beta:
            break

    return score

def chess_undo():
    # undo the last move and update the state of the game / your internal variables accordingly - note that you need to maintain an internal variable that keeps track of the previous history for this
    global mlFlag

    if mlCounter > -1:
        mlFlag = 1

        start, end = list(mLog[mlCounter].split('-'))
        end = end.strip('\n')
        strOut = end + '-' + start
        chess_move(strOut)

