""" 
Created by
@author: tao.zhan
@time: 2019/10/29 8:20 PM
"""

from aip import AipNlp

APP_ID = '17648580'
API_KEY = 'h0mES7OVPf3w7T9fWyCZ23go'
SECRET_KEY = 'FWCFxmPiI79b6jEvT8YdXiduURhAduUF'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

text = "薅羊毛薅出“羊圈生态”，羊毛党不只贪小便宜"
print(client.sentimentClassify(text))
