import argparse

from universe import Universe






if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")
    parser.add_argument('--size', dest='size', required=False, default=100)
    parser.add_argument(
        "--initial_figure",
        dest='initial_figure',
        choices=['10_cells_row']
    )
    parser.add_argument(
        "--figure_position",
        dest='figure_position',
        type=list
    )
    args = parser.parse_args()

    universe = Universe(args.size,initial_figures[args.initial_figure])