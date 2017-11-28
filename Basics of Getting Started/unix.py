#! /usr/bin/python
# -*- coding: utf-8 -*-
import crypt

def testPass(cryptPass):    # 加密的口令hash
    salt = cryptPass[0:2]   # 提取加密的口令hash前两个字符视为salt
    dictFile = open('dictionary.txt', 'r')   # 读取字典里的所有单词
    for word in dictFile.readlines():        # 遍历字典中的每一个单词
        word = word.strip('\n')              # 提取单个单词
        cryptWord = crypt.crypt(word, salt)  # 用每个单词和salt计算一个新的加密口令hash
        if cryptWord == cryptPass:           # 如果结果与加密口令hash匹配
            print '[+] Found Password: ' + word + '\n'  # 显示找到密码
            return                           # 找到密码，返回
    print '[-] Password Not Found.\n'     # 搜遍字典无果
    return                                # 没有找到密码，返回

def main():
    passFile = open('passwords.txt')    # 打开加密口令文件"passwords.txt"
    for line in passFile.readlines():   # 逐行读取口令文件中的内容
        if ':' in line:          
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')   # 每一行的用户名和口令hash都是分隔开的
            print '[*] Cracking Password For: ' + user
            testPass(cryptPass)     # 调用testPass()函数，尝试用字典中的单词破解口令hash

if __name__ == '__main__':
    main()