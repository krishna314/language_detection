import json
from twython import Twython
import re

ACCESS_TOKEN='870169225800720385-VwlNIl8lGomYktQMMmgeVfIiCdade51'
ACCESS_SECRET='OnhNiydxQk8EEokQIpVvD9qztEWV8ujJRfg6HvuT1hMZW'
API_KEY='ymkHKavDv9YobuRiRqLKIEHZR'
API_SECRET='mrUam2ZM2II0Z5jFubDlejOF7dE8TigNJuf2AxyCCiTKs0ua1N'
twitter=Twython(API_KEY,API_SECRET,ACCESS_TOKEN,ACCESS_SECRET)
f=open("twitter_ids")
total=''
k=0
regex=re.compile("http://.{1,4}/[a-zA-z0-9]{1,18}")
for line in f:
    if "zh-CN" in line:
        #t_id=int(line[3:])
        t_id = int(line[6:])
        #print(t_id)
        try:
            tweet = twitter.show_status(id=t_id)
            k+=1
            text = tweet["text"]
            text = regex.sub("", text)
            #print(text)
            total += text
        except:
            continue
    if k==1000:
        break

#regex=re.compile("[a-zA-z0-9.()?!:=-~]")
regex=re.compile("[\x00-\x7F]")
total=regex.sub("",total)
print(format(total))



