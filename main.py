import requests
from base64 import b64encode
import tkinter.filedialog as fd
import pandas as pd

class InputVariablesClass:
    def __init__(self):
        ## Sup Variables
        self.op_typeSups = None
        self.sup_dec_number = None
        self.declaration_choice = None
        self.controlled_goods = None
        self.additional_procedure = None
        self.goods_domestic_status = None
        self.exporter_eori = None
        self.total_packages = None
        self.movement_type = None
        self.nationality_of_transport = None
        self.identity_no_of_transport = None
        self.postponed_vat = None
        self.freight_charge_currency = None
        self.insurance_currency = None
        self.vat_adjust_currency = None
        self.incoterm = None
        self.delivery_location_country = None
        self.delivery_location_town = None

class TraderSupportServiceAPI(InputVariablesClass):
    def __init__(self, username, password):
        super().__init__()
        usern = username
        passw = password
        userAndPass = b64encode(b"%s:%s" % (bytes(usern,  encoding='utf-8'),bytes(passw,  encoding='utf-8'))).decode("ascii")
        self.ses = requests.Session()
        self.hrs = {
                'Accept':'application/json',
                'Content-Type':'application/json',
                'Request':'application/json',
                'Authorization' : f'Basic {userAndPass}'}
        self.Endpoint = "https://api.tradersupportservice.co.uk/api/x_fhmrc_tss_api/v1/tss_api/"

    ######### Gets #########
    def getDraftSups(self):
        response = self.ses.get(self.Endpoint+"supplementary_declarations?filter=status=Draft",headers=self.hrs) 
        return response.json()

    def getSupDetails(self,supNumber):
        response = self.ses.get(self.Endpoint+f"supplementary_declarations?reference={supNumber}&fields=declaration_choice,controlled_goods,additional_procedure,goods_domestic_status,exporter_eori,arrival_date_time,total_packages,movement_type,carrier_eori,nationality_of_transport,identity_no_of_transport,postponed_vat,incoterm,delivery_location_country,delivery_location_town",headers=self.hrs)
        return response.json()

    def getGoodsInSup(self,supNumber):
        response = self.ses.get(self.Endpoint+f"goods?sup_dec_number={supNumber}",headers=self.hrs)
        return response.json()

    def getGoodDetails(self,goodsID):
        response = self.ses.get(self.Endpoint+f"goods?reference={goodsID}&fields=type_of_packages,number_of_packages,package_marks,gross_mass_kg,net_mass_kg,goods_description,invoice_number,preference,commodity_code,country_of_origin,item_invoice_amount,item_invoice_currency,procedure_code,additional_procedure_code,valuation_method,valuation_indicator,nature_of_transaction,payable_tax_currency,ni_additional_information_codes,country_of_preferential_origin,document_references,consignment_number",headers=self.hrs)
        return response.json()

    ######### Updates #########
    def updateSupDetails(self,supNumber):
        current_details = self.getSupDetails(supNumber)["result"]
        payload = {
            "op_type":"update",
            "sup_dec_number": current_details["sup_dec_number"] if self.sup_dec_number is None else self.sup_dec_number,
            "declaration_choice": current_details["declaration_choice"] if self.declaration_choice is None else self.declaration_choice,
            "controlled_goods": current_details["controlled_goods"] if self.controlled_goods is None else self.controlled_goods,
            "additional_procedure": current_details["additional_procedure"] if self.additional_procedure is None else self.additional_procedure,
            "goods_domestic_status": current_details["goods_domestic_status"] if self.goods_domestic_status is None else self.goods_domestic_status,
            "exporter_eori": current_details["exporter_eori"] if self.exporter_eori is None else self.exporter_eori,
            "total_packages": current_details["total_packages"] if self.total_packages is None else self.total_packages,
            "movement_type": current_details["movement_type"] if self.movement_type is None else self.movement_type,
            "nationality_of_transport": current_details["nationality_of_transport"] if self.nationality_of_transport is None else self.nationality_of_transport,
            "identity_no_of_transport": current_details["identity_no_of_transport"] if self.identity_no_of_transport is None else self.identity_no_of_transport,
            "postponed_vat": current_details["postponed_vat"] if self.postponed_vat is None else self.postponed_vat,
            "freight_charge_currency": current_details["freight_charge_currency"] if self.freight_charge_currency is None else self.freight_charge_currency,
            "insurance_currency": current_details["insurance_currency"] if self.insurance_currency is None else self.insurance_currency,
            "vat_adjust_currency": current_details["vat_adjust_currency"] if self.vat_adjust_currency is None else self.vat_adjust_currency,
            "incoterm": current_details["incoterm"] if self.incoterm is None else self.incoterm,
            "delivery_location_country": current_details["delivery_location_country"] if self.delivery_location_country is None else self.delivery_location_country,
            "delivery_location_town": current_details["delivery_location_town"] if self.delivery_location_town is None else self.delivery_location_town,
            }
        response = self.ses.post(self.Endpoint+"supplementary_declarations",json=payload,headers=self.hrs)
        if str(response) == "<Response [200]>":
            print("success header "+str(supNumber))
        else:
            print(str(supNumber)+" ERROR")
            print(response.json())
            print()
        return response.json()

    def updateGoodDetails(self,goodsID):
        current_details = self.getGoodDetails(goodsID)["result"]
        payload = {
        "op_type":"update",
        "goods_id": current_details["goods_id"] if self.goods_id is None else self.goods_id,
        "type_of_packages": current_details["type_of_packages"] if self.type_of_packages is None else self.type_of_packages,
        "number_of_packages": current_details["number_of_packages"] if self.number_of_packages is None else self.number_of_packages,
        "package_marks": current_details["package_marks"] if self.package_marks is None else self.package_marks,
        "gross_mass_kg": current_details["gross_mass_kg"] if self.gross_mass_kg is None else self.gross_mass_kg,
        "net_mass_kg": current_details["net_mass_kg"] if self.net_mass_kg is None else self.net_mass_kg,
        "goods_description": current_details["goods_description"] if self.goods_description is None else self.goods_description,
        "invoice_number": current_details["invoice_number"] if self.invoice_number is None else self.invoice_number,
        "preference": current_details["preference"] if self.preference is None else self.preference,
        "commodity_code": current_details["commodity_code"] if self.commodity_code is None else self.commodity_code,
        "country_of_origin": current_details["country_of_origin"] if self.country_of_origin is None else self.country_of_origin,
        "country_of_preferential_origin": current_details["country_of_preferential_origin"] if self.country_of_preferential_origin is None else self.country_of_preferential_origin,
        "item_invoice_amount": current_details["item_invoice_amount"] if self.item_invoice_amount is None else self.item_invoice_amount,
        "item_invoice_currency": current_details["item_invoice_currency"] if self.item_invoice_currency is None else self.item_invoice_currency,
        "procedure_code": current_details["procedure_code"] if self.procedure_code is None else self.procedure_code,
        "additional_procedure_code": current_details["additional_procedure_code"] if self.additional_procedure_code is None else self.additional_procedure_code,
        "valuation_method": current_details["valuation_method"] if self.valuation_method is None else self.valuation_method,
        "valuation_indicator": current_details["valuation_indicator"] if self.valuation_indicator is None else self.valuation_indicator,
        "nature_of_transaction": current_details["nature_of_transaction"] if self.nature_of_transaction is None else self.nature_of_transaction,
        "payable_tax_currency": current_details["payable_tax_currency"] if self.payable_tax_currency is None else self.payable_tax_currency,
        "ni_additional_information_codes": current_details["ni_additional_information_codes"] if self.ni_additional_information_codes is None else self.ni_additional_information_codes,
        "document_references":[{
            "op_type": "update",
            "document_code": "", 
            "document_reference": "",
            "document_reason": ""
            },
        ]
        }
        response = self.ses.post(self.Endpoint+"goods",json=payload, headers=self.hrs)
        if str(response) == "<Response [200]>":
            print("success goods "+str(current_details['consignment_number']))
        else:
            print(str(current_details['consignment_number'])+" ERROR")
            print(response.json())
            print()

        return response.json()

    ########### Post #########
    def postDeclarations(self,supNumber):
        payload = {
        "op_type":"submit",
        "sup_dec_number": supNumber
        }
        response = self.ses.post(self.Endpoint+"supplementary_declarations",json=payload, headers=self.hrs)
        if str(response) == "<Response [200]>":
            print("success header "+str(supNumber))
        else:
            print(str(supNumber)+" ERROR")
            print(response.json())
            print()
        return response.json()

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

## Run Porgram
class Main():
    def update():
        pass

    def submit():
        pass
