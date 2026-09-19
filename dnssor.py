import subprocess
import re
from tld import queryy
import tldextract
from threading import Timer
from _socket import timeout

temp = []

with open("deneme.txt") as f:
    domain_all = f.read().splitlines()

for domain in domain_all:
    domain = tldextract.extract(domain)
    domain = "{}.{}".format(domain.domain, domain.suffix)
    domain_all = set(domain)
    if domain not in temp:
        temp.append(domain)

try:
    temp.remove('.') 
except:
    pass

print(temp)


yaz = open("yaz.txt", "w")
tyaz = open("trhyaz.txt", "w")


for domain in temp:
    
    print(domain)
    
    tld= queryy(domain)
    
    def whois(ip,name):
        p = subprocess.Popen(['whois', ip], stdout=subprocess.PIPE)
        out, err = p.communicate()
        m = re.search(tld.get(name), out.decode('ISO-8859-9'))
        return m.group(1)
    
    def whois_server(ip,name):
        p = subprocess.Popen(['whois', ip], stdout=subprocess.PIPE)
        out, err = p.communicate()
        try: m = re.findall(tld.get(name), out.decode('ISO-8859-9'))
        except: m = re.findall(tld.get(name), out.decode('ISO-8859-9')).group(1)
    
        return m


    yaz.write("\n" + domain + "\n")

    for k in tld:
        
        if(str(k) == "name_servers"):
            try:
                x = str(whois_server(domain, k))
                y = str(k) + "---> " + x
                print(y)
                yaz.write(y + "\n")
            
            except:
                print("No info on " + str(k))
        
        else:
            try:
                a = whois(domain, k)
                b = str(k) + "---> "+ a
                print(b)
                yaz.write(b + "\n")
            
            except:
                print("No info on " + str(k))
            
            if(str(k)== "expiration_date"):
                try:
                    tyaz.write(domain + "\n")
                    tyaz.write(a + "\n\n")
                except: pass
            
        

tyaz.close()



