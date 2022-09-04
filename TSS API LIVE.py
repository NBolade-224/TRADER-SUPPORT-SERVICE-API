import requests, time
from base64 import b64encode

usern ="Username goes here"
passw = "Password goes here"
userAndPass = b64encode(b"%s:%s" % (usern,passw)).decode("ascii")
ses = requests.Session()
hrs = {
'Accept':'application/json',
'Content-Type':'application/json',
'Request':'application/json',
'Authorization' : 'Basic %s' %  userAndPass
}
#############################################################
#############################################################

#############################################################
## LIST ALL INVOICES FOR ALL ###
#############################################################
DraftSUPs = ses.get("https://api.tradersupportservice.co.uk/api/x_fhmrc_tss_api/v1/tss_api/supplementary_declarations?filter=status=draft",headers=hrs)                     ##### THIS IS A LIST OF ALL SUP REFERENCES
SUPDecList = DraftSUPs.json()['result']
Decs = []  
for y in SUPDecList:
    Decs.append(y['number'])
l = 1
nn = len(Decs)
listofduplicates = []
finallist = []
for z in Decs:
    st = time.time()
    Gd = ses.get("https://api.tradersupportservice.co.uk/api/x_fhmrc_tss_api/v1/tss_api/goods?sup_dec_number=%s" % z,headers=hrs)
    ls = Gd.json()['result']['goods'] ## LIST OF ALL GOODS IN A SUP DEC
    k = 1      
    for x in ls:
        Td = ses.get("https://api.tradersupportservice.co.uk/api/x_fhmrc_tss_api/v1/tss_api/goods?reference=%s&fields=invoice_number" % x['goods_id'],headers=hrs)
        if str(Td.json()['result']['invoice_number']) in listofduplicates:
            print(str(Td.json()['result']['invoice_number'])+"   "+str(z)+"    Sup %d/%d" % (l, nn) + " DUPLICATE FOUND "+str(listofduplicates.index(str(Td.json()['result']['invoice_number']))+1))
            listofduplicates.append(str(Td.json()['result']['invoice_number']))
            finallist.append(str(Td.json()['result']['invoice_number'])+"   "+str(z)+"    Sup %d/%d" % (l, nn) + " DUPLICATE FOUND "+str(listofduplicates.index(str(Td.json()['result']['invoice_number']))+1))
            k += 1
            continue
        print(str(Td.json()['result']['invoice_number'])+"   "+str(z)+"    Sup %d/%d" % (l, nn))
        listofduplicates.append(str(Td.json()['result']['invoice_number']))
        finallist.append(str(Td.json()['result']['invoice_number'])+"   "+str(z)+"    Sup %d/%d" % (l, nn))
        if str(Td) == "<Response [200]>":
            pass
        else:
            print("Error - Check Code")
            break
        k += 1
    l += 1
    #ed = time.time()
    #print(ed - st)
print("BREAK")
print("BREAK")
print("BREAK")
finallist.sort(key=lambda x: int(''.join(filter(str.isdigit, x[:19]))))
for x in finallist:
    print(x)
##############################################################
#### Remove all goods except for one script ####
##############################################################
# Gu = "https://api.tradersupportservice.co.uk/api/x_fhmrc_tss_api/v1/tss_api/goods"
# DraftSUPs = ses.get("https://api.tradersupportservice.co.uk/api/x_fhmrc_tss_api/v1/tss_api/supplementary_declarations?filter=status=draft",headers=hrs)                     ##### THIS IS A LIST OF ALL SUP REFERENCES
# SUPDecList = DraftSUPs.json()['result']
# Decs = []  
# for y in SUPDecList:
#     Decs.append(y['number'])
# l = 1
# nn = len(Decs)
# for z in Decs:
#     st = time.time()
#     Gd = ses.get("https://api.tradersupportservice.co.uk/api/x_fhmrc_tss_api/v1/tss_api/goods?sup_dec_number=%s" % z,headers=hrs)
#     ls = Gd.json()['result']['goods'] ## LIST OF ALL GOODS IN A SUP DEC
#     if len(ls) > 1: 
#         k = 1
#         jj = len(ls) - 1        
#         for x in ls[:-1]:
#             tp = {
#             "op_type":"delete",
#             "goods_id":"%s" % x['goods_id']
#             }
#             Td = ses.post(Gu,json=tp,headers=hrs)        
#             print(str(Td)+"Sup %d/%d - Good %d/%d" % (l, nn, k, jj))
#             if str(Td) == "<Response [200]>":
#                 pass
#             else:
#                 print("Error - Check Code")
#                 break
#             k += 1
#     else:
#         pass
#     l += 1
#     ed = time.time()
#     print(ed - st)
#     time.sleep(0)

##############################################################
######### UPLOAD GOODS TO A SPECIFIED CONSIGNMENT (SFD)#######
##############################################################


# for x in range(99):
#     ToPostGoodCreate = {
#     "op_type":"create",
#     "consignment_number":"DEC000000001007622",
#     "goods_id":"",
#     "equipment_number":"",
#     "un_dangerous_goods_code":"",
#     "type_of_packages":"boxes",
#     "number_of_packages":"1",
#     "number_of_individual_pieces":"",
#     "package_marks":"ADDR",
#     "gross_mass_kg":"2",
#     "net_mass_kg":"",
#     "goods_description":"TEST %s" % x,
#     "invoice_number":"",
#     "controlled_goods":"no",
#     "controlled_goods_type":"",
#     "commodity_code":"",
#     "country_of_origin":"",
#     "item_invoice_amount":"",
#     "item_invoice_currency":"",
#     "procedure_code":"",
#     "additional_procedure_code":"",
#     "taric_code":"",
#     "cus_code":"",
#     }
#     TestPost = ses.post("https://api.tsstestenv.co.uk/api/x_fhmrc_tss_api/v1/tss_api/goods",json=ToPostGoodCreate,headers=hrs)        
#     print(TestPost)
#     print(TestPost.json())

