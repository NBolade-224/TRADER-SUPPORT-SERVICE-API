import tkinter.filedialog as fd
import pandas as pd

class ReadExcelFile:
    def __init__(self):
        self.ExcelSheet = self.openExcelSheet()

    def openExcelSheet(self):
        file = fd.askopenfilename(title='Select Excel Sheet')
        return pd.read_excel(file)

    def readSupCell(self):
        pass

    def readColCell(self):
        pass