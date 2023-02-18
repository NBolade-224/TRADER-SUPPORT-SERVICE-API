import requests
from base64 import b64encode

class TraderSupportServiceAPI:
    def __init__(self, username, password):
        usern = username
        passw = password
        userAndPass = b64encode(b"%s:%s" % (bytes(usern,  encoding='utf-8'),bytes(passw,  encoding='utf-8'))).decode("ascii")
        self.ses = requests.Session()
        self.hrs = {
                'Accept':'application/json',
                'Content-Type':'application/json',
                'Request':'application/json',
                'Authorization' : 'Basic %s' %  userAndPass
            }
        self.Endpoint = "https://api.tradersupportservice.co.uk/api/x_fhmrc_tss_api/v1/tss_api/"

    ######### Gets #########
    def getDraftSups(self):
        response = self.ses.get(self.Endpoint+"supplementary_declarations?filter=status={Draft}",headers=self.hrs) 
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
            "sup_dec_number":supNumber,
            "declaration_choice":"H1", 
            "controlled_goods":"no",
            "additional_procedure":"no",
            "goods_domestic_status":current_details["goods_domestic_status"],
            "exporter_eori":current_details["exporter_eori"],
            "total_packages":current_details["total_packages"],
            "movement_type":current_details["movement_type"],
            "nationality_of_transport":current_details["nationality_of_transport"],
            "identity_no_of_transport":current_details["identity_no_of_transport"],
            "postponed_vat":current_details["postponed_vat"],
            "freight_charge_currency":"GBP",
            "insurance_currency":"GBP",
            "vat_adjust_currency":"GBP",
            "incoterm":"DDP",
            "delivery_location_country":current_details["delivery_location_country"],
            "delivery_location_town":current_details["delivery_town"]
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
        "goods_id":goodsID,
        "type_of_packages":current_details['type_of_packages'],
        "number_of_packages":current_details['number_of_packages'],
        "package_marks":current_details['package_marks'],
        "gross_mass_kg":current_details['gross_mass_kg'],
        "net_mass_kg":current_details['gross_mass_kg'], 
        "goods_description":current_details['goods_description'],
        "invoice_number":int(current_details['invoice_number']), 
        "preference":"300", 
        "commodity_code":current_details['commodity_code'],
        "country_of_origin":"GB", 
        "country_of_preferential_origin":"GB", 
        "item_invoice_amount":current_details['item_invoice_amount'],
        "item_invoice_currency":"GBP",
        "procedure_code":"4000", 
        "additional_procedure_code":current_details['additional_procedure_code'],
        "valuation_method":current_details['valuation_method'],
        "valuation_indicator":current_details['valuation_indicator'],
        "nature_of_transaction":current_details['nature_of_transaction'],
        "payable_tax_currency":current_details['payable_tax_currency'],
        "ni_additional_information_codes":"TCA",
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
