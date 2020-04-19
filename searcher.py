from file_worker import FileWorker


class Searcher:
    def __init__(self):
        self.file_worker = FileWorker()

    def search(self, graph, text):

        n = len(graph.links)
        used = [False] * n
        result = []

        def runner(child, node):
            if used[child] == True:
                return False
            path = graph.ids[child]
            used[child] = True
            doc = self.file_worker.read(path)
            if self.find_text(text, doc):
                result.append(path)
            return True

        for i in range(len(used)):
            if not used[i]:
                graph.dfs(i, None, runner, used)
        return result

    def find_text(self, text, doc):
        return doc.find(text) != -1
