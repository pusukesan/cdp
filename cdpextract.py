# -*- coding: utf-8 -*-
"""
1. split by '------'. each array has one peer information.
2. if includes "Device ID"
========[use information below(line from 'show cdp nei det')]===========
Device ID: R2

Entry address(es): 
  IP address: 192.168.1.2

Interface: Ethernet1/1,  Port ID (outgoing port): Ethernet1/2
=========[change format from line to dictionary]==========================
device = {'R2': {}, …  }
device['R2'] = {'DeviceID':'R2', 'IPaddr':'192.168.1.2,'localInterface':'Ethernet1/1','remoteInterface':'Ethernet1/2'}
"""

import os
import re

os.chdir("some_directory")
f = open("some_filename", "r")

#def cdpdev(f):
splt = (f.read()).split('-------------------------\n')
device = {} 
for i in splt:
    if "Device ID" in i:
        hoge = [j.strip() for j in re.split('[\n]', i)]
        for k in hoge:
            if "Device ID" in k:
                #extract peer hostname
                didmatch = re.search(r'Device ID:(.*)', k)
            elif "IP address" in k:
                #extract peer IP address
                ipaddrmatch = re.search(r'IP address:(.*)', k)
            elif "Interface" in k:
                #extract local/peer interface name
                lifmatch = re.search(r'Interface:(.*),', k)
                rifmatch = re.search(r'Port ID \(outgoing port\):(.*)', k)
        #for simple processing, ignoring space in regex match and　next stripping space.      
        device[didmatch.group(1).strip()] = {'DID':didmatch.group(1).strip(),'IPa':ipaddrmatch.group(1).strip(),'lIf':lifmatch.group(1).strip(),'rIf':rifmatch.group(1).strip()}
