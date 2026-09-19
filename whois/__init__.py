import subprocess
import re
from twisted.protocols.wire import Who
from warnings import catch_warnings
from compiler.ast import GenExprInner

adres = raw_input("Sorgu yapacaginiz ip adresini giriniz:")

def whois(ip,name):
    p = subprocess.Popen(['whois', ip], stdout=subprocess.PIPE)
    out, err = p.communicate()
    m = re.search('{}:\s+[\d\w\@\.\-\:\ ]+'.format(name), out)
    return m.group(0)

expirydate= ["Expires on", "Registry Expiry Date"]
creationdate= ["Created on", "Creation Date","Created", "created"]

for i in range(expirydate.__len__()):
    try:
        print(whois(adres, expirydate[i]))
    except:
        print("bir hata olustu.")

for i in range(creationdate.__len__()):
    try: 
        print(whois(adres, creationdate[i]))
    except:
        print("hata kodu :2")

for i in range:
    

try:
    print(whois(adres, "dns"))

"""from warnings import filterwarnings

filterwarnings( action="ignore")
from ipwhois import IPWhois
obj = IPWhois('74.125.225.229')
obj.lookup_whois()



print(whois("213.180.204.3", ' '))

"""
