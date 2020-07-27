import random
from Snake import Snake
from sense_hat import SenseHat

class Board:
    
    sense = SenseHat()
    r = (255, 0, 0)
    g = (0, 255, 0)
    bl = (0, 0, 255)
    b = (0, 0, 0)
    
    board_dims = 8
    
    board_pixels = [
        b, b, b, b, b, b, b , b,
        b, b, b, b, b, b, b , b,
        b, b, b, b, b, b, b , b, 
        b, b, b, b, b, b, b , b,
        b, b, b, b, b, b, b , b,
        b, b, b, b, b, b, b , b,
        b, b, b, b, b, b, b , b,
        b, b, b, b, b, b, b , b
    ]
    
    def __init__(self):
        self.sense.clear()
        self.sense.set_pixels(self.board_pixels)
        self.snake = Snake(self.convertIndexToCoordinates(random.randint(0, 63)))
        self.drawSnake(self.snake)
        self.foodLoc = self.convertIndexToCoordinates(self.placeFood(self.snake))
    
    def drawSnake(self, snake):
        for i in range(len(snake.body)):
            board_Index = self.convertCoordinatesToIndex(snake.body[i])
            if i == 0:
                self.board_pixels[board_Index] = self.bl
            else:
                self.board_pixels[board_Index] = self.g
        self.sense.set_pixels(self.board_pixels)
    
    def refreshBoard(self):
        self.sense.set_pixels(self.board_pixels)
    
    def placeFood(self, snake):
        foodLoc = self.randExcludingBody(snake.body)
        self.board_pixels[foodLoc] = self.r
        self.sense.set_pixels(self.board_pixels)
        return foodLoc
        
    def randExcludingBody(self, body):
        randInt = random.randint(0,63)
        return self.randExcludingBody(body) if self.convertIndexToCoordinates(randInt) in body else randInt
        
        
    def convertIndexToCoordinates(self, index):
        return (index // self.board_dims, index % self.board_dims)
        
    def convertCoordinatesToIndex(self, coordinates):
        return (self.board_dims * coordinates[0]) + coordinates[1]
        
        