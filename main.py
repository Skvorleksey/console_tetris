import shapes
import random


class Tetris:
    def __init__(self):
        self.ground_width = 10
        self.ground_height = 20
        self.is_game_on = True
        self.greeting()
        self.shapes = shapes.shapes
        self.ground = [[' '] * self.ground_width for _ in range(self.ground_height)]
        self.current_shape = random.choice(shapes.shapes)
        self.x = 0
        self.y = 0

        self.stack = [[' '] * self.ground_width for _ in range(self.ground_height)]

        self.draw()
        self.start()

    def greeting(self):
        print("Welcome to tetris game!\n")

    def rotate_shape(self):
        width = len(self.current_shape)
        height = len(self.current_shape[0])
        new_shape = [[' '] * width for _ in range(height)]
        for i in range(width):
            for a in range(height):
                new_shape[a][width - 1 - i] = self.current_shape[i][a]
        self.current_shape = new_shape
        print(self.current_shape)

    def draw(self):
        self.ground = [[' '] * self.ground_width for _ in range(self.ground_height)]

        for y, line in enumerate(self.stack):
            for x, cell in enumerate(line):
                if cell != ' ':
                    self.ground[y][x] = cell

        for y, line in enumerate(self.current_shape):
            for x, cell in enumerate(line):
                if cell != ' ':
                    self.ground[self.y + y][self.x + x] = cell

        for line in self.ground:
            print(f"|{''.join(line)}|")

    def logic(self):
        # gravity
        self.y += 1

        # check side edges collision
        if self.x < 0:
            self.x = 0
        elif self.x + len(self.current_shape[0]) > self.ground_width:
            self.x = self.ground_width - len(self.current_shape[0])

        # check bottom collision
        if self.y + len(self.current_shape) >= self.ground_height + 1:
            for y, line in enumerate(self.current_shape):
                for x, cell in enumerate(line):
                    if cell != ' ':
                        self.stack[self.y + y - 1][self.x + x] = cell

            self.y = 0
            self.x = 0
            self.current_shape = random.choice(shapes.shapes)



    def control(self):
        button = input('Input [W A S D]: ')
        if button.lower() == 'x':
            print('Bye!')
            self.is_game_on = False
        elif button.lower() == 'a':
            self.x -= 1
        elif button.lower() == 'd':
            self.x += 1
        elif button.lower() == 'w':
            self.rotate_shape()

    def start(self):
        while self.is_game_on:
            self.control()
            self.logic()

            self.draw()


Tetris()
