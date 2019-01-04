# -*- coding: UTF-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import json
import os
import time
import urllib
import urllib2

sys.setdefaultencoding

def get_links(page_num, page_index=43):
    link_list = []
    for x in xrange(page_num):
        link_list.append("http://jandan.net/ooxx/page-%d#comments"%(x+page_index))
        print("the link list is {}".format(link_list))
    return link_list
        
def get_network_data(url):
    req = urllib2.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0")
    response = urllib2.urlopen(req)
    # print("the response type is {}".format(type(response)))
    data = response.read()
    print("the data len is  {}".format(len(data)))
    return data

def find_img_url(content):
    print("the content is {}".format((content)))
    img_url = list()
    start = 0
    end = 0
    while(1):
        time.sleep(1)
        start = content.find(r"<img src=", start)
        print("one the start = {}".format(start))
        if start == -1:
            break
        else:
            temp1 = content.find(".jpg", start)
            temp2 = content.find(".gif", start)
            temp3 = content.find(".png", start)
            temp_nums = filter(lambda x:x != -1, [temp1, temp2, temp3])
            # print("temp_nums is {}".format(temp_nums))
            end = min(temp_nums)
            print("the start is {}, end is {}".format(start, end))
            print("the content is {}".format(content[start+4:end+4]))
            img_url.append(content[start+4:end+4])
        start = end
        # print("two the start = {}".format(start))
    return img_url



def get_img_urls(website_links):
    img_list = []
    for url in website_links:
        html = get_network_data(url).decode("utf-8")
        imgs = find_img_url(html)
        img_list.extend(imgs)

if __name__ == '__main__':
    if not os.path.exists("images"):
        os.mkdir("images")
    os.chdir("images")
    num = int(raw_input("please input page num:\n"))
    website_links = get_links(num)

    image_urls = get_img_urls(website_links)
