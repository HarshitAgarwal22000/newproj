from flask import Flask,render_template, request,jsonify
app=Flask(__name__)
import re
import websockets
import datetime
import os
import asyncio
input_value=0

regexvalues=[]
file11=open("C:\\Users\\harsh\\OneDrive\\Desktop\\access.log","r")
con=file11.read()




@app.route('/process_value_fetch', methods=['POST'])
def process_value_fetch():
    regexvalues.clear()
    data = request.get_json()
    input_value = data['input_value']
    
    print(input_value)
    s=input_value[5]+input_value[6]
    if(s=="01"):
        l="Jan"
    elif (s=="02"):
        l="Feb"
    elif (s=="03"):
        l="Mar"
    elif (s=="04"):
        l="Apr"
    elif (s=="05"):
        l="May"
    elif (s=="06"):
        l="Jun"
    elif (s=="07"):
        l="Jul"
    elif (s=="08"):
        l="Aug"
    elif (s=="09"):
        l="Sep"
    elif (s=="10"):
        l="Oct"
    elif (s=="11"):
        l="Nov"
    elif (s=="12"):
        l="Dec"
    print(l)
    dat=input_value[8]+input_value[9]+"/"+l+"/"+input_value[0]+input_value[1]+input_value[2]+input_value[3]
    print(dat)
    datt=input_value[22]+input_value[23]
    if(datt=="01"):
        ly="Jan"
    elif (datt=="02"):
        ly="Feb"
    elif (datt=="03"):
        ly="Mar"
    elif (datt=="04"):
        ly="Apr"
    elif (datt=="05"):
        ly="May"
    elif (datt=="06"):
        ly="Jun"
    elif (datt=="07"):
        ly="Jul"
    elif (datt=="08"):
        ly="Aug"
    elif (datt=="09"):
        ly="Sep"
    elif (datt=="10"):
        ly="Oct"
    elif (datt=="11"):
        ly="Nov"
    elif (datt=="12"):
        ly="Dec"
    yr=input_value[25]+input_value[26]+"/"+ly+"/"+input_value[17]+input_value[18]+input_value[19]+input_value[20]
    print(yr)
    tore=rf".*{(dat)}.*"
    print(tore)
    ws=re.finditer(tore,con)
    for matc in ws:
        regexvalues.append(matc.group())
    
    tore2=rf".*{(yr)}.*"
    print(tore2)
    wsy=re.finditer(tore2,con)
    for matcu in wsy:
        regexvalues.append(matcu.group())
    print(regexvalues)
    response = f"Value processed: {input_value}"
    return response

















current_time = datetime.datetime.now()
print (current_time.hour)

pattern="[^/][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[ ][0-9]"
date="[0-9]{2}[/][A-Z]{1}[a-z]{2}[/][0-9]{4}"
statuscodes="[ ][0-9]{3}[ ]"
treq2=".*[0-9][0-9][0-9][ ]([2-9])+[.][0-9]{3}[ ][0-9].*"
treq5=".*[0-9][0-9][0-9][ ]([5-9])+[.][0-9]{3}[ ][0-9].*"
treq10=".*[0-9][0-9][0-9][ ][1-9][0-9][.][0-9]{3}[ ][0-9].*"
topip="[ ][0-9]*[.][0-9]*[.][0-9]*[.][0-9]*"
ipadd=[]
ipadd.append("All IP Addresses")
k=re.finditer(pattern,con)
print("IP Addresses \n")
for match in k:
    print(match.group())
    ipadd.append(match.group())


w=re.finditer(date,con)
print("Dates")
un=[]
datee=[]
datee.append("All dates")
for Match in w:
    if Match.group() not in un:
        un.append(Match.group())
        datee.append(Match.group())
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
stat=[]
cou=[]
for el in uniqtu:
    for matche in all:
        if matche == el:
            count=count+1
    print("Status Code",el,"occurs",count,'times')  
    stat.append(el)
    cou.append(count)
    count=0
re2=[]
re5=[]
re10=[]
tr=re.finditer(treq2,con)
for mat in tr:
    print(mat.group())
    re2.append(mat.group())
trs=re.finditer(treq5,con)
for matq in trs:
    print(matq.group())
    re5.append(matq.group())
trsy=re.finditer(treq10,con)
for matg in trsy:
    print(matg.group())
    re10.append(matg.group())
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


reqhost=[]
nreqhost=[]
lasthostreq=[]
all=[]
l=1
@app.route('/process_value_fetch1', methods=['POST'])
def process_value_fetch1():
    all.clear()
    
    data = request.get_json()
    host_value = data['input_value']
   
    all.clear()
    print("Printing ALL",all)
    tr=rf".*{(host_value)}"
    ed=re.finditer(tr,con)
    print("Requests for the specified host")
    all.append("All Requests for specified host")
    all.append(" ")
    all.append(" ")
    all.append(" ")
    for t in ed:
        print("TTTT",t.group())
        reqhost.append(t.group())
        all.append(t.group())
    print("ALLL2",all)
    nreqhost=reqhost[::-1]
    for elem in uniqtu:
        print("Status code",elem)
        for r in nreqhost:
            patterns=rf".*[ ]{(elem)}[ ].*"
            l=re.finditer(patterns,r)
            for am in l:
                print("x")
                print(am.group())
                lasthostreq.append(am.group())
                l=0
                break
            if(l==0):
                break
        print("LASTHOSTREQ",lasthostreq)
        all.append("Code")
        all.append(elem)
        print('vlsiir')
        print("LASTHOSTREQ2",lasthostreq)
        all.extend(lasthostreq)
        print("LASTHOSTREQ3",lasthostreq)
        lasthostreq.clear()
        print("ALLLL",all)
    print(all)


    response = f"Value processed: {host_value}"
    return response


a=""
hosts=[]
uniqhosts=[]
upip=[]
uniqip=[]
path=[]
uniqpath=[]
hostcount=[]
ipcount=[]
pathcount=[]
maxuniqhost=""
maxuniqip=""
maxuniqpath=""
val=[]
@app.route('/process_value_fetch2', methods=['POST'])
def process_value_fetch2():
  
    data = request.get_json()
    click_value = data['input_value']
    
    hosts.clear()
    uniqhosts.clear()
    upip.clear()
    uniqip.clear()
    path.clear()
    uniqpath.clear()
    hostcount.clear()
    ipcount.clear()
    pathcount.clear()
    val.clear()
    maxuniqhost=""
    maxuniqip=""
    maxuniqpath=""
    a=""
    print(click_value)
    t=rf".*{(click_value)}.*"
    print(t)
    z=re.finditer(t,con)
    print(z)
    for i in z:
        #print(i.group)
        a=a+" "+i.group()
    print("AAAAA",a) 
    #printing all requests for the clicked button and date
    #printing all hosts for that date
    count1t=0
    count2t=0
    count3t=0
    tw="[ ][a-z-]{2,5}[.].*[.][a-z0-9].*"
    zq=re.finditer(tw,con)
    for f in zq:
        if f.group() not in uniqhosts:
            uniqhosts.append(f.group())
        hosts.append(f.group())
    print("UNIQHOSTS",uniqhosts)
    print("HOSTS",hosts)
    for el in uniqhosts:
        for ele in hosts:
            if(el.strip()==ele.strip()):
                count1t=count1t+1
        hostcount.append(count1t)
        count1t=0
    maxuniqhost=uniqhosts[hostcount.index(max(hostcount))]
    val.append(maxuniqhost)
    print(maxuniqhost)
    print(hostcount)
    #printing all upstream ip's for that date
    yt="[ ][0-9]*[.][0-9]*[.][0-9]*[.][0-9]*"
    za=re.finditer(yt,a)
    for fa in za:
        if fa.group() not in uniqip:
            uniqip.append(fa.group())
        upip.append(fa.group())
    
    for elu in uniqip:
        for eleq in upip:
            if(elu.strip()==eleq.strip()):
                count2t=count2t+1
        ipcount.append(count2t)
        count2t=0
    maxuniqip=uniqip[ipcount.index(max(ipcount))]
    #print(uniqip)
    val.append(maxuniqip)
    print(maxuniqip)
    #printing all paths for that date
    p="[ ][/][a-z]*[/][a-z]*"
    zz=re.finditer(p,a)
    for fs in zz:
        if fs.group() not in uniqpath:
            uniqpath.append(fs.group())
        path.append(fs.group())
   
    for elk in uniqpath:
        for elep in path:
            if(elk.strip()==elep.strip()):
                count3t=count3t+1
        pathcount.append(count3t)
        count3t=0
    print(uniqpath)
    maxuniqpath=uniqpath[pathcount.index(max(pathcount))]
    val.append(maxuniqpath)
    print(uniqpath[pathcount.index(max(pathcount))])
    print("Values",val)
    response = f"Value processed: {click_value}"
    return response


cu_time = datetime.datetime.now()
req=[]
hour=cu_time.hour
oldmin=cu_time.minute
lmin=0

print(cu_time.year)
if(cu_time.month=="1"):
    mont="Jan"
elif (cu_time.month==2):
    mont="Feb"
elif (cu_time.month==3):
    mont="Mar"
elif (cu_time.month==4):
    mont="Apr"
elif (cu_time.month==5):
    mont="May"
elif (cu_time.month==6):
    mont="Jun"
elif (cu_time.month==7):
    mont="Jul"
elif (cu_time.month==8):
    mont="Aug"
elif (cu_time.month==9):
    mont="Sep"
elif (cu_time.month==10):
    mont="Oct"
elif (cu_time.month==11):
    mont="Nov"
elif (cu_time.month==12):
    mont="Dec"
else:
    mont="Jan"
print(mont)
print(cu_time.day)
if(cu_time.minute<10):
    newmin="5"+str(cu_time.minute)
    hour=hour-1
else:
    newmin=oldmin-10
    
    if(newmin==0):
        newmin="00"
    elif(newmin==1):
        newmin="01"
    elif(newmin==2):
        newmin="02"
    elif(newmin==3):
        newmin="03"
    elif(newmin==4):
        newmin="04"
    elif(newmin==5):
        newmin="05"
    elif(newmin==6):
        newmin="06"
    elif(newmin==7):
        newmin="07"
    elif(newmin==8):
        newmin="08"
    elif(newmin==9):
        newmin="09"
    print(newmin)
time=str(cu_time.day)+"/"+mont+"/"+str(cu_time.year)+":"+str(hour)+":"+str(newmin)
print(time)
pat=rf".*{(time)}.*"
print(pat)
zq=re.finditer(pat,con)
print(zq)
store_lines=False
for isx in zq:
    print(isx.group())
with open("C:\\Users\\harsh\\OneDrive\\Desktop\\access.log", "r") as file12:
    for line in file12:
        print(line)
        if re.search(pat, line):
                store_lines = True
        print(store_lines)
        if store_lines:
                req.append(line)
print(req)
    
    








file11.close()



@app.route('/')
def index():
    print(regexvalues)
    return render_template('index.html',un=un,regexvalues=regexvalues,maxuniqhost=maxuniqhost,maxuniqip=maxuniqip,maxuniqpath=maxuniqpath,val=val,all=all,req=req,re2=re2,re5=re5,re10=re10,ipadd=ipadd,stat=stat,cou=cou,datee=datee)

if __name__=='__main__':
    app.run(debug=True)

