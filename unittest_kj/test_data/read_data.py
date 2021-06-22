import  xlrd

class ReadData():

    def read_data(self):
        list_xpth=[]
        da=xlrd.open_workbook(r"C:\Users\wanglei\Desktop\python\data.xls")
        table=da.sheet_by_index(0)
        for i in range(1,table.ncols):
            list_xpth.append(table.col_values(i))
            return list_xpth

print(ReadData().read_data())

