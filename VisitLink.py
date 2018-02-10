# -*- coding: utf-8 -*-
from ProxyCrawl import *
import requests

def GetUserConfig():
    file = open ("config.txt","r")
    uid = file.readline()
    pid = file.readline()
    file.close()

    uid = uid.strip("\n")
    pid = pid.strip("\n")
    payload = {'pid':pid, 'uid':uid}

    UpdatePid(uid,pid)
    return payload

def UpdatePid(uid,pid):

    file = open("config.txt","w")
    file.write(uid + "\n")
    writeBackPid = str(int(pid) + 1)
    file.write(writeBackPid)
    file.close()

def MyJob():
    proxyIPList = GetProxyIPList()
    payload = GetUserConfig()
    for ip in proxyIPList:
        counter = 0
        proxyLog = {'http': ip}
        try:
            response = requests.get('http://www.maimemo.com/share/page/', params = payload, proxies=proxyLog)
            counter += 1
            if counter == 30:
                break
        except:
            continue

