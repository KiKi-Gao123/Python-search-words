import requests
import json
if __name__ == '__main__':
    url='http://www.kfc.com.cn/kfccda/storelist/index.aspx'
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'}

    reponse = requests.get(url=url, headers=headers)
    list_data = reponse.json()
    fp = open('./kfc.jsou', 'w', encoding='utf-8')
    json.dump(list_data, fp, ensure_ascii=False)
    print('爬取结束!!!')

