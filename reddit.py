#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, time, pprint

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
    
    return result

def main():
    user = str(raw_input('User='))
    x = int(raw_input('comments x100='))
    
    data = user_exist(user)
    #data = get_all(user, x) # go get a quick coffee now
    print len(data)
    pprint.pprint(data)

main()