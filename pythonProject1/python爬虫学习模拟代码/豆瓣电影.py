import requests
import json

if __name__== "__main__":
    url='https://movie.douban.com/j/chart/top_list'
    param={
        'type': '24',
        'interval_id': '100:90',
         'action':'',
         'start': '0',
          'limit': '1000'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'}
    reponse= requests.get(url=url,params=param,headers=headers)
    list_data=reponse.json()
    fp=open('./douban.jsou','w',encoding='utf-8')
    json.dump(list_data,fp,ensure_ascii=False)
    print('爬取结束!!!')


