#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests as rq
import json 
heroes = ['Hulk', 'Captain America', 'Thanos']
token = '2619421814940190'
url ='https://superheroapi.com/api/'
intel1 = 0
for hero in heroes:
    request = rq.get(url+token+'/search/'+hero)
    request = request.content
    response = json.loads(request)
    intel = int(response['results'][0]['powerstats']['intelligence'])
    if intel > intel1:
        intel1 = intel
        most_intel = hero
print(f'Самым умным является {most_intel}')


# In[ ]:




