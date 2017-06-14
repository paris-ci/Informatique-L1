# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

"""

"""

import urllib.request
import hashlib

import time

md5s = []
try:
    with open('current.txt', 'r') as infile:
        current = int(infile.readline())
    print("Read last image : " + str(current))

    md5s.append(hashlib.md5(open("{current}.png".format(current=str(current - 1).zfill(6)),'rb').read()).hexdigest())
    print("Got MD5 for last image : " + str(md5s[0]))
except FileNotFoundError:
    current = 1
    print("No current file to read")




def download_image(url:str, name:str):
    urllib.request.urlretrieve(url, name)

try:
    while True:

        downloaded = False
        while not downloaded:
            try:
                download_image("http://m.sytadin.fr//carto/dynamique/emprises/segment_TOTALE.png", "{current}.png".format(current=str(current).zfill(6)))
                new_md5 = hashlib.md5(open("{current}.png".format(current=str(current).zfill(6)),'rb').read()).hexdigest()
                print("Got MD5 : " + str(new_md5))

                if new_md5 not in md5s:
                    print("Downloaded {filename}".format(filename=str(current).zfill(6) + ".png"))
                    current += 1
                    downloaded = True
                    md5s.append(new_md5)
                else:
                    print("Same image as before, not downloading")

                time.sleep(60)
            except urllib.error.ContentTooShortError:
                pass





except KeyboardInterrupt:
    with open('current.txt', 'w') as outfile:
        outfile.write(str(current))
