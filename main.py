import argparse

from universe import Universe






if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")
    parser.add_argument(
        '--size',
        dest='size',
        required=False,
        default=100,
        help='Size of the universe'
    )
    parser.add_argument(
        "--figure_name",
        dest='figure_name',
        choices=['10_cells_row']
    )
    parser.add_argument(
        "--figure_position",
        dest='figure_position',
        type=list
    )
    args = parser.parse_args()

    universe = Universe(args.size,args.figure_name)