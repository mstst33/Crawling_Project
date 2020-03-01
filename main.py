# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import Utils

if __name__ == '__main__':
    fileext = '.html'
    imgurl = "https://t1.daumcdn.net/cfile/tistory/250AB44353D20E5036"
    url = "https://media.daum.net"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")

    # Utils.DownloadContent(imgurl, 'green.jpg') # Downlodad Image as bytes array
    # Utils.WriteTextAsFile("page.html", res.text) # Downlodad HTML as test
    sections = soup.select('.gnb_comm .link_gnb')
    s_txt = ''
    
    for section in sections:
        tmpurl = url + section['href']
        if section['href'] != '/':
            print(tmpurl)
            tmpres = requests.get(tmpurl)
            filename = section['href'].split('/')[1]
            Utils.WriteTextAsFile(filename + fileext, tmpres.text)

            tmpsoup = BeautifulSoup(tmpres.content, 'html.parser')
            title = tmpsoup.select('div.cont_thumb .tit_thumb .link_txt')

            s_txt += filename + '\n'
            for t in title:
                s_txt += t.get_text() + ' link(' + t['href'] + ')\n'
                print(t.get_text())
            tmpres.close()
            s_txt += '------------------------------------------------\n'
        
        print('------------------------------------------------')
    Utils.WriteTextAsFile('result.txt', s_txt)

    
