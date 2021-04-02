import argparse
from src.atree import ATree


def main():
    parser = argparse.ArgumentParser(description='tree files')
    parser.add_argument('file', nargs='?', default=".")
    parser.add_argument('-d', '--depth', type=int, help='set tree depth')
    parser.add_argument('-a', action='store_true', help='show all files')

    args = parser.parse_args()
    print(args)
    atree = ATree(args.file, depth=args.depth, skip_dot_file=not args.a)
    atree.walk()


if __name__ == '__main__':
    main()
