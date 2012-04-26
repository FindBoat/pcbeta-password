#!/usr/bin/env python
# coding=utf-8
import re
import login, http_utils
class User(object):
    reg_dict = {'username': 'MacIdea</a> &raquo; ([\s\S]+)的个人资料</div>',
                'uid': 'UID: (\d+)',
                'sex': '<th width="70">性别:</th>\r\n<td>\r\n([\s\S]{0,8})</td>\r\n</tr>',
                'home': '<th width="70">来自:</th>\r\n<td>\r\n ([\s\S]{0,50})</td>\r\n</tr>',
                'birth': '<th width="70">生日:</th>\r\n<td>\r\n([\s\S]{0,50})</td>\r\n</tr>\r\n</table>',
                'site': '<th>个人网站:</th>\r\n<td><a href="([\s\S]{0,50})" target="_blank">',
                'qq': 'http://wpa.qq.com/msgrd\?V=1&amp;Uin=([\s\S]{0,12})&amp;',
                'icq': '<th>ICQ:</th>\r\n<td>([\s\S]{0,20})</td>\r\n</tr>', 
                'yahoo': '<th>Yahoo:</th>\r\n<td>([\s\S]{0,70})</td>\r\n</tr>\r\n<tr>\r\n<th>MSN:</th>',
                'aliww': '<th>阿里旺旺:</th>\r\n<td><script type="text/javascript">([\s\S]*)</script></td>\r\n</tr>',
                'taobao': '<th>支付宝账号:</th>\r\n<td>([\s\S]{0,70})</td>\r\n</tr>',
                'pc': '<th>机型:</th>\r\n<td>\r\n([\s\S]{0,70})&nbsp;\r\n</td>\r\n</tr><tr>\r\n<th>系统:</th>',
                'os': '<th>系统:</th>\r\n<td>\r\n([\s\S]{0,70})&nbsp;\r\n</td>\r\n</tr><tr>\r\n<th>设备:</th>',
                'device': '<th>设备:</th>\r\n<td>\r\n([\s\S]{0,10})&nbsp;\r\n</td>\r\n</tr>',
                'interest': '<th>性向:</th>\r\n<td>\r\n([\s\S]{0,50})&nbsp;\r\n</td><tr>\r\n<th>iChat:</th>',
                'ichat': '<th>iChat:</th>\r\n<td>\r\n([\s\S]{0,70})&nbsp;\r\n</td>\r\n</tr></table>'}
    info = {}
    
    def __init__(self): pass

    def is_valid(self):
        if self.info['uid'] == 'None': return False
        return True

    def parse(self, html):
        try:
            for k in self.reg_dict.keys():
                pattern = re.compile(self.reg_dict[k])
                m = pattern.findall(html)
                if len(m) > 0 and len(m[0]) > 0:
                    self.info[k] = m[0]
                else:
                    self.info[k] = 'None'
            print self.info
        except Exception, e:
            print 'exception: %s' % str(e)

    def parse_from_str(self, s):
        # too sb.............................
        keys = ['username', 'qq', 'aliww', 'uid', 'birth', 'yahoo', 'site', 'pc', 'ichat', 'taobao', 
                'interest', 'device', 'home', 'icq', 'sex', 'os']
        if not len(s) == len(keys):
            print 'invalid string'
        else:
            for i in range(len(s)):
                self.info[keys[i]] = s[i]
    
    def __str__(self):
        s = ''
        for k in self.info.keys(): s += self.info[k] + ', '
        return s
    
if __name__ == '__main__':
    user = User()
    login.login()
    html = http_utils.http_get('http://mac.pcbeta.com/space-uid-2570038.html')
    user.parse(html)
    print str(user)
    
