#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
弱点扫描工具
'''

import socket
import os
import sys

# 判断是否可以连接成功
def retBanner(ip, port):
    try:
        # 为 socket 对象设置默认超时时间
        socket.setdefaulttimeout(2)
        # 创建一个新的 socket
        s = socket.socket()
        # 连接远程
        s.connect((ip, port))
        # 接收数据
        banner = s.recv(1024)
        # 返回接收的数据
        return banner
    except:
        return


# 检测漏洞是否存在
def checkVulns(banner, filename):
    # 打开文件
    f = open(filename, 'r')
    # 按行读取
    for line in f.readlines():
        # 判断行是否存在于 banner 字符串中
        if line.strip('\n') in banner:
            print '[+] Server is vulnerable: ' + \
                  banner.strip('\n')


def main():
    # 判断 传递给脚本的命令行参数 个数是否等于 2
    if len(sys.argv) == 2:
        # 将第二个参数赋值给 filename
        filename = sys.argv[1]
        # 如果文件路径不存在
        if not os.path.isfile(filename):
            print '[-] ' + filename + ' does not exist.'
            exit(0)
        # 如果文件路径不可读
        if not os.access(filename, os.R_OK):
            print '[-] ' + filename + ' access denied.'
            exit(0)
    else:
        print '[-] Usage: ' + str(sys.argv[0]) + ' <vuln filename>'
        exit(0)
    # 定义端口列表
    portList = [21, 22, 25, 80, 110, 443]
    # 循环 147 - 150
    for x in range(1, 5):
        # 定义 IP 地址
        ip = '192.168.0.' + str(x)
        # 循环端口
        for port in portList:
            # 判断 ip + port 是否可以连接成功
            banner = retBanner(ip, port)
            if banner:
                print '[+] ' + ip + ' : ' + banner
                checkVulns(banner, filename)


if __name__ == '__main__':
    main()