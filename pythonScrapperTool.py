import requests
import string
from bs4 import BeautifulSoup


str = ['ice hockey','volleyball','martial art','rugby',
       'cricket','kabaddi','football','tennis','archery',
       'wrestling','boxing','golf','fencing','canoeing',
       'badminton','table tennis','taekwondo','hockey',
       'weightlifting','gymnastics','basketball','handball',
       'cycling','swimming','table tennis','golf','softball']

def fun(source):
    i=0
    counter=-1
    while i < len(str):
        
        x=source.find(str[i])
        if x>-1:
            counter=i
            break
        else:
            i+=1
    if counter>=0:
        print (str[counter])
    else:
        print ("NA")
    return
        
            
fp = open("new.txt","r")
lines = fp.read().splitlines()
for temp in lines:
    l=''
    for k in temp:
        if k.isspace():
            print 
        else:
            l=l+k
    if l.isalnum():
        print("invalid")
        continue
    elif 'http://' not in l:
         l='http://'+ l
    if len(l)>7:
        r = requests.get(l)
        #print(r.status_code)
        c=r.status_code
        if c==200: 
            soup = BeautifulSoup(r.content,"html.parser")
            s = soup.prettify()
            fun(s)
            continue
        else:
            print("invalid url")
            continue
fp.close()
    

        

    
