import sys
import urllib
import urllib2
import uuid
import datetime,time
import hmac,hashlib
import json

access_id = "xxx"
access_secret = "Jn"
def domain():
    salt = str(uuid.uuid1())
    now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    url = "http://alidns.aliyuncs.com/?Format=JSON&AccessKeyId="+access_id+"&Action=DescribeDomainRecords&PageSize=200&SignatureMethod=HMAC-SHA1&DomainName=xzxpay.com&SignatureNonce="+salt+"&SignatureVersion=1.0&Version=2015-01-09&Timestamp="+now
    now1 = urllib.quote(now)
    para = "AccessKeyId="+access_id+"&Action=DescribeDomainRecords&DomainName=xzxpay.com&Format=JSON&PageSize=200&SignatureMethod=HMAC-SHA1&SignatureNonce="+salt+"&SignatureVersion=1.0&Timestamp="+now1+"&Version=2015-01-09"
    middlesign = "GET"+"&"+"%2F"+"&"+urllib.quote(para)
    secret = access_secret+"&"
    sign = hmac.new(secret,middlesign,hashlib.sha1).digest().encode('base64')
    url = url+"&Signature="+sign

    req = urllib2.Request(url)
    try:
        res = urllib2.urlopen(req)
        a = res.read()
        rtdict = json.loads(a)
        print rtdict["DomainRecords"]["Record"]
        return rtdict["DomainRecords"]["Record"]
    except urllib2.HTTPError,a:
        print a.reason
        print a.read()
        print a.code
    
def addrecord(dname,value,dtype="A"):
#    dtype = "A"
    print dname,value,dtype
    salt = str(uuid.uuid1())
    now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    now1 = urllib.quote(now)
    url = "http://alidns.aliyuncs.com/?AccessKeyId="+access_id+"&Action=AddDomainRecord&DomainName=xzxpay.com&Format=JSON&PageSize=200&RR="+dname+"&SignatureMethod=HMAC-SHA1&SignatureNonce="+salt+"&SignatureVersion=1.0&Timestamp="+now1+"&Type="+dtype+"&Value="+value+"&Version=2015-01-09"
    para = "AccessKeyId="+access_id+"&Action=AddDomainRecord&DomainName=xzxpay.com&Format=JSON&PageSize=200&RR="+dname+"&SignatureMethod=HMAC-SHA1&SignatureNonce="+salt+"&SignatureVersion=1.0&Timestamp="+now1+"&Type="+dtype+"&Value="+value+"&Version=2015-01-09"
    middlesign = "GET"+"&"+"%2F"+"&"+urllib.quote(para)
    secret = access_secret+"&"
    sign = hmac.new(secret,middlesign,hashlib.sha1).digest().encode('base64')
    url = url+"&Signature="+sign
    req = urllib2.Request(url)
    try:
        res = urllib2.urlopen(req)
        a = res.read()
        rtdict = json.loads(a)
        print rtdict
    except urllib2.HTTPError,a:
        print a.reason
        print a.read()

def removerecord(rid):
    salt = str(uuid.uuid1())
    now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    now1 = urllib.quote(now)
    url = "http://alidns.aliyuncs.com/?AccessKeyId="+access_id+"&Action=DeleteDomainRecord&DomainName=xzxpay.com&Format=JSON&PageSize=200&RecordId="+rid+"&SignatureMethod=HMAC-SHA1&SignatureNonce="+salt+"&SignatureVersion=1.0&Timestamp="+now1+"&Version=2015-01-09"
    para = "AccessKeyId="+access_id+"&Action=DeleteDomainRecord&DomainName=xzxpay.com&Format=JSON&PageSize=200&RecordId="+rid+"&SignatureMethod=HMAC-SHA1&SignatureNonce="+salt+"&SignatureVersion=1.0&Timestamp="+now1+"&Version=2015-01-09"
    middlesign = "GET"+"&"+"%2F"+"&"+urllib.quote(para)
    secret = access_secret+"&"
    sign = hmac.new(secret,middlesign,hashlib.sha1).digest().encode('base64')
    url = url+"&Signature="+sign
    req = urllib2.Request(url)
    try:
        res = urllib2.urlopen(req)
        a = res.read()
        rtdict = json.loads(a)
        print rtdict
    except urllib2.HTTPError,a:
        print a.reason
        print a.read()
    

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "usage:{show} {add name ip} {remove name}"
    elif sys.argv[1] == "show":
        domain()
    elif sys.argv[1] == "add":
        addrecord(sys.argv[2],sys.argv[3],sys.argv[4])
    elif sys.argv[1] == "remove":
        rtlist = domain()
        for srt in rtlist:
            if srt["RR"]==sys.argv[2]:
                dnsid = srt["RecordId"]
                break
        removerecord(dnsid)
    else:
        print "unknow argument.\nusage:{show} {add name ip} {remove name}"
