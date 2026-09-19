import uzanti

def queryy(domain):
        domain = domain.lower().strip().rstrip('.')  # Remove the trailing dot to support FQDN.
        d = domain.split('.')
        if d[0] == 'www':
            d = d[1:]
        if len(d) == 1:
            return None
        
        if domain.endswith('.ac.uk') and len(d) > 2:
            tld = uzanti.ac_uk
        elif domain.endswith('co.il') and len(d) > 2:
            tld = uzanti.co_il
        elif domain.endswith('.com.au') and len(d) > 2:
            tld = uzanti.au
        elif domain.endswith('com.tr') and len(d) > 2:
            tld = uzanti.com_tr
        elif domain.endswith('bel.tr') and len(d) > 2:
            tld = uzanti.gov_tr
        elif domain.endswith("gov.tr") and len(d)> 2:
            tld = uzanti.gov_tr
            
        elif domain.endswith('.frl' or '.game' or '.ink' or '.link' or '.pub' or '.sale' or 'amsterdam' or
                             '.security' or '.site' or '.space' or '.store' or '.tech' or '.theatre' or '.tickets' or '.trade' or '.website'):
            tld= uzanti.store    
            
        
        elif domain.endswith('.com' or '.fm' or '.ie' or '.in' or '.info' or '.net' or '.pro' or '.study' or '.za' or '.istanbul' or 'ist' or 'ca' or 'courses'):
            tld= uzanti.com
            
            
            
        elif domain.endswith('am'):
            tld = uzanti.am
        elif domain.endswith('.ar'):
            tld= uzanti.ar
        elif domain.endswith('.at'):
            tld= uzanti.at
        elif domain.endswith('.au'):
            tld= uzanti.au
        elif domain.endswith('.aw'):
            tld= uzanti.aw
        
        elif domain.endswith('.be'):
            tld= uzanti.be
        elif domain.endswith('biz'):
            tld = uzanti.biz
        elif domain.endswith('.br'):
            tld= uzanti.br
        elif domain.endswith('.by'):
            tld= uzanti.ar
            
        elif domain.endswith('.cc'):
            tld= uzanti.at
        elif domain.endswith('.cl'):
            tld= uzanti.cl
        elif domain.endswith('.cn'):
            tld= uzanti.cn
        elif domain.endswith('.co'):
            tld= uzanti.co
        elif domain.endswith('.cz'):
            tld= uzanti.cz
        elif domain.endswith('.cr'):
            tld= uzanti.cz
        
        
        elif domain.endswith('.de'):
            tld= uzanti.de
        elif domain.endswith('.download'):
            tld= uzanti.download
            
            
        elif domain.endswith('.edu'):
            tld= uzanti.edu
        elif domain.endswith('education'):
            tld= uzanti.education
        elif domain.endswith('.eu'):
            tld= uzanti.eu
            
            
        elif domain.endswith('.fi'):
            tld= uzanti.fi
        elif domain.endswith('.fr'):
            tld= uzanti.fr
        
        
        elif domain.endswith('.global'):
            tld= uzanti.global_
            
            
        elif domain.endswith('.hk'):
            tld= uzanti.hk
        
        
        elif domain.endswith('.id'):
            tld= uzanti.id_
        elif domain.endswith('.im'):
            tld= uzanti.im
        elif domain.endswith('.io'):
            tld= uzanti.io
        elif domain.endswith('.ir'):
            tld= uzanti.ir
        elif domain.endswith('.is'):
            tld= uzanti.is_
        elif domain.endswith('.it'):
            tld= uzanti.it
            
            
        elif domain.endswith('.kr'):
            tld= uzanti.kr
        elif domain.endswith('.kz'):
            tld= uzanti.kz
        
        
        elif domain.endswith('.lt'):
            tld= uzanti.lt
        elif domain.endswith('.lv'):
            tld= uzanti.lv
        
        elif domain.endswith('.me'):
            tld= uzanti.me
        elif domain.endswith('.ml'):
            tld= uzanti.ml
        elif domain.endswith('.mobi'):
            tld= uzanti.mobi
        elif domain.endswith('.mx'):
            tld= uzanti.mx
        
        
        elif domain.endswith('.name'):
            tld= uzanti.name
        elif domain.endswith('.ninja'):
            tld= uzanti.education
        elif domain.endswith('.nl'):
            tld= uzanti.nl
        elif domain.endswith('.nu'):
            tld= uzanti.se
        elif domain.endswith('.nyc'):
            tld= uzanti.nyc
        elif domain.endswith('.nz'):
            tld= uzanti.nz
            
            
        elif domain.endswith('.online'):
            tld= uzanti.online
        elif domain.endswith('.org'):
            tld= uzanti.org
            
            
        elif domain.endswith('.pe'):
            tld= uzanti.pe
        elif domain.endswith('.pharmacy'):
            tld= uzanti.pharmacy
        elif domain.endswith('.pl'):
            tld= uzanti.pl
        elif domain.endswith('.press'):
            tld= uzanti.press
        elif domain.endswith('.pt'):
            tld= uzanti.pt
        elif domain.endswith('.pw'):
            tld= uzanti.pw
        
        
        elif domain.endswith('.rest'):
            tld= uzanti.rest
        elif domain.endswith('.ru'):
            tld= uzanti.ru
        elif domain.endswith('.ru_rf'):
            tld= uzanti.ru_rf
        
        
        elif domain.endswith('.sh'):
            tld= uzanti.sh
        elif domain.endswith('.se'):
            tld= uzanti.se
        
        elif domain.endswith('.tel'):
            tld= uzanti.tel
        elif domain.endswith('.tv'):
            tld= uzanti.tv
        
        
        elif domain.endswith('.ua'):
            tld= uzanti.ua
        elif domain.endswith('.uk'):
            tld= uzanti.uk
        elif domain.endswith('.us'):
            tld= uzanti.name
        elif domain.endswith('.uz'):
            tld= uzanti.uz
            
            
        elif domain.endswith('.video'):
            tld= uzanti.video
        elif domain.endswith('.wiki'):
            tld= uzanti.wiki
        elif domain.endswith('.work'):
            tld= uzanti.work
        elif domain.endswith('.xyz'):
            tld= uzanti.xyz
        
        else:
            tld= uzanti.store
            
        return tld
    
    
    