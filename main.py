import argparse

from universe import Universe

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Runs Conway's Game of Life simulation.")
    parser.add_argument(
        '--size',
        dest='size',
        type=int,
        required=False,
        default=100,
        help='Size of the universe'
    )
    parser.add_argument(
        "--figure_name",
        dest='figure_name',
        type=str,
        choices=['10_cells_row']
    )
    parser.add_argument(
        "--figure_position",
        dest='figure_position',
        help='Top left corner coordinates of the figure in the universe. 2 '
             'numbers seperates by a coma'
    )
    args = parser.parse_args()
    figure_position = list(args.figure_position.split(','))

    universe = Universe(args.size, args.figure_name, figure_position)
