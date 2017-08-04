'''
Created on 2017年7月26日

@author: Mi
'''

import csv

def csv2dict(csvpath):
    govlist = {}
    with open(csvpath) as f:
        reader=csv.reader(f,delimiter=',')
        for row in reader:
            url = row[1].split('.')
            url = '.'.join(url[1:])
            govlist[row[0]]=url
    return govlist
    
def dict2csv(dict,file):
    with open(file,'w') as f:
        w=csv.writer(f)
        # write each key/value pair on a separate row
        w.writerows(dict.items())
    #anti empty lines 
    with open(file,'rt') as fmid:
        lines=''
        for line in fmid:
            if line!='\n':
                lines+=line
    with open(file,'wt')as ffinal:  #再次文本方式写入，不含空行
        ffinal.write(lines)
        
# if __name__ == '__main__':
#     d = csv2dict(r'县政府名单.csv')
#     d1 = {}
#     for k,v in d.items():
#         d1[k] = len(v)
#     print(d)
#     print(d1)
#     dict2csv(d1,'tst.csv')