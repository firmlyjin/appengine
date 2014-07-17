# coding=utf-8

from urllib2 import urlopen
from time import sleep
from engine import url


@url("/")
def hello(environ, start_response):
    s = "Hello, World!\n"

    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(s)))
    ])

    return s


@url("/async")
def async(environ, start_response):
    sleep(0.01)
    s = "Hello, World!\n"

    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(s)))
    ])

    return s


@url("/remote")
def remote(environ, start_response):
    s = urlopen("http://220.181.40.167:8080").read()

    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(s)))
    ])

    return s

@url("/testssh")
def testssh(environ, start_response):
    sleep(0.01)
    curDir = getcwd()        
    shellDir =  path.join(curDir, "shell")        
    greRsaCmd = ["/bin/sh", shellDir + "/greRSA.sh"] #制作RSA文件并远程传递给各个远程IP
    subpros(greRsaCmd)
    ipadds = open(shellDir+ "/ip.txt").readlines()        #查探各个IP的挂载盘信息并得到返回值
    print ipadds
    vals = ""
    for ip in ipadds:        
        val = subpros(["/bin/sh", shellDir + "/remote.sh", ip.strip()])             
        vals += "<h2>%s</h2>"%ip + val + "\n"

    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(vals)))
    ])

    return  vals   