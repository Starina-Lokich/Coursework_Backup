import vk_client as vk_client
import yandex as yandex


ya_token = input("Введите Яндекс токен: ")
user_id = int(input("Введите id вашего прфиля: "))
token = input("Введите VK токен: ")
name_folder = input("Введите имя папки: ")


vk = vk_client.VkUser(token, user_id)
photos_urls = vk.photo_url()

disk = yandex.YandexDisk(ya_token)
disk.save_photo_classic(name_folder, photos_urls)