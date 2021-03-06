# mazesolving
A variety of algorithms to solve mazes from an input image.
Originally forked from a Computerphile project, now with some cool changes for maze generation and solving. Will eventually implement dual-side dijkstra's algorithm, which is arguably fastest for maze solving. Any input is appreciated.

## About
These are the python files for maze generation and solving. Feel free to use, alter, redistribute the code as you see fit.

## Input
Some example mazes are included in the repository.. Once exported I edited the mazes to ensure that the following rules are adhered to:

- Each maze is black and white. White represents paths, black represents walls.
- All mazes are surrounded entirely by black walls.
- One white square exists on the top row of the image, and is the start of the maze.
- One white square exists on the bottom row of the image, and is the end of the maze.

## Installation
use python 2, python 3 requires a bit of modification regarding the Node less-than comparison. Run `python solve.py [input_file] [output_file]` to use the default configuration on some of the examples. Use the `-m` flag to set a specific algorithm to use (such as Dijkstra, AStar, leftturn, etc.). The Dijkstra and AStar are the fastest. To generate your own mazes, use `python mazegenerator.py [width] [height] [output_file] [generate_bmp]`. Then run `solve.py` to get the result. Or to do the whole sequence in one command, use `python generateandsolve.py [width] [height] [maze_file] [result_file] [generate_bmp]`. And that's it - you now have a consistent maze-solver.