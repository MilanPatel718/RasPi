from Board import Board
from pynput.keyboard import Key, Listener
from enum import Enum
import time

#Used as indicators for movement
currDirection = ""
prevDirection = ""
#Global Access for Board
board = Board()
#Choose a value 0 > x <= 1 (lower values will make the snake faster)
sleepTime = .5

#Game Driver
def main():
    global board
    global currDirection
    global prevDirection
    snakeBody = board.snake.body
    listener = Listener(on_press=on_press, on_release=on_release)
    listener.start()
    while(True):
        newPos = ""
        if currDirection == "up":
            if snakeBody[0] - 8 != snakeBody[1]:
                newPos = snakeBody[0] - 8
                if newPos < 0:
                    break
                elif newPos in snakeBody:
                    break
                moveSnake(newPos, snakeBody)
            else:
                currDirection = prevDirection
                continue
                
        elif currDirection == "down":
            if snakeBody[0] + 8 != snakeBody[1]:
                newPos = snakeBody[0] + 8
                if newPos > 63:
                    break
                elif newPos in snakeBody:
                    break
                moveSnake(newPos, snakeBody)
            else:
                currDirection = prevDirection
                continue
                
        elif currDirection == "left":
            if snakeBody[0] - 1 != snakeBody[1]:
                newPos = snakeBody[0] - 1
                if newPos < 0:
                    break
                elif newPos % board.board_dims == 7:
                    break
                elif newPos in snakeBody:
                    break
                moveSnake(newPos, snakeBody)
            else:
                currDirection = prevDirection
                continue
            
            
        elif currDirection == "right":
            if snakeBody[0] + 1 != snakeBody[1]:
                newPos = snakeBody[0] + 1
                if newPos > 63:
                    break
                elif newPos % board.board_dims == 0:
                    break
                elif newPos in snakeBody:
                    break
                moveSnake(newPos, snakeBody)
            else:
                currDirection = prevDirection
                continue
            
        board.drawSnake(board.snake)
        time.sleep(sleepTime)
    listener.stop()

def moveSnake(newPos, snakeBody):
    global board
    prevCell = ""
    for i in range(len(snakeBody)):
            if i == 0:
                prevCell = snakeBody[i]
                snakeBody[i] = newPos
            else:
                temp = snakeBody[i]
                snakeBody[i] = prevCell
                prevCell = temp
    
    if newPos == board.foodLoc:
        snakeBody.append(prevCell)
        board.snake.body = snakeBody
        board.board_pixels[prevCell] = board.g
        board.foodLoc = board.placeFood(board.snake)
        board.refreshBoard()

    else:
        board.snake.body = snakeBody
        board.board_pixels[prevCell] = board.b


#Keyboard Listener Methods        
def on_press(key):
    return True

def on_release(key):    
    global currDirection
    global prevDirection
    if isinstance(key, Enum):
        if key == Key.up:
            prevDirection = currDirection
            currDirection = "up"
        if key == Key.down:
            prevDirection = currDirection
            currDirection = "down"
        if key == Key.left:
            prevDirection = currDirection
            currDirection = "left"
        if key == Key.right:
            prevDirection = currDirection
            currDirection = "right"
    else:
        if key.char == "w":
            prevDirection = currDirection
            currDirection = "up"
        if key.char == "s":
            prevDirection = currDirection
            currDirection = "down"
        if key.char == "a":
            prevDirection = currDirection
            currDirection = "left"
        if key.char == "d":
            prevDirection = currDirection
            currDirection = "right"
            
    return True
        
if __name__ == '__main__':
    main()