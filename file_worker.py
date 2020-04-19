DIST = 'dist/'


class FileWorker:
    def read(self, path):
        f = open(path, "r")
        return f.read()

    def write(self, path, text):
        with open(DIST + path, 'w+') as f:
            f.write(text)
