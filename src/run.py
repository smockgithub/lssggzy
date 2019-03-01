#coding:utf-8
import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'http://www.lssggzy.com/lsweb/jyxx/071002/071002005/071002005001/')
if(r.status==200):
    print(r.data)
else:
    print("error:",r.status)