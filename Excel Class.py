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


# DraftSUPs = ses.get("https://api.tradersupportservice.co.uk/api/x_fhmrc_tss_api/v1/tss_api/supplementary_declarations?filter=status=%s" % StatusFilter,headers=hrs)                     ##### THIS IS A LIST OF ALL SUP REFERENCES
# SUPDecList = DraftSUPs.json()['result'] 
# PandasDict = {"SupDec":[],"PO_Number":[],"Goodsid":[],"Item_Description":[],"PackageMark":[],"Commodity_Code":[],"Item Gross Mass (KG)":[],"Item Price / Amount":[],"Number of Packages":[],"Arrival Date":[]}

# for current_iter, each_sup in enumerate(SUPDecList):
#     print(str(each_sup['number'])+" "+str(current_iter+1)+"/"+str(len(SUPDecList)))
#     print()
#     List_Of_All_Goods_In_A_Sup = apiCall("https://api.tradersupportservice.co.uk/api/x_fhmrc_tss_api/v1/tss_api/goods?sup_dec_number=%s" % each_sup['number'])['goods']
#     Sup_details = apiCall("https://api.tradersupportservice.co.uk/api/x_fhmrc_tss_api/v1/tss_api/supplementary_declarations?reference=%s&fields=arrival_date_time,status,trader_reference,movement_reference_number" % each_sup['number'])

#     for each_good in List_Of_All_Goods_In_A_Sup:
#         Good_Details = apiCall("https://api.tradersupportservice.co.uk/api/x_fhmrc_tss_api/v1/tss_api/goods?reference=%s&fields=gross_mass_kg,commodity_code,item_invoice_amount,number_of_packages,package_marks,goods_description" % each_good['goods_id']) #&fields=gross_weight_kg,commodity_code,item_invoice_amount,additional_information
#         PandasDict['SupDec'].append(each_sup['number'])
#         PandasDict['Goodsid'].append(each_good['goods_id'])
#         PandasDict['Item_Description'].append(Good_Details['goods_description'])
#         PandasDict['PackageMark'].append(Good_Details['package_marks'])
#         PandasDict['Commodity_Code'].append(Good_Details['commodity_code'])
#         PandasDict['Item Gross Mass (KG)'].append(Good_Details['gross_mass_kg'])
#         PandasDict['Item Price / Amount'].append(Good_Details['item_invoice_amount'])
#         PandasDict['Number of Packages'].append(Good_Details['number_of_packages'])
#         PandasDict['Arrival Date'].append(Sup_details['arrival_date_time']) 
#         PandasDict['PO_Number'].append(Sup_details['trader_reference']) 
    
# df = pd.DataFrame(PandasDict)
# df.to_excel("C:\\Users\\nick.bolade\\Desktop\\TSS Showcase Mark Ralph\\TSS Data Export %s %s.xlsx" % (StatusFilter,datetime.today().strftime("%Y%m%d %H%M%S")))
# return "C:\\Users\\nick.bolade\\Desktop\\TSS Showcase Mark Ralph\\TSS Data Export %s %s.xlsx" % (StatusFilter,datetime.today().strftime("%Y%m%d %H%M%S")) 



# Passed_TSS_File = pd.read_excel(fd.askopenfilename(title='Select TSS export'))
# Passed_TSS_Data_Sum = Passed_TSS_File.groupby(["SupDec","PO_Number","Item_Description","Commodity_Code","Item Gross Mass (KG)"], as_index=False)["Item Price / Amount"].sum()

# Passed_DDI_File = pd.read_excel(fd.askopenfilename(title='Select Combined Manifest export'))
# Passed_DDI_File['Commodity_Code'] = Passed_DDI_File['Commodity_Code'].replace(np.nan, 0)
# Passed_DDI_File_Sum = Passed_DDI_File.groupby(["PO_Number","Postcode","Item_Description","Commodity_Code"], as_index=False)["Item_Invoice_Amount","Weight_Per_Item"].sum()

# result = pd.merge(Passed_TSS_Data_Sum, Passed_DDI_File_Sum, how="left", on=["PO_Number", "Item_Description"], validate="one_to_one").replace(np.nan, "blank")

# towns = []

# for index, x in result.iterrows():
#     towns.append(getTown(x))

# result["Town"] = towns
# result.to_excel("C:\\Users\\nick.bolade\\Desktop\\TSS Showcase Mark Ralph\\TSS and Manifest Data Joined %s.xlsx" % datetime.today().strftime("%Y%m%d %H%M%S"))