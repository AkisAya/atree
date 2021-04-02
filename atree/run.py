import argparse

from atree.atree import ATree


def main():
    parser = argparse.ArgumentParser(description='tree files')
    parser.add_argument('file', action='store_const', const=".")
    parser.add_argument('-d', '--depth', nargs=1, help='set tree depth')
    parser.add_argument('-a', action='store_true', help='show all files')

    args = parser.parse_args()
    atree = ATree(args.file, depth=args.depth, skip_dot_file=not args.a)
    atree.walk()


if __name__ == '__main__':
    main()
