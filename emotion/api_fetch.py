""" 
Created by
@author: tao.zhan
@time: 2019/10/29 8:20 PM
"""

import datetime
from aip import AipNlp


APP_ID = 'xxxx'
API_KEY = 'xxxx'
SECRET_KEY = 'xxxx'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

result = []
with open("./tutorial/qq-title.2019-10-30") as rf:
    line = rf.readline()
    while line:
        result.append(line.strip())
        line = rf.readline()

print(datetime.datetime.now())
for text in result:
    resp = client.sentimentClassify(text)['items'][0]
    print(text + "\t" + str(resp["confidence"]) + "\t" + str(resp["sentiment"]) + "\t" + str(resp["negative_prob"]))
print(datetime.datetime.now())
