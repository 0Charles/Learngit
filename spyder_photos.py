# -*- coding: utf-8 -*-
"""
Created on 2019/1/28 20:46

@author: li
"""

import requests
import json
import time
from contextlib import closing


class GetPhotos(object):
    def __init__(self):
        self.photos_id = []
        self.download_sever = 'https://unsplash.com/photos/xxx/download?force=true'
        self.download_target = 'https://unsplash.com/napi/collections/3356568/photos?page=1&per_page=20&order_by=latest'

    def get_id(self):
        req = requests.get(url=self.download_target, verify=False)
        html = json.loads(req.text)
        for each in html:
            self.photos_id.append(each['id'])
        time.sleep(1)

    def download(self, photo_id, filename):
        target = self.download_sever.replace('xxx', photo_id)
        with closing(requests.get(url=target, stream=True, verify=False)) as r:
            with open('%d.jpg' % filename, 'ab+') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()


if __name__ == '__main__':
    gp = GetPhotos()
    print('获取图片链接中:')
    gp.get_id()
    print('图片下载中:')
    for i in range(len(gp.photos_id)):
        print('正在下载第%d张图片' % (i + 1))
        gp.download(gp.photos_id[i], i + 1)


# if __name__ == '__main__':
#     target = 'https://unsplash.com/napi/collections/3356568/photos?page=1&per_page=20&order_by=latest'
#     req = requests.get(url=target, verify=False)
#     html = json.loads(req.text)
#     print(html[0])
#     print(html[0]['links']['download_location'])
