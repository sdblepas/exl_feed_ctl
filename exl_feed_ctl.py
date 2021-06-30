import json
import sys
from urllib.request import urlopen

url = "http://sd-99892.dedibox.fr:5555/exl_hands_on_lab/feeds.json"

method = sys.argv[1]

if method == 'list':
    #pass the JSON to a dict to print the value of a key
    data = json.loads(urlopen(url).read())
    field_name = sys.argv[2]

    for feed in data['feeds']:
        print(feed[field_name])

elif method == 'set':
        #still using the dict
        data = json.loads(urlopen(url).read())

        id = sys.argv[2]
        field_name = sys.argv[3]
        field_value = sys.argv[4]

def mapFeed(feed):
    if str(feed['id']) == str(id):
        feed[field_name] = field_value
        return feed
    else:
        return feed
#now using list and calling the function on all the feeds
data['feeds'] = [ mapFeed(feed) for feed in data['feeds'] ]
print(data)

#OLD CODE TO DISCUSS
#import json
#from urllib.request import urlopen
#from jsonpath_ng import jsonpath, parse


#url = "http://sd-99892.dedibox.fr:5555/exl_hands_on_lab/feeds.json"

#data = urlopen(url).read()
#exl_json = json.loads(data)

#type = str(input())

#def list_key(type):
#    jsonpath_expression = parse('feeds[*].{}'.format(type))
#    for match in jsonpath_expression.find(exl_json):
#       print(f'{type}: {match.value}')
#list_key(type)
