# Bowling Score Tracker

from time import sleep


def main():
    board = [None]*21
    frame_board = [None]*10
    symbol_board = [None]*10
    shot = 0
    for frame in range(1, 11):
        print("Frame ", frame)
        print()
        score = int(input("Enter score for ball 1: "))
        board[shot] = score
        shot += 1
        # -------- 10th frame -----------------
        if frame == 10:
            if score == 10:
                symbol_board[frame-1] = "X"
                score = int(input("Enter score for ball 2: "))
                board[shot] = score
                if score == 10:
                    symbol_board[frame-1] += "X"
                else:
                    symbol_board[frame-1] += str(board[shot])
                shot += 1
                score = int(input("Enter score for ball 3: "))
                board[shot] = score
                if board[shot] == 10:
                    symbol_board[frame-1] += "X"
                elif board[shot] + board[shot-1] == 10:
                    symbol_board[frame-1] += "/"
                else:
                    symbol_board[frame-1] += str(board[shot])
                shot += 1
            else:
                score = int(input("Enter score for ball 2: "))
                board[shot] = score
                if board[shot] + board[shot-1] >= 10 and board[shot] != 10:
                    symbol_board[frame-1] = str(board[shot-1]) + "/"
                    shot += 1
                    score = int(input("Enter score for ball 3: "))
                    board[shot] = score
                    if score != 10:
                        symbol_board[frame-1] += str(board[shot])
                    else:
                        symbol_board[frame-1] += "X"
                else:
                    symbol_board[frame-1] = str(board[shot-1]) + str(board[shot])
        # --------- 10th frame -----------------
        else:
            if score == 10:
                symbol_board[frame-1] = "X"
                shot += 1
            else:
                score = int(input("Enter score for ball 2: "))
                board[shot] = score
                if board[shot] + board[shot-1] >= 10:
                    symbol_board[frame-1] = str(board[shot-1]) + "/"
                else:
                    symbol_board[frame-1] = str(board[shot-1]) + str(board[shot])
                shot += 1
            print()
    # ---------- Score Calculation ----------
    #print(board)
    shot = 0
    for frame in range(10):
        if frame == 9:
            if board[20] == None:
                frame_board[frame] = board[18] + board[19]
            else:
                frame_board[frame] = board[18] + board[19] + board[20]
        else:
            if board[shot] == 10:
                frame_board[frame] = 10 + board[shot+2]
                if board[shot+3] == None:
                    frame_board[frame] += board[shot+4]
                else:
                    frame_board[frame] += board[shot+3]
            else:
                if board[shot] + board[shot+1] >= 10:
                    frame_board[frame] = 10 + board[shot+2]
                else:
                    frame_board[frame] = board[shot] + board[shot+1]
            shot += 2
    #print(frame_board)
    final_score = sum(frame_board)
    #print(symbol_board)
    #print(final_score)
    # ---------- Score Calculation ----------
    print()
    print()
    print("SCOREBOARD")
    sleep(1)
    # Score Display
    for symbol in symbol_board:
        sleep(0.002)
        print(symbol, end = "    ")
    print()
    for i in range(10):
        #sleep(0.002)
        print(sum(frame_board[:i+1]) , end="   ")
    end_message = "FINAL SCORE: " + str(sum(frame_board))
    print()
    sleep(1)
    print(end_message)
    #for i in range(len(end_message)):
        #sleep(0.001)
        #print(end_message[i], end="")
    perfect = "PERFECT GAME!!!"
    if sum(frame_board) == 300:
        sleep(1)
        print()
        #for i in range(len(perfect)):
            #sleep(0.001)
            #print(perfect[i], end="")
        print(perfect)
        
if __name__ == "__main__":
    main()

    
