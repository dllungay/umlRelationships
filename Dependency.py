class Document:
    def __init__(self, text):
        self.text = text

class Printer:
    def print_doc(self, doc: Document):
        print(doc.text)

Printer().print_doc(Document("Hello"))