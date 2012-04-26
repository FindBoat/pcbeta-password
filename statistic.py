#!/usr/bin/env python
# coding=utf-8
from user import User

stat = {}
u = User()
for k in u.reg_dict.keys(): stat[k] = 0

def get_stat(file_names):
    global keys
    for file_name in file_names:
        f = open(file_name, 'r')
        line = f.readline()
        while line:
            s = repr(line)
            t = s[2: len(s) - 5].split(', ')
            user = User()
            user.parse_from_str(t)
            for k in user.info.keys():
                if not user.info[k] == 'None' and not user.info[k] == '00/00' and not user.info[k] == '\\xe4\\xbf\\x9d\\xe5\\xaf\\x86':
                    stat[k] += 1
            print stat
            line = f.readline()
        f.close()
    total = stat['uid']
    for k in stat.keys():
        stat[k] = stat[k] * 1.0 / total
    print total
    print stat


if __name__ == '__main__':
    get_stat(['user_info0', 'user_info1', 'user_info2', 'user_info3', 'user_info4',
              'user_info5', 'user_info6', 'user_info7', 'user_info8', 'user_info9', 'user_info10'])
