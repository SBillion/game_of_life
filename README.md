# The game of life


The universe of the Game of Life is an infinite, two-dimensional orthogonal 
grid of square cells, each of which is in one of two possible states,
alive or dead, (or populated and unpopulated, respectively). 
Every cell interacts with its eight neighbours, which are the cells that are
horizontally, vertically, or diagonally adjacent. At each step in time, 
the following transitions occur:

    Any live cell with fewer than two live neighbors dies, as if by under population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by overpopulation.
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The initial pattern constitutes the seed of the system.
The first generation is created by applying the above rules simultaneously 
to every cell in the seed; births and deaths occur simultaneously, 
and the discrete moment at which this happens is sometimes called a tick. 
Each generation is a pure function of the preceding one. 
The rules continue to be applied repeatedly to create further generations.

## Clone the repo

First step is to clone this repo in your working directory

`git clone https://github.com/SBillion/game_of_life.git`

## Install required packages

Next step is to install third packages used by this program

### Using pipenv

To install with your default python interpreter:
```shell
pipenv install
```

To install using a specific version of python:


```shell
pipenv install  --python 3.7
```

To install packages used for testing and development, please add 
`--dev`

### Using pip

Install required packages:

```shell
pip install -r requirements.txt
```

To install packages used for testing and development:
```shell
pip install -r requirements_dev.txt
```

## Launch it
 
### Basic start
 
 ```bash
 python main.py
 ```
 
 Wait until the end of execution and you see that a **gif** file appeard in
 your folder. This gif is the result of the game of life using a random initial
 pattern of the universe and 50 iterations. 
 Open the **gif** file to see the result
 
 ### Using parameters
 
 You can use `--help` to see the list of available parameters:
 
 ```bash
python main.py --help
```
 
```bash
usage: main.py [-h] [--size SIZE]
               [--figure_name {10_cells_row,infinite,6_cells,bird}]
               [--figure_position FIGURE_POSITION] [--iterations ITERATIONS]

Runs Conway's Game of Life simulation.

optional arguments:
  -h, --help            show this help message and exit
  --size SIZE           Size of the universe
  --figure_name {10_cells_row,infinite,6_cells,bird}
  --figure_position FIGURE_POSITION  Top left corner coordinates of the figure in the
                        universe. 2 numbers seperates by a coma
  --iterations ITERATIONS Number of universe iteration
```
 
## Tests

To launch all the test just do:

```bash
tox
```
 