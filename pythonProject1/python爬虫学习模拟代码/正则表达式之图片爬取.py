import requests
import re
import os
if __name__== "__main__":
    #创建一个文件夹,保存所有的图片
    if not os.path.exists('./糗图'):
        os.mkdir('./糗图')

    #发起请求
    url='https://www.qiushibaike.com/'
    #UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'}
    #获取响应数据 content是二进制类型数据 用来获取图片数据
    page_text = requests.get(url=url,  headers=headers).text
    #使用聚焦爬虫来获取页面的糗图
    ex = '<div class="thumb">.*?<img src="(.*?)"alt.*?</div>'
    img_list=re.findall(ex,page_text,re.S)
    for src in img_list:
        src = 'https:'+src
        img_list=requests.get(url=src,headers=headers).content
        img_name=src.split('/')[-1]
        imgPath='./糗图'+img_name
        with open(imgPath,'wb') as fp:
            fp.write(img_list)
            print(img_name,'下载成功!!!')

