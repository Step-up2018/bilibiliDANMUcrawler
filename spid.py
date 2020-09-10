# coding:utf-8

from lxml import etree
import requests
import sys
import re
import importlib

importlib.reload(sys)

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'
}

def spidera(av):
    f = open("av" + av + '.txt', 'w', encoding='utf-8')
    url = f'https://api.bilibili.com/x/player/pagelist?aid={av}&jsonp=jsonp'
    res = requests.get(url)
    cid = res.json()['data'][0]['cid']
   #print(cid)
    comment_url = 'http://comment.bilibili.com/' + str(cid) + '.xml'
    comment_text = requests.get(comment_url, headers=head)
    comment_selector = etree.HTML(comment_text.content)
    comment_content = comment_selector.xpath('//i')
    for comment_each in comment_content:
        comments = comment_each.xpath('//d/text()')
        if comments:
            for comment in comments:
               f.writelines(comment + '\n')
               pass

def spiderb(bv):
    f = open("BV" + bv + '.txt', 'w', encoding='utf-8')
    url = f'https://api.bilibili.com/x/player/pagelist?bvid={bv}&jsonp=jsonp'
    res = requests.get(url)
    cid = res.json()['data'][0]['cid']
    comment_url = 'http://comment.bilibili.com/' + str(cid) + '.xml'
    comment_text = requests.get(comment_url, headers=head)
    comment_selector = etree.HTML(comment_text.content)
    comment_content = comment_selector.xpath('//i')
    for comment_each in comment_content:
        comments = comment_each.xpath('//d/text()')
        if comments:
            for comment in comments:
               f.writelines(comment + '\n')
               pass