import requests
if __name__ == '__main__':
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'}
    url='https://www.so.com/s?'
    kw = input('请输入一个要搜索的词:')
    param={'q':kw}
    reponse=requests.get(url=url,params=param,headers=headers)
    page_text=reponse.text
    fileName=kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'保存成功!')