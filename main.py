import msvcrt
import time

from shape import Shape


class Tetris:
    def __init__(self):
        self.ground_width = 10
        self.ground_height = 20
        self.is_game_on = True
        self.greeting()
        self.ground = [[' '] * self.ground_width for _ in range(self.ground_height)]
        self.lines = 0
        self.scores = 0
        self.level = 1

        self.shape = Shape()

        self.stack = [[' '] * self.ground_width for _ in range(self.ground_height)]

        self.draw()
        self.start()

    def greeting(self):
        print("Welcome to tetris game!\n")

    def draw(self):
        self.ground = [[' '] * self.ground_width for _ in range(self.ground_height)]

        for y, line in enumerate(self.stack):
            for x, cell in enumerate(line):
                if cell != ' ':
                    self.ground[y][x] = cell

        for y, line in enumerate(self.shape.current_shape):
            for x, cell in enumerate(line):
                if cell != ' ':
                    self.ground[self.shape.y + y][self.shape.x + x] = cell

        print()
        for i, line in enumerate(self.ground):
            if i - 1 < len(self.shape.next_shape) and i != 0:
                next_shape_line = self.shape.next_shape[i-1]
                print(f"|{''.join(line)}| {''.join(next_shape_line)}")
            elif i == 0:
                print(f"|{''.join(line)}| Next:")
            elif i == 5:
                print(f"|{''.join(line)}| Lines: {self.lines}")
            elif i == 7:
                print(f"|{''.join(line)}| Scores: {self.scores}")
            else:
                print(f"|{''.join(line)}|")

    def logic(self):
        # gravity
        self.shape.y += 1

        # check side edges collision
        if self.shape.x < 0:
            self.shape.x = 0
        elif self.shape.x + len(self.shape.current_shape[0]) > self.ground_width:
            self.shape.x = self.ground_width - len(self.shape.current_shape[0])

        # check stack collisions
        if self.is_touch_stack():
            for y, line in enumerate(self.shape.current_shape):
                for x, cell in enumerate(line):
                    if cell != ' ':
                        self.stack[self.shape.y + y][self.shape.x + x] = cell

            self.shape.get_new_shape()

        # check bottom collision
        elif self.shape.y + len(self.shape.current_shape) >= self.ground_height + 1:
            for y, line in enumerate(self.shape.current_shape):
                for x, cell in enumerate(line):
                    if cell != ' ':
                        self.stack[self.shape.y + y - 1][self.shape.x + x] = cell

            self.shape.get_new_shape()

        # check completed lines
        multiply_rate = {1: 1, 2: 3, 3: 5, 4: 8}
        completed = 0
        for line in self.stack:
            if line == ['#'] * self.ground_width:
                self.stack.remove(line)
                self.stack.insert(0, [' '] * self.ground_width)
                completed += 1

        if completed:
            self.lines += completed
            self.scores += 100 * self.level * multiply_rate[completed]

    def is_game_over(self):
        for col in range(3, 7):
            if (row := self.get_highest_stack_point(col)) <= 2 and (row != -1):
                return True

    def is_touch_stack(self):
        col_range = [i + self.shape.x for i in range(len(self.shape.current_shape[0]))]
        for col in col_range:
            if self.get_highest_stack_point(col) - self.get_lowest_shape_point(col) == 1:
                return True

    def get_highest_stack_point(self, col):
        for row, line in enumerate(self.stack[self.shape.y:], self.shape.y):
            if line[col] != ' ':
                return row
        return -1

    def get_lowest_shape_point(self, col):
        for i in range(len(self.shape.current_shape) - 1, -1, -1):
            if self.shape.current_shape[i][col-self.shape.x] != ' ':
                return i + self.shape.y

    def control(self):
        if msvcrt.kbhit():
            button = ord(msvcrt.getch())
            if button == ord('x'):
                print('Bye!')
                self.is_game_on = False
                return True
            elif button == ord('a'):
                self.shape.x -= 1
            elif button == ord('d'):
                self.shape.x += 1
            elif button == ord('w'):
                self.shape.rotate_shape()
            elif button == ord('s'):
                self.scores += 1
        else:
            time.sleep(0.5)

    def start(self):
        while self.is_game_on:
            if self.control():
                break
            self.logic()
            if self.is_game_over():
                print('Game over!')
                self.is_game_on = False

            self.draw()


Tetris()
