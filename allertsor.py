import datetime
import string
import Tkinter as tk
import tkMessageBox



zaman = datetime.datetime.today()
print("Today: ")
print(zaman)
print("")

logla = open("log.txt","r")
oku = open("tarih.txt","r")
dizi = oku.readlines()
i= 0

for s in dizi:
        adres = s.rstrip("\n")
        
        if( i %2 == 0):
            print(adres)
            adrs = adres
        else:
            dizit = adres.split(": ")
            print(dizit[1])
            a = dizit[1]
            try:
                tarih = datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S CLST')
            except:
                tarih = datetime.datetime.strptime(a, '%Y-%m-%dT%H:%M:%SZ')
            
            
            simdi = datetime.datetime.today()
            kalanay = tarih-simdi
            print(kalanay)
            
            datetimeString = str(kalanay)
            time_parse = datetimeString.split("days")
            #print(time_parse)
            days = time_parse[0]
            
            if( int(days) <= 30):
                root = tk.Tk()
                root.withdraw()
                tkMessageBox.showwarning(adrs, 'Domain expired!')

            
            
        print("")    
        i+=1
        

        
        
        