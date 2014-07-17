#!/usr/bin/env python
#coding:utf-8
# Author:  firmlyjin@gmail.com --<best love at buddha>
# Purpose: 
# Created: 2013-5-16

import subprocess

def subpros(cmd):
    """return value if success otherwise return False"""
    a = subprocess.Popen(cmd, shell = False, stdout = subprocess.PIPE)
    #a.wait()
    if a.poll() == 0 or a.poll() == None: #假如cmd命令执行成功，返回0
        #self.loger(self.curtime()+ "\t" + u"连接subprocess成功")
        b = a.stdout.read()
        try:
            if str(b.split(":")[0]) != "Error":
                print  u"连接subprocess执行命令\"%s\""%cmd
                #self.loger(self.curtime()+ "\t" + u"连接subprocess执行命令\"%s\""%cmd)
            else:
                print   u"执行命令\"%s\"时\n"%cmd + '\t出现错误:\n' + b
                #self.loger(self.curtime()+ "\t" +  u"执行命令\"%s\"时\n"%cmd + '\t出现错误:\n' + b)
        except: pass
    else:
        #dlg = wx.MessageDialog(None, u'无法连接设备!\n\n请查看ADB线是否插上',
        #          'MessageDialog', wx.OK | wx.ICON_QUESTION)
        #result = dlg.ShowModal()
        #dlg.Destroy()
        #self.loger(self.curtime()+ "\t" + u'无法连接设备!请查看ADB线是否插上' + '\n')
        b = False
    try: a.kill()
    except: pass
    return b

if __name__=='__main__':
    subpros('pwd')