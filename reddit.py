import requests, time
import pprint

def get_all(max_depth=5,after=None):
    """recursive function to keep fetching pages (reddit limits to batches of 100)"""
    
    url = "http://www.reddit.com/user/zemike/comments.json?limit=100"
    if after:
        url += "&after="+after
        
    print max_depth, url
    r=requests.get(url)
    j = r.json()
    
    if j['data']['after'] and max_depth > 0:
        time.sleep(2)
        return j['data']['children'] + get_all(max_depth-1, j['data']['after'])
    else:
        return j['data']['children'] 

data = get_all(15) # go get a quick coffee now
print len(data)
pprint.pprint(data[0])
