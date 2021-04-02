import os


class ATree:
    def __init__(self, file=".", depth=None, skip_dot_file=True):
        self._file = file
        self._depth = depth
        self._skip_dot_file = skip_dot_file

    def walk(self):
        file = os.path.abspath(self._file)
        if self._skip_dot_file and os.path.basename(file).startswith("."):
            return
        self._walk(file, True, 0)

    def _walk(self, file: str, is_last_file, depth, prefix=""):
        if self._depth and depth > self._depth:
            return
        if is_last_file:
            print("{}└─{}".format(prefix, os.path.basename(file)))
        else:
            print("{}├─{}".format(prefix, os.path.basename(file)))
        if os.path.isdir(file):
            dirs = os.listdir(file)
            if self._skip_dot_file:
                dirs = [file for file in dirs if not file.startswith(".")]
            size = len(dirs)
            for i, dir_file in enumerate(dirs):
                dir_file = os.path.join(file, dir_file)
                if is_last_file:
                    self._walk(dir_file, i == size - 1, depth + 1, prefix + "  ")
                else:
                    self._walk(dir_file, i == size - 1, depth + 1, prefix + "│ ")
