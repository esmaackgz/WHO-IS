com = { #ca, courses

    'domain_name':               r'Domain Name:\s?(.+)',

    'registrar':                 r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':        r'Registrant Country:\s?(.+)',

    'creation_date':             r'Creation Date:\s?(.+)',
    'expiration_date':           r'Registry Expiry Date:\s?(.+)',
    'updated_date':              r'Updated Date:\s?(.+)',

    'name_servers':              r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}


gov_tr = {
    'domain_name':               r'\*\* Domain Name:\s?(.+)',

    'creation_date':             r'Created on..............:\s?(.+).',
    'expiration_date':           r'Expires on..............:\s?(.+).',
    
    'name_servers':              r'\*\* Domain Servers:\n*(.+)\s(.*)',
    'registrar':                 r'Organization Name\s+:\s?(.+)',
    'registrant':                r'\*\* Registrant:\s+?(.+)',
}

com_tr = {
    
    'domain_name':          r'\*\* Domain Name:\s?(.+)',

    'registrar':            r'Organization Name\s+:\s?(.+)',
    'registrant':           r'\*\* Registrant:\s+?(.+)',


    'creation_date':        r'Created on..............:\s?(.+).',
    'expiration_date':      r'Expires on..............:\s?(.+).',

    
    'name_servers':         r'\*\* Domain Servers:\n(?:(\S+)\n)(?:(\S+)\n)?(?:(\S+)\n)?(?:(\S+)\n)?',
    

#(\d{1,3}[.](?:\d{1,3})[.](?:\d{1,3})[.](?:\d{1,3}))
}


ac_uk = {
    'domain_name':              r'Domain:\n\s?(.+)',

    'owner':                    r'Domain Owner:\n\s?(.+)',
    'registrar':                r'Registered By:\n\s?(.+)',
    'registrant':               r'Registered Contact:\n\s*(.+)',
    
    'expiration_date':          r'Renewal date:\n\s*(.+)',
    'updated_date':             r'Entry updated:\n\s*(.+)',
    'creation_date':            r'Entry created:\n\s?(.+)',
    'name_servers':             r'Servers:\s*(.+)\t\n\s*(.+)\t\n',

}

am = {
    'domain_name':              r'Domain name:\s+(.+)',
    'status':                   r'Status:\s(.+)',

    'registrar':                r'Registrar:\s+(.+)',
    'registrant':               r'Registrant:\s+(.+)',
    'registrant_country':       r'Registrant:\n.+\n.+\n.+\n\s+(.+)',

    'creation_date':            r'Registered:\s+(.+)',
    'expiration_date':          r'Expires:\s+(.+)',
    'updated_date':             r'Last modified:\s+(.+)',

    'name_servers':             r'DNS servers.*:\n(?:\s+(\S+)\n)(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?(?:\s+(\S+)\n)\n?',
}

amsterdam = { #store,

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'updated_date':             r'Updated Date:\s?(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s*(.+)',
}

ar = {
    'domain_name':              r'domain\s*:\s?(.+)',

    'registrar':                r'registrar:\s?(.+)',

    'creation_date':            r'registered:\s?(.+)',
    'expiration_date':          r'expire:\s?(.+)',
    'updated_date':             r'changed\s*:\s?(.+)',

    'name_servers':             r'nserver:\s*(.+)\s*',
}

at = {

    'domain_name':              r'domain:\s?(.+)',

    'updated_date':             r'changed:\s?(.+)',

    'name_servers':             r'nserver:\s*(.+)',
}

au = { #com_au
    'registrar':                r'Registrar Name:\s?(.+)',
    'registrant':               r'Registrant:\s+(.+)',
    
    'updated_date':             r'Last Modified:\s?(.+)',
    
    'status':                   r'Status:\s?(.+)',
    'domain_name':              r'Domain Name:\s?(.+)',
    'name_servers':             r'Name Server:\s*(.+)\s*',
}

aw = { #nl
    'creation_date':            r'Creation Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
    
    'expiration_date':          None,
    'registrant_country':       None,
    'registrar':                r'Registrar:\s?(.+)',
    'domain_name':              r'Domain name:\s?(.+)',
    'name_servers':             (
        r'''(?x:
            Domain\ nameservers:[ \t]*\n
            (?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n       # ns1.tld.nl [A?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns2.tld.nl [A?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns2.tld.nl [AAAA?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns3.tld.nl [A?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns3.tld.nl [AAAA?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns4.tld.nl [A?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns4.tld.nl [AAAA?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns5.tld.nl [A?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns5.tld.nl [AAAA?]
            # Don't check for final LF; there might be even more records..
        )'''),

    'abuse_contact':            r'Abuse Contact:\s?(.+)',
}

be = {

    'domain_name':              r'\nDomain:\s*(.+)',
    'name_servers':             r'Name Servers:\s*(.+)\s*',
    'registrar':                r'Name:\n?(.+)',

    'creation_date':            r'Registered:\s*(.+)\n',

    'status':                   r'Status:\s?(.+)',
}

biz = {
    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)\s*',

    'status':                   None,
}

br = {
    'domain_name':              r'domain:\s?(.+)',

    'registrar':                'nic.br',
    'registrant':               None,
    'owner':                    r'owner:\s?(.+)',

    'creation_date':            r'created:\s?(.+)',
    'expiration_date':          r'expires:\s?(.+)',
    'updated_date':             r'changed:\s?(.+)',

    'name_servers':             r'nserver:\s*(.+)',
    'status':                   r'status:\s?(.+)',
}

by = {

    'domain_name':              r'Domain Name:\s*(.+)',
    'registrar':                r'\nRegistrar:\s*(.+)',
    'registrant':               r'\nOrg:\s*(.+)',
    'registrant_country':       r'\nCountry:\s*(.+)',

    'creation_date':            r'\nCreation Date:\s*(.+)',
    'expiration_date':          r'\nExpiration Date:\s*(.+)',
    'updated_date':             r'\nUpdated Date:\s*(.+)',

    'name_servers':             r'\nName Server:\s*(.+)',
}

cc = {
    'domain_name':              r'Domain Name:\s?(.+)',

    'registrant':               r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    
    'name_servers':             r'Name Server:\s*(.+)\s*',
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   r'Status:\s?(.+)',
    'emails':                   r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

cl = {
    'domain_name':              r'Domain name:\s?(.+)',
    'registrar':                'nic.cl',
    'registrant':               r'Registrant\s*organi(?:s|z)ation:\s?(.+)',
    
    'creation_date':            r'Creation date:\s?(.+)',
    'expiration_date':          r'Expiration date:\s?(.+)',
    
    'name_servers':             r'Name server:\s*(.+)\s*',
}

cn = {
    'registrar':                r'Sponsoring Registrar:\s?(.+)',
    'registrant':               r'Registrant:\s?(.+)',
    'emails':                   r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
    'creation_date':            r'Registration Time:\s?(.+)',
    'expiration_date':          r'Expiration Time:\s?(.+)',
}

co = {
    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
    
    'status':                   r'Status:\s?(.+)',
}


co_il = {
    'domain_name':              r'domain:\s*(.+)',
    'registrar':                r'registrar name:\s*(.+)',
    'registrant':               None,
    'registrant_country':       None,

    'creation_date':            None,
    'expiration_date':          r'validity:\s*(.+)',
    'updated_date':             None,

    'name_servers':             r'nserver:\s*(.+)',
    'status':                   r'status:\s*(.+)',
}


cz = {#cr
    'domain_name':              r'domain:\s?(.+)',
    'registrar':                r'registrar:\s?(.+)',
    'registrant':               r'registrant:\s?(.+)',

    'creation_date':            r'registered:\s?(.+)',
    'expiration_date':          r'expire:\s?(.+)',
    'updated_date':             r'changed:\s?(.+)',

    'name_servers':             r'nserver:\s*(.+) ',
}

de = {

    'domain_name':              r'\ndomain:\s*(.+)',

    'updated_date':             r'\nChanged:\s?(.+)',

    'name_servers':             r'Nserver:\s*(.+)',
}

download = {

    'name_servers':             r'Name Server:\s*(.+)\r',
    'status':                   r'Domain Status:\s*([a-zA-z]+)',
}


edu = {

    'registrant':               r'Registrant:\s*(.+)',

    'creation_date':            r'Domain record activated:\s?(.+)',
    'updated_date':             r'Domain record last updated:\s?(.+)',
    'expiration_date':          r'Domain expires:\s?(.+)',

    'name_servers':             r'Name Servers:\s?\t(.+)\n\t(.+)\n',
}


education = {
    # GANDI SAS
    'extend': 'com',

    'registrant':               r'Registrant Organization:\s?(.+)',

    'expiration_date':          r'Registrar Registration Expiration Date:\s?(.+)',

    'status':                   r'Domain Status:\s?(.+)',
}


eu = {
    'extend': 'com',

    'registrar':                r'Name:\s?(.+)',

    'domain_name':              r'\nDomain:\s*(.+)',

    'name_servers':             r'Name servers:\n(?:\s+(\S+)\n)(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?(?:\s+(\S+)\n)?(?:\s+(\S+)\n)\n?',
}


fi = {
    'extend': None,

    'domain_name':              r'domain\.+:\s?(.+)',

    'registrar':                r'registrar\.+:\s?(.+)',

    'registrant_country':       None,

    'creation_date':            r'created\.+:\s?(.+)',
    'expiration_date':          r'expires\.+:\s?(.+)',
    'updated_date':             r'modified\.+:\s?(.+)',

    'name_servers':             r'nserver\.+:\s*(.+)',
    'status':                   r'status\.+:\s?(.+)',
}

fr = {
    'domain_name':              r'domain:\s?(.+)',
    'registrar':                r'registrar:\s*(.+)',
    'registrant':               r'contact:\s?(.+)',

    'creation_date':            r'created:\s?(.+)',
    'expiration_date':          r'Expiry Date:\s?(.+)',
    'updated_date':             r'last-update:\s?(.+)',

    'name_servers':             r'nserver:\s*(.+)',
    'status':                   r'status:\s?(.+)',
    'emails':                   r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
    
}


global_ = {
    'extend': 'store',

    'name_servers': r'Name Server: (.+)',
}

hk = {
    'domain_name':               r'Domain Name:\s+(.+)',

    'registrar':                 r'Registrar Name:\s?(.+)',
    'registrant':                r'Company English Name.*:\s?(.+)',

    'creation_date':             r'Domain Name Commencement Date:\s?(.+)',
    'expiration_date':           r'Expiry Date:\s?(.+)',
    'updated_date':              None,

    'name_servers':              r'Name Servers Information:\n\n(?:(\S+)\n)(?:(\S+)\n)(?:(\S+)\n)?(?:(\S+)\n)?\n?',

    'status':                    r'Domain Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
    
}

id_ = {
    'extend': 'com',

    'registrar':                r'Sponsoring Registrar Organization:\s?(.+)',

    'creation_date':            r'Created On:\s?(.+)',
    'expiration_date':          r'Expiration Date:\s?(.+)',
    'updated_date':             r'Last Updated On:\s?(.+)$',
}


im = {
    'domain_name':              r'Domain Name:\s+(.+)',
    'status':                   None,

    'registrar':                None,
    'registrant_country':       None,

    'creation_date':            '',
    'expiration_date':          r'Expiry Date:\s?(.+)',
    'updated_date':             '',

    'name_servers':             r'Name Server:(.+)',
}

io = {
    'extend': 'com',

    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
}


ir = {
    'extend': None,

    'domain_name':              r'domain:\s?(.+)',
    'registrar':                'nic.ir',

    'registrant_country':       None,

    'creation_date':            None,
    'status':                   None,

    'expiration_date':          r'expire-date:\s?(.+)',
    'updated_date':             r'last-updated:\s?(.+)',

    'name_servers':             r'nserver:\s*(.+)\s*',
}


is_ = {
    'domain_name':              r'domain:\s?(.+)',

    'registrar':                None,
    'registrant':               r'registrant:\s?(.+)',
    'registrant_country':       None,

    'creation_date':            r'created:\s?(.+)',
    'expiration_date':          r'expires:\s?(.+)',
    'updated_date':             None,

    'name_servers':             r'nserver:\s?(.+)',
    'status':                   None,
    'emails':                   r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}


it = {
    'extend': 'com',

    'domain_name':              r'Domain:\s?(.+)',
    'registrar':                r'Registrar\s*Organization:\s*(.+)',
    'registrant':               r'Registrant\s*Organization:\s*(.+)',

    'creation_date':            r'Created:\s?(.+)',
    'expiration_date':          r'Expire Date:\s?(.+)',
    'updated_date':             r'Last Update:\s?(.+)',

    'name_servers':             r'Nameservers\s?(.+)\s?(.+)\s?(.+)\s?(.+)',
    'status':                   r'Status:\s?(.+)',
}

kr = {
    'extend': 'com',

    'domain_name':              r'Domain Name\s*:\s?(.+)',

    'registrar':                r'Authorized Agency\s*:\s*(.+)',
    'registrant':               r'Registrant\s*:\s*(.+)',

    'creation_date':            r'Registered Date\s*:\s?(.+)',
    'expiration_date':          r'Expiration Date\s*:\s?(.+)',
    'updated_date':             r'Last Updated Date\s*:\s?(.+)',

    'status':                   r'status\s*:\s?(.+)',
}


kz = {
    'extend': None,

    'domain_name':              r'Domain name\.+:\s(.+)',

    'registrar':                r'Current Registar:\s(.+)',
    'registrant_country':       r'Country\.+:\s?(.+)',

    'expiration_date':          None,
    'creation_date':            r'Domain created:\s(.+)',
    'updated_date':             r'Last modified :\s(.+)',

    'name_servers':             r'server.*:\s(.+)',
    'status':                   r'Domain status :\s?(.+)',
}

lt = {
    'extend': 'com',

    'domain_name':              r'Domain:\s?(.+)',

    'creation_date':            r'Registered:\s?(.+)',
    'expiration_date':          r'Expires:\s?(.+)',

    'name_servers':             r'Nameserver:\s*(.+)\s*',
    'status':                   r'\nStatus:\s?(.+)',
}

lv = {
    'extend': 'ru',

    'creation_date':            r'Registered:\s*(.+)\n',
    'updated_date':             r'Changed:\s*(.+)\n',

    'status':                   r'Status:\s?(.+)',
}

me = {
    'domain_name':              r'Domain Name:\s?(.+)',
    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)\s*',

    'status':                   None,
    
}

ml = {
    'extend': 'com',

    'domain_name':              r'Domain name:\s*([^(i|\n)]+)',

    'registrar':                r'(?<=Owner contact:\s)[\s\S]*?Organization:(.*)',
    'registrant_country':       r'(?<=Owner contact:\s)[\s\S]*?Country:(.*)',
    'registrant':               r'(?<=Owner contact:\s)[\s\S]*?Name:(.*)',

    'creation_date':            r'Domain registered: *(.+)',
    'expiration_date':          r'Record will expire on: *(.+)',

    'name_servers':             r'Domain Nameservers:\s*(.+)\n\s*(.+)\n',

    'emails':                   r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

mobi = {
    'extend': 'com',

    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date':             r'\nUpdated Date:\s?(.+)',
}


mx = {
    'domain_name':              r'Domain Name:\s?(.+)',

    'registrant':               r'Registrant:\n\s*(.+)',
    'registrar':                r'Registrar:\s?(.+)',

    'creation_date':            r'Created On:\s?(.+)',
    'expiration_date':          r'Expiration Date:\s?(.+)',
    'updated_date':             r'Last Updated On:\s?(.+)',

    'name_servers':             r'\sDNS:\s*(.+)',
}


name = {
    'extend':                   'com',

    'status':                   r'Domain Status:\s?(.+)',
}


nl = {
    'extend': 'com',

    'expiration_date':          None,
    'registrant_country':       None,

    'domain_name':              r'Domain name:\s?(.+)',
    'name_servers':             (
        r'''(?x:
            Domain\ nameservers:[ \t]*\n
            (?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n       # ns1.tld.nl [A?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns2.tld.nl [A?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns2.tld.nl [AAAA?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns3.tld.nl [A?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns3.tld.nl [AAAA?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns4.tld.nl [A?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns4.tld.nl [AAAA?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns5.tld.nl [A?]
            (?:(?:[ \t]+) (\S+) (?:[ \t]+\S+)? \n)?  # opt-ns5.tld.nl [AAAA?]
            # Don't check for final LF; there might be even more records..
        )'''),
    'reseller':                 r'Reseller:\s?(.+)',
    'abuse_contact':            r'Abuse Contact:\s?(.+)',
}



nyc = {
    'extend': 'com',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'Status:\s?(.+)',
}


nz = {
    'extend': None,

    'domain_name':              r'domain_name:\s?(.+)',
    'registrar':                r'registrar_name:\s?(.+)',
    'registrant':               r'registrant_contact_name:\s?(.+)',
    'registrant_country':       None,

    'creation_date':            r'domain_dateregistered:\s?(.+)',
    'expiration_date':          r'domain_datebilleduntil:\s?(.+)',
    'updated_date':             r'domain_datelastmodified:\s?(.+)',

    'name_servers':             r'ns_name_[0-9]{2}:\s?(.+)',
    'status':                   r'query_status:\s?(.+)',
    'emails':                   r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}


online = {
    'extend': 'com',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'Status:\s?(.+)',
}

org = {
    
    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date':             r'\nLast Updated On:\s?(.+)',

    'name_servers':             r'Name Server:\s?(.+)\s*',
    
    'domain_name':               r'Domain Name:\s?(.+)',

    'registrar':                 r'Registrar:\s?(.+)',
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':        r'Registrant Country:\s?(.+)',

    'creation_date':             r'Creation Date:\s?(.+)',
    'expiration_date':           r'Registry Expiry Date:\s?(.+)',
    'updated_date':              r'Updated Date:\s?(.+)',

    'name_servers':              r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',


}

pe = {
    'domain_name':               r'Domain Name:\s?(.+)',

    'registrar':                 r'Registrar:\s?(.+)',
    'registrant_country':        r'Registrant Country:\s?(.+)',

    'creation_date':             r'Creation Date:\s?(.+)',
    'expiration_date':           r'Registry Expiry Date:\s?(.+)',
    'updated_date':              r'Updated Date:\s?(.+)',

    'name_servers':              r'Name Server:\s*(.+)\s*',
    'status':                    r'Status:\s?(.+)',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'registrant':                r'Registrant Name:\s?(.+)',

    'admin':                    r'Admin Name:\s?(.+)',
}

pharmacy = {
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':        r'Registrant Country:\s?(.+)',

    'name_servers':              r'Name Server:\s*(.+)\s*',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'status:\s?(.+)',
}

pl = {
    'extend': 'uk',

    'registrar':                r'\nREGISTRAR:\s*(.+)\n',

    'creation_date':            r'\ncreated:\s*(.+)\n',
    'updated_date':             r'\nlast modified:\s*(.+)\n',
    'expiration_date':          r'\noption expiration date:\s*(.+)\n',

    'name_servers':             r'\nnameservers:\s*(.+)\n\s*(.+)\n',
    'status':                   r'\nStatus:\n\s*(.+)',
}


press = {

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'Status:\s?(.+)',
    
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':        r'Registrant Country:\s?(.+)',

    'name_servers':              r'Name Server:\s*(.+)\s*',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

pt = {

    'domain_name':              r'Domain:\s?(.+)',

    'registrar':                None,

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Expiration Date:\s?(.+)',
    'updated_date':             None,

    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s?(.+)',
    
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':        r'Registrant Country:\s?(.+)',

    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}


pw = {

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'Status:\s?(.+)',
    
    'registrant':                r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country':        r'Registrant Country:\s?(.+)',

    'name_servers':              r'Name Server:\s*(.+)\s*',
    'emails':                    r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

rest = {
    'extend':                   'store',

    'status':                   r'Domain Status:\s*(.+)',
}

ru = {

    'domain_name':              r'\ndomain:\s*(.+)',

    'creation_date':            r'\ncreated:\s*(.+)',
    'expiration_date':          r'\npaid-till:\s*(.+)',

    'name_servers':             r'\nnserver:\s*(.+)',
    'status':                   r'\nstate:\s*(.+)',

    'registrar':                 r'\nregistrar:\s?(.+)',
    'registrant':                r'\norg:\s?(.+)',

}

ru_rf = {
    'extend': 'com',

    'domain_name':              r'\ndomain:\s*(.+)',

    'creation_date':            r'\ncreated:\s*(.+)',
    'expiration_date':          r'\npaid-till:\s*(.+)',

    'name_servers':             r'\nnserver:\s*(.+)',
    'status':                   r'\nstate:\s*(.+)',
    
    'registrar':                 r'\nregistrar:\s?(.+)',
    'registrant':                r'\norg:\s?(.+)',
}

sh = {
    'extend': 'com',
    
    'registrant':              r'\nRegistrant Organization:\s?(.+)',

    'expiration_date':         r'\nRegistry Expiry Date:\s*(.+)',

    'status':                  r'\nDomain Status:\s?(.+)',
}

se = {

    'domain_name':              r'domain:\s?(.+)',

    'registrar':                r'registrar:\s?(.+)',

    'registrant_country':       None,

    'creation_date':            r'created:\s?(.+)',
    'expiration_date':          r'expires:\s?(.+)',
    'updated_date':             r'modified:\s?(.+)',

    'name_servers':             r'nserver:\s*(.+)',
    'status':                   r'status:\s?(.+)',
}

store = {

    'registrar':                r'Registrar:\s?(.+)',
    'registrant':               r'Registrant Organization:\s?(.+)',

    'updated_date':             r'Updated Date:\s?(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',

    'name_servers':             r'Name Server:\s*(.+)',
    'status':                   r'Domain Status:\s*(.+)',
}

tel = {
    'extend': 'com',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'Status:\s?(.+)',
}


tv = {
    'extend': 'com',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'Status:\s?(.+)',
}

ua = {
    'extend': 'com',

    'domain_name':              r'\ndomain:\s*(.+)',

    'registrar':                r'\nregistrar:\s*(.+)',
    'registrant_country':       r'\ncountry:\s*(.+)',

    'creation_date':            r'\ncreated:\s*(.+)',
    'expiration_date':          r'\nexpires:\s*(.+)',
    'updated_date':             r'\nmodified:\s*(.+)',

    'name_servers':             r'\nnserver:\s*(.+)',
    'status':                   r'\nstatus:\s*(.+)',
}

uk = {
    'extend': 'com',

    'registrant':               r'Registrant:\n\s*(.+)',

    'creation_date':            r'Registered on:\s*(.+)',
    'expiration_date':          r'Expiry date:\s*(.+)',
    'updated_date':             r'Last updated:\s*(.+)',

    'name_servers':             r'Name Servers:\s*(.+)\s*',
    'status':                   r'Registration status:\n\s*(.+)',
}

uz = {
    'extend': 'com',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Expiration Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'Status:\s?(.+)',
}

video = {
    'extend': 'com',

    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date':             r'\nUpdated Date:\s?(.+)',
}


wiki = {
    'extend': 'com',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',

    'status':                   r'Status:\s?(.+)',
}

work = {
    'extend': 'com',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',

    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'Registry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
}

xyz = {
    'extend': 'com',

    'domain_name':              r'Domain Name:\s?(.+)',

    'registrar':                r'Registrar:\s*(.+)',
    'creation_date':            r'Creation Date:\s?(.+)',
    'expiration_date':          r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date':             r'Updated Date:\s?(.+)',
    'status':                   r'Status:\s?(.+)',
}


