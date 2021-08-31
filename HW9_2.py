#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pprint import pprint
import requests
import json
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str, path_ya: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        self.file_path = path_to_file
        self.path_ya = path_ya
        url = 'https://cloud-api.yandex.net/v1/disk/'
        publish = 'resources/upload'
        docs = open(self.file_path, 'rb')
        headers = {'accept': 'application/json', 'authorization' : f'OAuth {self.token}'}
        params = {"path": docs}
        r=requests.get(url+publish, headers=headers, params={'path':self.path_ya})
        #print(r.json())
        urlu = r.json()['href']
        r = requests.put(urlu, headers=headers, files = {'file' : docs})


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input('Введите путь до файла: ')
    token = input('Введите Ваш токен: ')
    path_ya = input('Введите путь или папку, по которому (в которой) сохранится файл на Яндекс.диск без указания имени загружаемого файла: ')
    name = []
    for i in path_to_file.split('\\'):
        name += [i]
    name = '/'+name[-1]
    path_ya = path_ya+name
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, path_ya)
    #result2 = uploader.upload(path_ya)


# In[ ]:




