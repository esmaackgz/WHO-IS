from datetime import datetime
import re
import smtplib

toku= open("trhyaz.txt","r")
dizit = toku.readlines()
print(dizit)


gonderici_mail = ''
gonderici_sifre = ''
alicilar = ['']


pattern = "\d{4}[/.-]\w{2,3}[/.-]\d{2}|\d{8}|\d{1,2}[/.-]\w{1,3}[/.-]\d{4}|\w{1,4}[ ]\w{2,3}[ ]\d{4}"
mesaj = ""
i= 0
for s in dizit:
    satir = s.rstrip("\n")
    
    
    dates = re.findall(pattern,satir)
    #print(dates)
    if (i % 3 == 0):
        mesaj2 = satir +"\n"
        
    if(i % 3 == 1):
        try:
            tarih = datetime.strptime(dates[0], '%Y-%m-%d')
        except ValueError:
            try:
                tarih = datetime.strptime(dates[0], '%Y.%m.%d')
            except ValueError:
                try:
                    tarih = datetime.strptime(dates[0], '%Y%m%d')
                except ValueError:
                    try:
                        tarih = datetime.strptime(dates[0], '%d-%b-%Y')
                    except ValueError:
                        try:
                            tarih = datetime.strptime(dates[0], '%d.%m.%Y')
                        except:
                            tarih = datetime.strptime(dates[0], '%Y-%b-%d')
            
        

        kalanay = tarih - datetime.today()
        #print kalanay
        datetimeString = str(kalanay)
        time_parse = datetimeString.split("days")

        days = time_parse[0]

        #print mesaj2+ " Kalan : " + days + "days \n"
        
        if( int(days) <= 150):
            mesaj += mesaj2
            message = " Kalan : " + days + "days \n"
            mesaj +=  message
        

    i += 1
print mesaj


server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(gonderici_mail, gonderici_sifre)
server.sendmail(gonderici_mail, alicilar, mesaj)
server.quit()


