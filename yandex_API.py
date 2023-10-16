import requests

from xxx import token

class MyYandexDisk:
    def __init__(self, token):
        self.token = token
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def creating_folder(self, folder_path):
        '''Метод создает папку'''
        response = requests.put(f'{self.url}?path={folder_path}', headers=self.headers)
        return response.status_code


    def upload_file(self, load_file, save_file, replace=False):
        '''Метод загружает файлы'''
        res = requests.get(f'{self.url}/upload?path={save_file}&overwrite={replace}', headers=self.headers).json()
        with open(load_file, 'rb') as f:
            r = requests.put(res['href'], files={'file': f})
            return r.status_code
    
        
if __name__ == '__main__':
    MyYandexDisk(token)