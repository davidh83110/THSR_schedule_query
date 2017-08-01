'''
* THSR Schedule Query 
*
* @author David
* Version 1.0 , 2017-08-01 
*
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd

def THSR(StartStation, EndStation, SearchDate, SearchTime):
    #r = requests.get('http://www.thsrc.com.tw/tw/TimeTable/SearchResult')
    
    station = {
        'ｫnｴ・ : '2f940836-cedc-41ef-8e28-c2336ac8fe68',
        '･x･_' : '977abb69-413a-4ccf-a109-0272c24fd490',
        'ｪOｾ・ : 'e6e26e66-7dc1-458f-b2f3-71ce65fdc95f',
        'ｮ邯・ : 'fbd828d8-b1da-4b06-a3bd-680cdca4d2cd',
        'ｷsｦﾋ' : 'a7a04c89-900b-4798-95a3-c01c455622f4',
        'ｭ]ｮﾟ' : 'e8fc2123-2aaf-46ff-ad79-51d4002a1ef3',
        '･x､､' : '3301e395-46b8-47aa-aa37-139e15708779',
        'ｹ・ﾆ' : '38b8c40b-aef0-4d66-b257-da96ec51620e',
        'ｶｳｪL' : '5f4c7bb0-c676-4e39-8d3c-f12fc188ee5f',
        'ｹﾅｸq' : '60831846-f0e4-47f6-9b5b-46323ebdcef7',
        '･xｫn' : '9c5ac6ca-ec89-48f8-aab0-41b738cb1814',
        '･ｪﾀ・ : 'f2519629-5973-4d08-913b-479cce78a356'
    }
    
    
    payload = {
        "StartStation": station.get(StartStation), 
        "EndStation": station.get(EndStation),
#        "SearchDate": SearchDate[:4] + '/' + searchDate[4:6] + '/' + searchDate[6:],
        "SearchDate": SearchDate,
#        "SearchTime": searchTime[:2] + ':' + searchTime[2:],
        "SearchTime": SearchTime,
        "SearchWay":"DepartureInMandarin"
    }
    
    url = 'http://www.thsrc.com.tw/tw/TimeTable/SearchResult'
    
    result = BeautifulSoup(requests.post(url=url, data=payload).text , 'lxml')
    
    thsr_result = []
    for i in result.findAll('td' , {'class':'toTouch'}):
        for x in i.findAll('td'):
            if x.text != '':
                thsr_result.append(x.text)

    thsr_result_to_df = []
    train_index = len(thsr_result)
    start_iter = 0
    for x in range(3, train_index, 3):
        thsr_result_to_df.append(thsr_result[start_iter:x])
        start_iter = x
    
    df_columns = ['ｨｮｦｸ','･Xｵoｮﾉｶ｡','ｩ雹Fｮﾉｶ｡']
    df_result = pd.DataFrame(data=thsr_result_to_df, columns=df_columns)
    return df_result
