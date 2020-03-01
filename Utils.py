# -*- coding: utf-8 -*-

from requests import get

def WriteTextAsFile(filename, text):
    with open(filename, 'w') as f:
        f.write(text)
        f.close()

def DownloadContent(url, filename=None):
    if filename == None:
        filename = url.split('/')[-1]

    resp = get(url)
    with open(filename, 'wb') as f:
        f.write(resp.content)
        f.close()
