import re
import socket
from dns import resolver
#import dnssor


oku = open("ipwrite.txt", "r")
metin = oku.readlines()
print metin
oku.close()

yaz = open("ipwrite.txt", "w")

dns_list = []

with open("yaz.txt", "r") as f:
    content = f.read()

pattern = "([0-9a-zA-Z\.]+\.[a-zA-Z\.]+\.[a-zA-Z\.]+\.*[a-zA-Z\.]+\.*[a-zA-Z\.])"
check = re.findall(pattern, content, re.MULTILINE)
for i in check:
    i= i.upper()
    if i not in dns_list:
        dns_list.append(i)  

#print dns_list

res = resolver.Resolver()
res.nameservers = ['8.8.8.8']

for i in dns_list:
    answer = res.query(i)
    for r in answer:
        #print("Domain: "+ i +" IP: " +r.address)
        yaz.write("Domain: "+ i +" IP: " +r.address +"\n")

yaz.close()

klm = open("ipwrite.txt", "r")
kelime = klm.readlines()
print kelime
for i in kelime:
    if i in metin:
        print i +"vardir."
    else:
        print i+ "Domain not excist"
    

"""
if( metin.find(dizi[1]) != -1 ):
        print 

if dizi[1] in metin and dizi[3] in metin:
        print ""
"""

"""
if (metin != None ):
    satir = oku.readlines()
    print satir
    dizi = satir.split(" ")
    kelime = dizi[1]
    if ( metin.find(kelime) != -1):
        print kelime + " Domain excist"
    else:
        print kelime + "Domain not exist"
"""
#([0-9\-\.]+[0-9\-]+[0-9\-]+[0-9\-\.]+)


"""    
for i in metin:
    i = i.rstrip("\n")
    print i
    dizi = i.split(" ")
    
    
print dizi"""
"""
for i in metin:
    index = i.find("TR")
    if (index != -1):
        print i
    """
    