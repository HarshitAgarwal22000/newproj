import re
import datetime

current_time = datetime.datetime.now()
print (current_time.hour)
file11=open("C:\\Users\\harsh\\OneDrive\\Desktop\\access.log","r")
con=file11.read()
pattern="[^/][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[ ][0-9]"
date="[0-9]{2}[/][A-Z]{1}[a-z]{2}[/][0-9]{4}"
statuscodes="[ ][0-9]{3}[ ]"
treq2=".*[0-9][0-9][0-9][ ]([2-9])+[.][0-9]{3}[ ][0-9].*"
treq5=".*[0-9][0-9][0-9][ ]([5-9])+[.][0-9]{3}[ ][0-9].*"
treq10=".*[0-9][0-9][0-9][ ][1-9][0-9][.][0-9]{3}[ ][0-9].*"
topip="[ ][0-9]*[.][0-9]*[.][0-9]*[.][0-9]*"
text='''152.156.141.78 12/Feb/2021:06:52:54 +5470 "GET /myapi/consumers/executive/artificial%20intelligence HTTP/1.1" 200 0.979 10.77.27.15:443 1407 "-" "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_7_4) AppleWebKit/5361 (KHTML, like Gecko) Chrome/37.0.861.0 Mobile Safari/5361" TLSv1.2/ECDHE-RSA-AES256-GCM-SHA384 62b923587b05d59b-BOM application/json; charset=utf-8 apptwo-new.ppops.com
179.83.110.181 12/Feb/2021:06:52:54 +5470 "GET /recharge/phone/time-frame HTTP/1.1" 200 0.155 10.77.27.14:443 1957 "-" "Mozilla/5.0 (Windows NT 6.0; en-US; rv:1.9.2.20) Gecko/1990-03-11 Firefox/36.0" TLSv1.2/ECDHE-RSA-AES256-GCM-SHA384 62b923587b05d59b-BOM application/json; charset=utf-8 api.ppops.com
12.192.135.144 12/Feb/2021:06:52:54 +5470 "GET /recharge/dth/Cross-platform HTTP/1.1" 200 0.725 10.77.22.15:443 2061 "-" "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_6_3 rv:6.0; en-US) AppleWebKit/536.35.5 (KHTML, like Gecko) Version/4.2 Safari/536.35.5" TLSv1.2/ECDHE-RSA-AES256-GCM-SHA384 62b923587b05d59b-BOM application/json; charset=utf-8 apptwo-new.ppops.com
76.47.103.205 12/Feb/2021:06:52:55 +5570 "HEAD /myapi/consumers/middleware_Total HTTP/1.1" 405 0.476 10.77.27.13:8443 68 "-" "Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/1916-01-03 Firefox/35.0" TLSv1.2/ECDHE-RSA-AES256-GCM-SHA384 62b923587b05d59b-BOM application/json; charset=utf-8 api.ppops.com
6.7.79.57 12/Feb/2021:06:52:55 +5570 "GET /check/balance/capability/application-internet%20solution HTTP/1.1" 200 0.261 10.77.23.12:443 2130 "-" "Opera/10.89 (Windows 98; Win 9x 4.90; en-US) Presto/2.9.256 Version/12.00" TLSv1.2/ECDHE-RSA-AES256-GCM-SHA384 62b923587b05d59b-BOM application/json; charset=utf-8 api.ppops.com
243.67.250.6 12/Feb/2021:06:52:55 +5570 "GET /myapi/kyc/Compatible-Intuitive/local HTTP/1.1" 200 0.104 10.77.22.13:80 1716 "-" "Opera/10.58 (Windows 95; en-US) Presto/2.10.312 Version/10.00" TLSv1.2/ECDHE-RSA-AES256-GCM-SHA384 62b923587b05d59b-BOM application/json; charset=utf-8 apptwo.ppops.com
161.55.45.91 12/Feb/2021:06:52:55 +5570 "HEAD /myapi/kyc/directional/intangible HTTP/1.1" 304 10.868 10.77.22.14:8443 34 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/536.35.5 (KHTML, like Gecko) Version/5.1 Safari/536.35.5" TLSv1.2/ECDHE-RSA-AES256-GCM-SHA384 62b923587b05d59b-BOM application/json; charset=utf-8 apptwo.ppops.com'''

k=re.finditer(pattern,con)
print("IP Addresses \n")
"""for match in k:
    print(match.group())"""


w=re.finditer(date,con)
print("Dates")
un=[]
for Match in w:
    if Match.group() not in un:
        un.append(Match.group())
print(un)

uniqtu=[]
all=[]
s=re.finditer(statuscodes,con)
for matches in s:
    all.append(int(matches.group()))
    if int(matches.group().strip()) not in uniqtu:
        uniqtu.append(int(matches.group().strip()))
print(uniqtu)
count=0
sq=re.finditer(statuscodes,con)
"""for el in uniqtu:
    for matche in all:
        if matche == el:
            count=count+1
    print("Status Code",el,"occurs",count,'times')  
    count=0
tr=re.finditer(treq2,con)"""
#for mat in tr:
    #print(mat.group())
"""trs=re.finditer(treq5,con)
for matq in trs:
    print(matq.group())
trsy=re.finditer(treq10,con)
for matg in trsy:
    print(matg.group())"""
topips=re.finditer(topip,con)
uip=[]
allhost=[]
for map in topips:
    allhost.append(map.group())
    if map.group() not in uip:
        uip.append(map.group())
print(uip)
count1=0
w=re.finditer(topip,con)
for de in uip:
    for s in allhost:
        if s==de:
            count1=count1+1
    print(de)
    print(count1)
    count1=0
file11.close()

