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

    def save_photo_classic(self, name_folder, photos_urls):
        '''
        Функция загружает фотографии с аккаунта вк в Яндекс диск
        Сохраняет информацию по фотографиям в json-файл с результатами
        Создает файл "backup.log"
        '''

        self.creat_folder(name_folder)
        log_list = []
        count = 1
        name_photo_list = []
        day = datetime.today().strftime('%d-%m-%Y')
        for photo in photos_urls:
            if str(photo['likes']) not in name_photo_list:
                name_photo = str(photo['likes'])
                name_photo_list.append(name_photo)
            else:
                name_photo = f"{str(photo['likes'])}({day})"
            params = {
                "path": f"{name_folder}/{name_photo}",
                "url": photo['url']
            }
            self.response = requests.post(self.url + "resources/upload",
                                          params = params, headers = self.headers)
            print(f"Загружен {count} объект из {len(photos_urls)}")
            count += 1
            log_list.append({
                "file_name": f"{name_photo}.jpg",
                "size": photo['type']
            })
            logging.basicConfig(level=logging.INFO, filename="backup.log",filemode="a", 
                                format="%(asctime)s %(levelname)s %(message)s")
            logging.info('photo saved successfully')
        with open("result.json", "w", encoding="utf-8") as file:
            json.dump(log_list, file)
        logging.info('The program successfully saved the photos')
        print('Программа успешно загрузила фотографии')
