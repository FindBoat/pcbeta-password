#!/usr/bin/env python
import urllib, urllib2, cookielib

def http_get(url):
    print 'http get %s' % url
    try:
        req = urllib2.Request(url)
        html = urllib2.urlopen(req).read().decode('gbk').encode('utf8')
    except Exception, e:
        print 'exception: %s'% str(e)
        return None
    return html

if __name__ == '__main__':
    print http_get('http://mac.pcbeta.com/space-uid-1.html')

