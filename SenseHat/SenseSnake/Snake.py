class Snake:
    def __init__(self, coord):
        self.body = self.initSnake(coord)
        
    def initSnake(self, coord):
        snakeHeadCoord = coord
        snakeHead_X = snakeHeadCoord[0]
        snakeHead_Y = snakeHeadCoord[1]
        if snakeHead_X + 2 < 8:
            return [snakeHeadCoord, (snakeHead_X + 1, snakeHead_Y), (snakeHead_X + 2, snakeHead_Y)]
        elif snakeHead_Y + 2 < 8:
            return [snakeHeadCoord, (snakeHead_X, snakeHead_Y + 1), (snakeHead_X, snakeHead_Y + 2)]
        elif snakeHead_X - 2 >= 0:
            return [snakeHeadCoord, (snakeHead_X - 1, snakeHead_Y), (snakeHead_X - 2, snakeHead_Y)]
        elif snakeHead_Y - 2 >= 0:
            return [snakeHeadCoord, (snakeHead_X, snakeHead_Y - 1), (snakeHead_X, snakeHead_Y - 2)]
        return
        
        

        