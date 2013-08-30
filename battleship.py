from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print 'Just so you know, the answer is row ' + str(ship_row) + ' and column ' + str(ship_col)

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
turn = 0
for turn in range(4):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if turn == 3:
            print "You missed my battleship!"
            print "Game Over"
        elif (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
    # Print (turn + 1) here!
    print_board(board)
    turn += 1
    if turn == 3:
        print 'You have 1 guess left'
    elif turn == 4:
        print 'No more guesses for you!'
    else:
        print 'You have ' + str(4 - turn) + ' guesses left.'