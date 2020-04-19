import xml.etree.ElementTree as ET
from file_worker import FileWorker
EXT = 'html'
DIST = 'dist/'


class Parser:
    def __init__(self, graph):
        self.graph = graph

    def parse(self, text, path):

        text = self.parse_links(text, path)
        text = self.parse_text(text)
        text = self.parse_input(text)

        return text

    def get_converted_file_name(self, original_name):
        tokens = original_name.split('.')
        result = tokens[:len(tokens) - 1]
        result.append(EXT)
        return '.'.join(result)

    def parse_links(self, text, path):
        tree = ET.parse(path)
        self.root = tree.getroot()
        for link in self.root.findall('Link'):
            href = link.get('href')
            converted_href = self.get_converted_file_name(href)
            text = text.replace(href, converted_href)
            if href not in self.graph.links:
                self.graph.add_link(path, href)
                self.convert(path, converted_href)
            else:
                self.graph.add_link(path, href)
        text = text.replace('<Link', '<a')
        text = text.replace('/Link>', '/a>')

        return text

    def parse_text(self, text):
        text = text.replace('<Text', '<div')
        text = text.replace('/Text>', '/div>')
        return text

    def parse_input(self, text):
        text = text.replace('<Input', '<input')
        text = text.replace('/Input>', '/input>')
        return text

    def parse_buttons(self, text):
        text = text.replace('<Button', '<button')
        text = text.replace('/Button>', '/button>')
        return text

    def parse_images(self, text):
        text = text.replace('<Image', '<img')
        text = text.replace('/img>', '/img>')
        return text

    def parse_header(self, text):
        text = text.replace('<Header', '<header')
        text = text.replace('/Header>', '/header>')
        return text

    def parse_footer(self, text):
        text = text.replace('<Footer', '<footer')
        text = text.replace('/Footer', '/footer')
        return text

    def parse_table(self, text):
        text = text.replace('<Table', '<table')
        text = text.replace('/Table>', '/table>')
        return text

    def parse_cols(self, text):
        text = text.replace('<Column', '<td')
        text = text.replace('/Column>', '/td>')
        return text

    def parse_rows(self, text):
        text = text.replace('<Row', '<th')
        text = text.replace('/Row>', '/th>')
        return text

    def convert(self, source='index.karp', dist='index.html'):

        if source not in self.graph.links:
            file_worker = FileWorker()
            content = file_worker.read(source)
            converted_content = self.parse(content, source)
            file_worker.write(dist, converted_content)
