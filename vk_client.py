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
    