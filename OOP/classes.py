
class TextReader(object):

    def read_text(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            print(f.read())