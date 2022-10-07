import shapes
import random


class Shape:
    """
    It has 2d array current shape, next value for shape, full list of shapes, coordinates.
    """
    def __init__(self) -> None:
        """
        Initialize start values to start the game.
        """
        self.shapes = shapes.shapes
        self.current_shape = random.choice(shapes.shapes)
        self.next_shape = random.choice(shapes.shapes)
        self.x = 3
        self.y = 0

    def rotate_shape(self) -> None:
        """Change the 2d array image"""
        width = len(self.current_shape)
        height = len(self.current_shape[0])
        new_shape = [[' '] * width for _ in range(height)]
        for i in range(width):
            for a in range(height):
                new_shape[a][width - 1 - i] = self.current_shape[i][a]
        self.current_shape = new_shape

    def get_new_shape(self) -> None:
        """
        Refresh coordinates.
        Next shape becomes current shape.
        Refresh next shape.
        """
        self.y = 0
        self.x = 3
        self.current_shape = self.next_shape
        self.next_shape = random.choice(shapes.shapes)
