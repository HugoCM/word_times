'''
Created on 2017年8月4日

@author: Mi
'''

import os
import IO
from townGov import Town

def cli(word):
    govlist = IO.csv2dict(r'县政府名单.csv')
    timelist = {}
    for k,v in govlist.items():
        timelist[k] = Town(k,v).get_times(word)
    
    IO.dict2csv(timelist,'rst.csv')
#     os.rename('rst.csv','rst.xlsx')

if __name__ == '__main__':
    cli('扶贫 农业')