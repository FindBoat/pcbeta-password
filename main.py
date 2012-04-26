#!/usr/bin/env python
import re
from login import login
from http_utils import http_get
from user import User
import time

def get_uid_list(html):
    pattern = re.compile('a href=\"space-uid-(\d+).html\"')
    uid_list = pattern.findall(html)
    return uid_list

def get_all_uid(start_page):
    f = open('uid', 'a')
    for page in range(start_page, 7754):
        print 'getting uid from page %s' % page
        url = 'http://mac.pcbeta.com/member.php?action=list&listgid=&srchmem=&order=uid&type=&page=%s' % page
        html = http_get(url)
        if html is None: return
        uid_list = get_uid_list(html)
        if len(uid_list) == 0: return
        print uid_list
        for uid in uid_list: f.write(str(uid) + ' ')
        f.write('\n')
        print 'write to file'
    f.close()

def get_uid_from_file(file_name):
    f = open(file_name, 'r')
    uid = []
    line = f.read()
    s = repr(line)
    uid = s[2: len(s) - 3].split('\\n ')
    f.close()
    return uid

def get_user_info(save_file, uid_list, start):
    f = open(save_file, 'a')
    f2 = open('log', 'a')
    find = (start == -1)
    i = 0
    while i < len(uid_list):
        if find:
            print 'processing uid#%s' % uid_list[i]
            url = 'http://mac.pcbeta.com/space-uid-%s.html' % uid_list[i]
            user = User()
            html = http_get(url)
            if html is None:
                time.sleep(10)
                continue
            user.parse(html)
            if user.is_valid():
                f.write(str(user) + '\n')
                print 'write to file'
            else:
                login()
                i -= 1
        else:
            if uid_list[i] == str(start): find = True
        i += 1
    f.close()
    f2.close()

    
if __name__ == '__main__':
    login()
    uid_list = get_uid_from_file('spo10.txt')
    get_user_info('user_info10', uid_list, 2189466)



