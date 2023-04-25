import re

from PySide6 import QtCore, QtWidgets

def search_table_widget_header(table:QtWidgets.QTableWidget):
    def wrapped(query:str=None):
        if query is None:
            if not hasattr(table, 'search_query') or table.search_query == '' or not table.selectedItems():
                return
            selected_row = table.selectedItems()[0].row()
            for row in range(selected_row + 1, table.rowCount()):
                item = table.verticalHeaderItem(row)
                text = re.sub(r'\d+ ', '', item.text()).casefold()
                if text.startswith(table.search_query):
                    table.clearSelection()
                    table.selectRow(row)
                    return    
        else:
            table.search_query = query.casefold()

        
        for row in range(table.rowCount()):
            item = table.verticalHeaderItem(row)
            text = re.sub(r'\d+ ', '', item.text()).casefold()
            if text.startswith(table.search_query):
                table.clearSelection()
                table.selectRow(row)
                return

    return wrapped

def search_table_widget_body(table:QtWidgets.QTableWidget):
    def wrapped(query:str=None):
        if query is None: # Enter pressed
            if not hasattr(table, 'search_query') or table.search_query == '' or not table.selectedItems():
                return
            selected_row = table.selectedItems()[0].row()
            items = table.findItems(table.search_query, QtCore.Qt.MatchStartsWith)
            for item in items:
                row = item.row()
                if row > selected_row:
                    table.clearSelection()
                    table.selectRow(row)
                    return
            if items:
                table.clearSelection()
                table.selectRow(items[0].row())

        else:
            table.search_query = query
            if query == '':
                return
            items = table.findItems(query, QtCore.Qt.MatchStartsWith)
            if items:
                table.clearSelection()
                table.selectRow(items[0].row())

    return wrapped
