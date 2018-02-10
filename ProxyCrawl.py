# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

def GetIP(url, headers):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    ipSet = soup.find_all('tr')
    ipList = []
    for i in range(1,len(ipSet)):
        ipInfo = ipSet[i]
        tds = ipInfo.find_all('td')
        ipList.append('http://' + tds[1].text + ':' + tds[2].text)
    return ipList


def GetProxyIPList():
    """
    从xicidaili爬取1000个IP，并返回
    由于此IP代理有效性太低，故选择1000个，能满足20个可用
    """

    proxyUrl = 'http://www.xicidaili.com/wt/'
    proxyHeaders = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/56.0.2924.87 Safari/537.36'
    }
    proxyIPList = []
    for i in range(1,10):
        proxyUrl = proxyUrl + str(i)
        proxyIP = GetIP(proxyUrl, proxyHeaders)
        proxyIPList.extend(proxyIP)

    return proxyIPList
