#!/usr/bin/env python
from sets import Set

def get_username(file_names, save_file):
    usernames = []
    for file_name in file_names:
        f = open(file_name, 'r')
        line = f.readline()
        while line:
            s = repr(line)
            t = s[2: len(s) - 5].split(', ')
            usernames.append(t[0])
            print 'get username: %s' % t[0]
            line = f.readline()
        f.close()
    f = open(save_file, 'w')
    for name in usernames: f.write(name + ' ')
    f.close()

def get_csdn_usernames(file_name, save_file):
    usernames = []
    f = open(file_name, 'r')
    line = f.readline()
    count = 0
    while line:
        count += 1
        s = repr(line)
        index = s.find(' #')
        usernames.append(s[1: index])
        print '%s get username: %s' % (count, s[1: index])
        line = f.readline()
    f.close()
    f = open(save_file, 'w')
    for name in usernames: f.write(name + ' ')
    f.close()


if __name__ == '__main__':
#    get_csdn_usernames('csdn.sql', 'csdn_usernames')
    # get_username(['user_info0', 'user_info1', 'user_info2', 'user_info3', 'user_info4',
    #               'user_info5', 'user_info6', 'user_info7', 'user_info8', 'user_info9',
    #               'user_info10'], 'usernames')
    f = open('usernames', 'r')
    d = f.read()
    usernames1 = d[0: len(d) - 1].split(' ')
    f.close()
    f = open('csdn_usernames', 'r')
    d = f.read()
    usernames2 = d[0: len(d) - 1].split(' ')
    f.close()
    u1 = Set(usernames1)
    u2 = Set(usernames2)
    intersect = u1 & u2
    f = open('intersect', 'w')
    for u in intersect: f.write(u + '\n')
    f.close()
    print len(intersect)

