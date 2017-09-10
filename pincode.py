import pandas as pd
import csv
import re


path="D:/a/april_deck/hdfc_doc/offers_may/offersupdated_may17/"
file="store_offers_may17_2.csv"



file1=pd.read_csv(path + file)
file1.keys()

def pin(add):
    pin=[]
    pincode=[]
    for each in add.split():
        try:
            pin = each[re.search("\\d{6}",each).start():re.search("\\d{6}",each).end()]
            if len(pin) ==6 or len(pin) == 7:
                pincode.append(pin)
        except:
            pin=''
    return pincode
	
addd="No.1/6 Ground Floor,Shop No.7, Ratanlal Plot,Akola-444 001 tuhee adas 12332 asad "


pincod=[]
for i in range(0,file1.shape[0]):
    try :
        pincod.append(pin(str(file1['merchantaddress'].iloc[i])))
    except:
        pincod=''
    
	
	