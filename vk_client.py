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
    