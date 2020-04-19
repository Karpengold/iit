# -*- coding: utf-8 -*-
from file_worker import FileWorker
from parser import Parser
from graph_worker import GraphWorker
from searcher import Searcher
import glob

EXT = 'html'
DIST = 'dist/'

files = glob.glob("*.karp")
parser = Parser(GraphWorker())

for file in files:
    parser.convert(file, parser.get_converted_file_name(file))

print(parser.graph.is_bipartite())  # проверка графа на двудольность

searcher = Searcher()

print(searcher.search(parser.graph, 'search me'))  # поиск текста в документах
