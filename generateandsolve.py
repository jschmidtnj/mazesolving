from solve import solve
from mazegenerator import generatemaze, str2bool
import argparse, factory

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--method", nargs='?', const=factory.DefaultMethod, default=factory.DefaultMethod,
                        choices=factory.MethodChoices)
    parser.add_argument("--priority-queue", nargs='?', const=None, default=None,
                        choices=factory.PriorityQueueChoices,
                        help="only used by the astar and dijkstra methods")
    parser.add_argument("width")
    parser.add_argument("height")
    parser.add_argument("maze_file")
    parser.add_argument("result_file")
    parser.add_argument("generate_bmp", nargs='?', default='no')
    args = parser.parse_args()
    generate_bmp_bool = str2bool(args.generate_bmp)
    width = 0
    height = 0
    try:
        width = int(args.width)
    except:
        raise argparse.ArgumentTypeError('Width must be an integer.')
    try:
        height = int(args.height)
    except:
        raise argparse.ArgumentTypeError('Height must be an integer.')

    #print(width, height, args.output_file, generate_bmp_bool)
    generatemaze(width, height, args.maze_file, generate_bmp_bool)
    solve(args.maze_file + '.png', args.result_file + '.png', args.method, args.priority_queue)

if __name__ == "__main__":
    main()