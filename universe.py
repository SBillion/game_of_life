import numpy as np


class Universe:
    # Dictionnary of matrice in values representing initial living cells
    figures = {
        '10_cells_row': [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
        '6_cells': [[1, 1, 0, 1, 1, 1, 0, 1, 0, 0]]
    }

    def __init__(self, size=None, figure_name=None, figure_position=None):
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
        self.size = [size,size]
        if not figure_name:
            self.matrix = self.random_initial_life(size)
            return
        self.matrix = np.zeros(self.size)  # Universe full of dead cells
        # Get position of the figure to populate the universe
        x_start, y_start = figure_position[0], figure_position[1]
        figure_matrix = np.array(self.figures[figure_name])
        x_end, y_end = x_start + figure_matrix.shape[0], y_start + \
                       figure_matrix.shape[1]

        # Populate the universe by injecting the figure in its matrix
        self.matrix[x_start:x_end, y_start:y_end] = figure_matrix

    def random_initial_life(self, size):
        """

        :return:
        """
        return np.random.choice(
            [0, 1], size * size, p=[0.2, 0.8]
        ).reshape(self.size)
