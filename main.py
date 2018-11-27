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
        choices=['10_cells_row','infinite','6_cells','bird']
    )
    parser.add_argument(
        "--figure_position",
        dest='figure_position',
        help='Top left corner coordinates of the figure in the universe. 2 '
             'numbers seperates by a coma'
    )
    parser.add_argument(
        "--iterations",
        dest='iterations',
        default=50,
        type=int,
        help='Number of universe iterations'
    )
    args = parser.parse_args()
    try:
        figure_position = [ int(i) for i in args.figure_position.split(',')]
    except AttributeError:
        figure_position=None
    universe = Universe(args.size, args.figure_name, figure_position, args.iterations)
    universe.animate()
