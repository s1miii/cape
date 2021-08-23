import requests
import json
import argparse
import socket
def args():
    arg=argparse.ArgumentParser()
    arg.add_argument('-i','--ip',dest='ip',help='-i or --ip Argument Pass IP')
    arg.add_argument('-l','--list',dest='list',help='-l or --list Argument Pass List IP')
    return [arg.parse_args().ip,arg.parse_args().list]
def extract(ip):
    save = open('Sites.txt','a')
    try:
        i=socket.gethostbyaddr(str(ip))
        save.write(i[0]+' | '+str(ip)+'\n')
    except:
        req=requests.get('https://api.viewdns.info/reverseip/?host='+str(ip)+'&apikey=e0cbb9dd32ea828d23759ffbc735f2c5f4541655&output=json').text
        js=json.loads(req)
        count=int(js['response']['domain_count'])
        for i in range(0,count):
            save.write(js['response']['domains'][i]['name']+' | '+str(ip)+'\n')
print('''
       ////////////////////////////////////////
     ///////////////////////////////////////////
   //////////////////////////////////////////////
  /////////////[ Coded By MrVirus ]///////////////
 //////////////[ Instagram : BQBB ]////////////////
///////////////[ Telegram : camera ]/////////////////
   //////////////////////////////////////////////
    ///////////////////////////////////////////
     ////////////////////////////////////////
''')    
ip=args()[0]
li=args()[1]
if(li):
    li=open(str(li)+'.txt','r')
    for i in li:
        extract(i.strip())
elif(li==None):
    if(ip):
        extract(ip.strip())
    else:
        ch=input('[ 1 ] From IP\n[ 2 ] From List\nSelect : ')
        if(int(ch)==1):
            ip=input('IP : ')
            extract(ip.strip())
        elif(int(ch)==2):
            li=input('List : ')
            li=open(li+'.txt','r')
            for i in li:
                extract(i.strip())
        else:
            exit()
