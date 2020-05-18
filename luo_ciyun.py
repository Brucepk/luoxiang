import requests
import json
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
import random

"""
爬取对应up主下所有视频的bvid信息，然后把弹幕都保存在csv文件中

1、下方的headers信息和params替换成自己的，在up主空间页面里，按F12，查看network请求，可以直接复制 curl链接，
通过一个网站工具可以直接转换成Python形式的请求：这个转换不懂的话可以参考这篇文章：https://mp.weixin.qq.com/s/fVDwNdVDZo_0q6jAMWCGAA

2、对Python感兴趣的同学可以关注我的个人公众号「Python知识圈」，有疑问也可以通过公众号加我微信，一起探讨交流
"""


def get_video_url():
    headers = {
        'authority': 'api.bilibili.com',
        'accept': 'application/json, text/plain, */*',
        'xxx':'xxxx'
    }

    params = (
        ('mid', '517327498'),
        ('ps', '30'),
        ('xx', '0'),
        ('xxxx', '1'),
        ('xxx', ''),

    )
    response = requests.get('https://api.bilibili.com/x/space/arc/search', headers=headers, params=params).text
    json_res = json.loads(response)
    video_urls = []
    for i in range(0, 23):
        bvid = json_res['data']['list']['vlist'][i]['bvid']
        video_url = 'https://www.bilibili.com/video/' + bvid
        video_urls.append(video_url)
        print('正在获取第 %d个视频的链接' %(i+1))
        time.sleep(int(format(random.randint(5, 10))))
    return video_urls


def get_cid(url):
    """"
    通过视频链接获取cid信息
    """
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
        }
        response = requests.get(url, headers=headers)
        match_rule = r'cid=(.*?)&aid'
        cid = re.search(match_rule, response.text).group(0).replace('cid=', '').replace('&aid', '')
        return cid
    except:
        print('没有爬取到视频的cid，跳过')


def download2csv(cid):
    """
    爬取视频的弹幕信息保存为csv文件
    """
    danmu_url = 'http://comment.bilibili.com/{}.xml'.format(cid)
    headers = {
        'user-agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
    }
    html = requests.get(danmu_url, headers=headers).content
    html_data = str(html, 'utf-8')
    soup = BeautifulSoup(html_data, 'lxml')
    results = soup.find_all('d')
    comments = [comment.text for comment in results]
    comments_dict = {'comments': comments}
    print(comments_dict)
    df = pd.DataFrame(comments_dict)
    df.to_csv('luox.csv', mode='a', encoding='utf-8')


if __name__ == '__main__':
    video_urls = get_video_url()
    for video_url in video_urls:
        cid = get_cid(video_url)
        download2csv(cid)
        time.sleep(int(format(random.randint(5, 10))))
    print('保存弹幕文件完成！')

