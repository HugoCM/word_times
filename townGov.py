'''
Created on 2017年7月26日

@author: Mi
'''
import re
import urllib.request
import urllib.parse


class Town:
    '''
县政府类
    '''


    def __init__(self, name, url, ):
        '''    
    县名，
    URL，
        '''
        self.name = name
        self.url = url    
    
    #获取关键词出现次数
    
    def get_times(self, word):
        data = urllib.parse.quote(word)+'%20'
        get_url = 'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd='+data+'site%3A'+self.url
        #print(get_url)

        resp = urllib.request.urlopen(get_url)
        content = resp.read()
        content = content.decode('utf-8')
    
        p = r'百度为您找到相关结果约([0-9]+)个'
        pattern = re.compile(p)
        times = pattern.findall(content)[0]
        print(self.name+':'+times)
        
        return times
    
    
        
        