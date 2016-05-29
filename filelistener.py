import sys
import os


class FileListener:
    def __init__(self):
        self.mtimes = {}
        self.files = set()

    def add_path(self, path):
        self.files.add(path)

    def listen(self):
        for path in self.files:
            self.check(path)

    def check(self, path):
        try:
            mtime = os.stat(path).st_mtime
        except:
            return

        if path not in self.mtimes:
            self.mtimes[path] = mtime
        elif self.mtimes[path] < mtime:
            try:
                print('%s is modified!' % (path))
                self.mtimes[path] = mtime
            except:
                pass


if __name__ == '__main__':
    path = sys.argv[1]

    import time
    r = FileListener()
    r.add_path(path)
    while 1:
        try:
            r.listen()
            time.sleep(1)
        except KeyboardInterrupt:
            break
