#!/usr/bin/env python
import urllib, urllib2, cookielib  
login_url = r'http://mac.pcbeta.com/logging.php?action=login&loginsubmit=yes&floatlogin=yes&inajax=1'
login_data = urllib.urlencode({'formhash': 'fe01714b',
                               'referer': 'http://mac.pcbeta.com/member.php?action=list',
                               'loginfield': 'username',  
                               'username': '11zhaohang',
                               'password': '5c915e063df6dc1c8a9a8b579d1c83b6',
                               'questionid': '0',
                               'answer': '',
                               'loginsubmit': 'true',
                               'cookietime': '2592000'})
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',  
           'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'gzip,deflate,sdch',
           'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'Content-Length': '221',
           'Content-Type': 'application/x-www-form-urlencoded',
           'Host': 'mac.pcbeta.com',
           'Origin': 'http://mac.pcbeta.com',
           'Referer': 'http://mac.pcbeta.com/member.php?action=list',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'}

def login():
    print 'login...'
    global login_url, login_data, headers
    cookieJar = cookielib.CookieJar()
    cookie_support= urllib2.HTTPCookieProcessor(cookieJar)
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    req = urllib2.Request(login_url, login_data, headers)
    try:
        r = urllib2.urlopen(req)
    except Exception, e:
        print 'exception: %s' % str(e)
        return False
    if r.code == 200:
        print 'login success'
        return True
    else:
        print 'login fail'
        return False

if __name__ == '__main__':
    login()
