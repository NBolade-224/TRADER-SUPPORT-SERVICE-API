import tkinter.filedialog as fd
import pandas as pd

class ReadExcelFile:
    def __init__(self):
        file = fd.askopenfilename(title='Select Excel Sheet')
        self.Excelfile = pd.read_excel(file)
        self.NumberOfRows = len(self.Excelfile)
        self.ColumnNames = self.Excelfile.columns.values

    def getEntireColumn(self,columnName: str) -> list:
        return self.Excelfile[columnName].values
    
    def getEntireRow(self,rowIndex: int) -> object:
        return self.Excelfile.iloc[rowIndex]



# df = pd.read_excel("C:\\Users\\nickb\\Desktop\\New folder\\PROJECTS\\TRADER-SUPPORT-SERVICE-API\\TestData1.xlsx")

# ## Get list of rows in Excel File
# print(df.columns.values)
# print()

# ## Get list of Values in column
# print(df["Row Labels"].values)
# print()

## get list of values for each column
# for x in df.columns.values:
#     print(list(df[x].values))
#     print()

# ## get object of current Row
# print(df.iloc[0]['Row Labels'])

## get Len of all rows#
#print(len(df))s