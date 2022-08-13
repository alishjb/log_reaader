import re
from ipaddr import IPAddress,IPNetwork
from ipwhois import IPWhois as ips
netip=IPNetwork('0.0.0.0/0')
regex_keyword='(?i)union'
unnormal_ips=list()
logfile = 'apache.log' # address of file
def log_reader(logfile):
    file = open(logfile,'r')
    for line in file:
        if re.findall(regex_keyword,line):
            if netip.Contains(IPAddress(re.findall(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}",line)[0])):
                unnormal_ips.append(re.findall(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}",line)[0])
                print(line)
    print(unnormal_ips)


log_reader(logfile)
for object in unnormal_ips:
    print("Please Wait, Trying to get cidr of unnormal ip's ")
    obj = ips(object)
    result = obj.lookup_whois()
    print(f"Ip:{object} - CIDR = {result['asn_cidr']}")
    CIDR= result['asn_cidr']
    netip = IPNetwork(CIDR)
    file = open(logfile,'r')
    for line in file:
        if netip.Contains(IPAddress(re.findall(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", line)[0])):
            print(line)


