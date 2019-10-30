""" 
Created by
@author: tao.zhan
@time: 2019/10/29 8:20 PM
"""

import datetime
from aip import AipNlp


APP_ID = '17648580'
API_KEY = 'h0mES7OVPf3w7T9fWyCZ23go'
SECRET_KEY = 'FWCFxmPiI79b6jEvT8YdXiduURhAduUF'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

result = []
with open("./tutorial/qq-title.2019-10-30") as rf:
    line = rf.readline()
    while line:
        result.append(line.strip())
        line = rf.readline()

print(datetime.datetime.now())
for text in result:
    print(client.sentimentClassify(text)['items'][0]['sentiment'])
