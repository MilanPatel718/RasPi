import random

class Snake:
    def __init__(self, coord, snake_size, board_dims):
        self.lowerBound = 0
        self.upperBound = (board_dims ** 2) - 1
        self.vertOffset = board_dims * (snake_size - 1)
        self.horOffset = snake_size - 1
        self.body = self.initSnake(coord, snake_size, board_dims)
        
    def initSnake(self, coord, snake_size, board_dims):

        snakeHeadIndex = coord
        
        #Introduce random element to make snake horizontal or vertical
        orientation = random.choice(["Horizontal", "Vertical"])
        
        if orientation == "Horizontal":
            if snakeHeadIndex + self.horOffset <= self.upperBound:
                initList = []
                for i in range(snake_size):
                    initList.append(snakeHeadIndex + i)
                validPos = True
                for i in range(snake_size - 1):
                    if initList[i] % board_dims > initList[i + 1] % board_dims:
                        print(str(initList[i] % board_dims ) + " " + str(initList[i+1] % board_dims))
                        validPos = False
                        break
                if validPos == True:
                    return initList
                    
            if snakeHeadIndex - self.horOffset >= self.lowerBound:
                initList = []
                for i in range(snake_size):
                    initList.append(snakeHeadIndex - i)
                validPos = True
                for i in range(snake_size - 1):
                    if initList[i] % board_dims < initList[i + 1] % board_dims:
                        validPos = False
                        break
                if validPos == True:
                    return initList
        else:    
            if snakeHeadIndex + self.vertOffset <= self.upperBound:
                initList = []
                for i in range(snake_size):
                    initList.append(snakeHeadIndex + (i * board_dims))
                return initList
            
            if snakeHeadIndex - self.vertOffset >= self.lowerBound:
                initList = []
                for i in range(snake_size):
                    initList.append(snakeHeadIndex - (i * board_dims))
                return initList
        
        

        