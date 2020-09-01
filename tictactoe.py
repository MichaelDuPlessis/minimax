import math

donePlaying = False
while not donePlaying:
    board = []
    SIZE = 3
    player, AI = 'O', 'X'

    for i in range(SIZE):
        board.append([])

    for i in range(SIZE):
        for j in range(SIZE):
            board[i].append(i*3+j+1)

    # Prints board
    def printBoard():
        line = ''

        for i in board:
            for j in i:
                line += str(j)
            print(line)
            line = ""

        print()

    def checkFull():
        count = 0

        for i in board:
            for j in i:
                if (j == player or j == AI):
                    count += 1

        if (count >= 9):
            return True
        else:
            return False

    def checkWinner():
        for i in range(SIZE):
            if (board[0][i] == board[1][i] and board[0][i] == board[2][i]):
                return board[0][i]

            if (board[i][0] == board[i][1] and board[i][0] == board[i][2]):
                return board[i][0]

        if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
            return board[1][1]

        if (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
            return board[1][1]

        return None

    def bestMove():
        winner = checkWinner()

        if (winner != None or checkFull()):
            return

        best = -math.inf

        for i in range(SIZE):
            for j in range(SIZE):
                if (board[i][j] != AI and board[i][j] != player):
                    temp = board[i][j]
                    board[i][j] = AI
                    score = minimax(0, False, AI, player)
                    board[i][j] = temp

                    if (score > best):
                        best = score
                        pos = []
                        pos.append(i)
                        pos.append(j)

        board[pos[0]][pos[1]] = AI

        printBoard()
        playerMove()

    def minimax(depth, isMax, p1, p2):
        winner = checkWinner()
        if (winner != None):
            if (winner == p1):
                return 1
            else:
                return -1
        
        if (checkFull()):
            return 0

        if (isMax):
            best = -math.inf

            for i in range(SIZE):
                for j in range(SIZE):
                    if (board[i][j] != p1 and board[i][j] != p2):
                        temp = board[i][j]
                        board[i][j] = p1
                        score = minimax(depth + 1, False, p1, p2)
                        board[i][j] = temp

                        if (score > best):
                            best = score

            return best

        else:
            best = math.inf

            for i in range(SIZE):
                for j in range(SIZE):
                    if (board[i][j] != p1 and board[i][j] != p2):
                        temp = board[i][j]
                        board[i][j] = p2
                        score = minimax(depth + 1, True, p1, p2)
                        board[i][j] = temp

                        if (score < best):
                            best = score

            return best

    def playerMove():
        winner = checkWinner()

        if (winner != None or checkFull()):
            return

        spot = int(input("Enter a position to play: "))

        if (spot > 9):
            return

        board[(spot-1)//3][(spot-1)%3] = player

        bestMove()


    p = input("Player 1 or 2 1/2: ")
    print()

    printBoard()

    if (p == "1"):
        player, AI = AI, player
        playerMove()
    else:
        bestMove()

    printBoard()

    if (checkWinner() == None):
        print("\nTie")
    else:
        print("\n"+checkWinner(),"Wins")


    playAgain = input("Do you want to play again (y/n): ")
    if (playAgain != "y"):
        donePlaying = True
