import requests


class VkUser:

    API_BASE_URL = "https://api.vk.com/method/"

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def _get_common_params(self):
        return {
            "access_token": self.token,
            "v": 5.199
        }

    def photos_info(self, count = 5):
       '''
        Функция возвращает словарь 
        с информацией по фотографии(ям) из профиля пользователя
       '''

       params = self._get_common_params()
       params.update({"user_id": self.user_id, "album_id": "profile", 
                      "extended": 1, "photo_sizes": 1, "count": count})
       response = requests.get(f'{self.API_BASE_URL}photos.get', params=params).json()
       return response
    
    def photo_url(self):
        '''
        Функция возвращает словарь с информацией по фотографиям,
        а также url  фотографии максимального размера
        '''

        photos_urls = []
        photos = self.photos_info()['response']['items']
        for photo in photos:
            target_photo = None
            TYPES = 'smxopqryzw'
            for photo_size in photo['sizes']:
                if not target_photo or TYPES.find(photo_size['type']) > TYPES.find(
                        target_photo['type']): target_photo = photo_size
            photos_urls.append({'url': target_photo['url'],
                               'type': target_photo["type"],
                               'width': target_photo["width"],
                               'height': target_photo["height"],
                               'likes': photo['likes']['count'],
                               })
        sorted_photo_list = sorted(photos_urls, key=lambda x: x['height'])
        return sorted_photo_list
    