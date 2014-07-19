# coding=utf-8

from urllib2 import urlopen
from time import sleep
from engine import url
from os.path import  join
from os import getcwd
from Subpros import subpros
from re import compile

@url("/testssh2")
def testssh(environ, start_response):
    sleep(0.01)
    curDir = getcwd()        
    shellDir =  join(curDir, "action", "shell")        
    greRsaCmd = ["/bin/sh", shellDir + "/greRSA.sh"] #制作RSA文件并远程传递给各个远程IP
    #subpros(greRsaCmd)
    ipadds = open(shellDir+ "/ip.txt").readlines()        #查探各个IP的挂载盘信息并得到返回值
    print ipadds
    vals = ""
    comp = compile(r"^\#")
    for ip in ipadds:        
        if comp.match(ip.strip()):
            val = subpros(["/bin/sh", shellDir + "/remote.sh", ip.strip()])             
            vals += "<h2>%s</h2>"%ip + val + "\n"

    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(vals)))
    ])

    return  vals   