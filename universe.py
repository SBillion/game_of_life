import datetime

import numpy as np
from matplotlib import pyplot, animation


class Universe:
    # Dictionnary of matrice in values representing initial living cells
    figures = {
        "10_cells_row": [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
        "infinite": [
            [1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 1, 1, 0, 1],
            [1, 0, 1, 0, 1],
        ],
        "6_cells": [[1, 1, 0, 1, 1, 1, 0, 1, 0, 0]],
        "bird": [
            [0, 0, 1, 1, 0],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 1, 0],
            [0, 1, 1, 0, 0],
        ],
    }

    def __init__(self, size=100, figure_name=None, figure_position=None, iterations=50):
        """
        Initialize the Universe with living cells
        :param size: Size of the universe
        :type size: int
        :param figure_name: Key of dict FIGURES to get one initial figure
        :type figure_name: str
        :param figure_position: Top left corner coordinate of the figure in
        the universe:
        :type: tuple (int,int)
        """
        # Return a matrix universe with random life if figure is not provided
        self.size = [size, size]
        self.iterations = iterations
        if not figure_name:
            self.matrix = self.random_initial_life(size)
            return
        self.matrix = np.zeros(self.size)  # Universe full of dead cells

        if not figure_position:
            figure_position = (int(size / 2), int(size / 2))
        # Get position of the figure to populate the universe
        x_start, y_start = figure_position[0], figure_position[1]
        figure_matrix = np.array(self.figures[figure_name])
        x_end, y_end = (
            x_start + figure_matrix.shape[0],
            y_start + figure_matrix.shape[1],
        )

        # Populate the universe by injecting the figure in its matrix
        self.matrix[x_start:x_end, y_start:y_end] = figure_matrix

    def random_initial_life(self, size):
        """
        Get a matrix of the size of the universe with random life
        :return: a matrix of random life
        :rtype: np.array
        """
        return np.random.choice([0, 1], size * size, p=[0.2, 0.8]).reshape(self.size)

    def animate(self):
        fig = pyplot.figure()
        pyplot.axis("off")
        ims = []
        for i in range(self.iterations):
            ims.append((pyplot.imshow(self.matrix),))
            self.matrix = self.get_next_matrix()
        im_ani = animation.ArtistAnimation(
            fig, ims, repeat_delay=3000, blit=True
        )
        im_ani.save(("{}.gif".format(
            datetime.datetime.now().isoformat('_','seconds')
        )), writer="imagemagick")

    def get_next_matrix(self):
        """
        Get the next sate of the matrix of the universe

        :return: new universe of cells
        :rtype: np.array
        """
        # Copy the original matrix to avoid modification during loop
        new_matrix = np.copy(self.matrix)
        # Browse the original matrix of the universe
        for i in range(self.matrix.shape[0]):
            for j in range(self.matrix.shape[1]):
                # Set the new state if the cell for new matrix
                new_matrix[i, j] = self.get_next_state_of_cell(i, j)
        return new_matrix

    def get_total_neighbours_of_cell(self, x, y):
        """
        Get the total of neighbour of a cell

        :param x: x coordinate of cell in the universe
        :type x: int
        :param y: y coordinate of cell in the universe
        :type y: int
        :return: Total of neighbour of a cell
        :rtype: int
        """
        return np.sum(self.matrix[x - 1 : x + 2, y - 1 : y + 2]) - self.matrix[x, y]

    def get_next_state_of_cell(self, x, y):
        """
        Get the next state of a cell in the universe.

        :param x: x coordinate of cell in the universe
        :type x: int
        :param y: y coordinate of cell in the universe
        :type y: int
        :return: Next state of the cell
        :rtype: int
        """

        total_neighbours = self.get_total_neighbours_of_cell(x, y)

        # Cell become dead if total of neighbours is between 2 and 3
        if self.matrix[x, y] and not 2 <= total_neighbours <= 3:
            return 0
        # Cell become alive if total of neighbours is 3
        elif total_neighbours == 3:
            return 1

        return self.matrix[x, y]
