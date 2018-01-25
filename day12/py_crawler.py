#!/usr/bin/env python3
'''
  * @time: Created on 2018/01/24 09:11
  * @author: by Ysan

    工作 获取蜜蜂视频的 动漫，少儿的视频json数据，导入自己的Launcher数据库中，方便搜索
'''

import pickle
import json
import gevent
from urllib.request import urlopen
from gevent import monkey
import time
monkey.patch_all()

base_dir = "E:/beevideos/少儿"
file_base = "少儿_%s"


def f(url, filename):
    file_path = "%s/%s" % (base_dir, filename)
    print("GET: %s" % url)
    resp = urlopen(url)
    data = resp.read()
    with open(file_path, 'wb') as f:
        # f.write(data)
        pickle.dump(data, f)


def achieve_data():
    urls = []
    base_url = "http://meta.beevideo.tv/videoApi/api2.0/qmz/listVideo.action?topId=2&page={}&pageSize=100"
    for i in range(1, 30):
        url = base_url.format(i)
        urls.append(gevent.spawn(f, url, file_base % i))

    time_start = time.time()
    gevent.joinall(urls)
    time_end = time.time()
    time_spend = time_end - time_start
    print("start : %s ; end : %s ; spend : %s" % (time_start, time_end, time_spend))


def parse_data():
    file_path = "%s/%s" % (base_dir, "shaoer")
    root_dict = {
        "data": []
    }
    for i in range(1, 29):
        file_name = "少儿_%s" % i
        print("------------------------------------- page_%s -------------------------------------" % i)
        with open("%s/%s" % (base_dir, file_name), 'rb') as f:
            file_data = f.read()
            file_json = pickle.loads(file_data).decode()
            file = json.loads(file_json)
            print(len(file["data"]))
            for d in file["data"]:
                item = {}
                item["duration"] = d["duration"]
                item["episodeTotal"] = d["episodeTotal"]
                item["id"] = d["id"]
                item["introduction"] = d["introduction"]
                item["link_data"] = d["link_data"]
                item["name"] = d["name"]
                item["pay"] = d["pay"]
                item["pic"] = d["pic"]
                if len(d["region"]) > 0:
                    item["region"] = d["region"][0]
                else:
                    item["region"] = "其他"

                if len(d["tags"]) == 0:
                    item["tag"] = "其他"
                else:
                    item["tag"] = d["tags"][0]
                root_dict["data"].append(item)

    with open(file_path, 'w') as wf:
        dongman = json.dumps(root_dict)
        print(dongman, type(dongman))
        wf.write(dongman)


# achieve_data()
parse_data()
