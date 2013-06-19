#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, time
import pprint, urllib2
import sys

def internet_on():
    try:
        response = urllib2.urlopen('http://74.125.224.72/',timeout=1)
        return True
    except urllib2.URLError as err: 
        pass
    return False

def get_all(user, max_depth=5,after=None):
    """recursive function to keep fetching pages (reddit limits to batches of 100)"""
    
    url = "http://www.reddit.com/user/"+user+"/comments.json?limit=100"
    if after:
        url += "&after="+after
        
    print max_depth, url
    r=requests.get(url)
    j = r.json()
    
    if j['data']['after'] and max_depth > 0:
        time.sleep(2)
        return j['data']['children'] + get_all(user, max_depth-1, j['data']['after'])
    else:
        return j['data']['children'] 

def user_exist(user):
    url = "http://www.reddit.com/user/"+user+"/about.json"
    
    r = requests.get(url)
    result = r.json()
    pprint.pprint(result)
    try:
        print "Erro: " + str(result['error']) +". User não existe."
        return False
    except KeyError:
        return True
    

def main():
    if internet_on() == False:
        print "Nao tens net"
        sys.exit(0)
    
    user = str(raw_input('User='))
    user_exist(user)
    
    x = int(raw_input('comments 100 + n100. n= '))
    #data = get_all(user, x) # go get a quick coffee now
    #print len(data)
    #pprint.pprint(data)

main()