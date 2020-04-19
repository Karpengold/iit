class GraphWorker:
    def __init__(self):
        self.nodes = {}
        self.links = {}
        self.ids = []

    def add_link(self, f_link, to_link):

        if f_link not in self.links:
            self.links[f_link] = len(self.links)
            self.ids.append(f_link)
        if to_link not in self.links:
            self.links[to_link] = len(self.links)
            self.ids.append(to_link)

        self.add_node(self.links[f_link], self.links[to_link])

    def add_node(self, f_node, to_node):

        if f_node in self.nodes:
            self.nodes[f_node].append(to_node)
        else:
            self.nodes[f_node] = [to_node]

        if to_node not in self.nodes:
            self.nodes[to_node] = []

    # Проверка графа на двудольность
    # Пробуем "окрасить" одну вершину в один цвет,
    # а всех ее соседей в противоположный
    # Если среди соседей окажется уже окрашенный в такой же цвет
    # значит граф не двудольный

    # Так же данный алгоритм можно использовать для поиска
    # количества компонент связности графа

    def is_bipartite(self):

        n = len(self.links)
        colors = [None] * n
        used = [False] * n
        bipartite = [True]

        def runner(child, parent):
            used[child] = True
            colors[child] = True
            if parent:
                if colors[child] == colors[parent]:
                    bipartite[0] = False
                    return False
                if colors[child] is None:
                    colors[child] = not colors[parent]
                    return True

        for i in range(len(used)):
            if not used[i]:
                self.dfs(i, None, runner, used)

        return bipartite[0]

   # Поиск в глубину

    def dfs(self, node, parent, callback, used):
        callback(node, parent)
        for i in self.nodes[node]:
            if not used[i]:
                self.dfs(i, node, callback, used)
