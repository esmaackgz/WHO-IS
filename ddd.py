import subprocess
import re

adres = raw_input("Sorgu yapacaginiz ip adresini giriniz:")

dosya = open("yaz.txt", "a")

def whois(ip,name):
    p = subprocess.Popen(['whois', ip], stdout=subprocess.PIPE)
    out, err = p.communicate()
    m = re.search('{}[\.\n]*:\s+[\d\w\@\.\-\:\ ]+'.format(name), out)
    return m.group(0)

expirydate= ["Registry Expiry Date", "Expires on"]
creationdate= ["Creation Date", "Created on"]
dnsname = [ "Name Server", "Domain Servers"]
registrarname=["Registrar", "Registrant"]
registrantorg= ["Registrant Organization", "Organization Name"]
address= ["Registrant State/Province", "Address"]

"""boyutt= expirydate.__len__()
if (creationdate.__len__()> boyutt):
    boyutt == creationdate.__len__()
if(dnsname.__len__()> boyutt):
    boyutt == dnsname.__len__()
"""


for i in range(creationdate.__len__()):
    try:
        print(whois(adres, creationdate[i]))
        dosya.write(whois(adres, creationdate[i]))
    except: continue
    
    try:
        print(whois(adres, expirydate[i]))
        dosya.write(whois(adres, expirydate[i]))
    except: continue
        
    try:
        print(whois(adres, dnsname[i]))
        dosya.write(whois(adres, dnsname[i]))
    except: continue
    
    try:
        print(whois(adres, registrarname[i]))
        dosya.write(whois(adres, registrarname[i]))
    except: continue
    
    try:
        print(whois(adres, registrantorg[i]))
        dosya.write(whois(adres, registrantorg[i]))
    except: continue
    
    try:
        print(whois(adres, address[i]))
        dosya.write(whois(adres, address[i]))
    except: continue
        
print("finish")
