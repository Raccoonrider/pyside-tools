from PySide6.QtCore import QFile, QTextStream

def load_stylesheet(resource_name:str) -> str:
    file = QFile(resource_name)
    file.open(QFile.ReadOnly | QFile.Text)
    text_stream = QTextStream(file)
    return text_stream.readAll()
