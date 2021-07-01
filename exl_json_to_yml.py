#!/usr/bin/env python
import json
import yaml
from urllib.request import urlopen

url = "http://sd-99892.dedibox.fr:5555/exl_hands_on_lab/feeds.json"

data = json.loads(urlopen(url).read())
print(yaml.safe_dump(data))
