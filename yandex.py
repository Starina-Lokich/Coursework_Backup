import requests
from datetime import datetime
import json
import logging


class YandexDisk:

    def __init__(self, yandex_token):
        self.yandex_token = yandex_token
        self.url = "https://cloud-api.yandex.net/v1/disk/"
        self.headers = {
            'Content-Type': 'application/json',
            "Authorization": yandex_token
        }
        
    def creat_folder(self, name_folder):
        '''
        Функция создает папку на YandexDisk
        '''

        self.params = {
            "path" : name_folder
        }
        self.response = requests.put(self.url + "resources", 
                                    headers = self.headers, 
                                    params = self.params)
