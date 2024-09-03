#from filestack import Client
import requests

class FileSharer:
    def __init__(self, filepath, client_id):
        self.filepath = filepath
        self.client_id = client_id

    def share(self):
        headers = {'Authorization': f'Client-ID {self.client_id}'}
        with open(self.filepath, 'rb') as file:
            response = requests.post('https://api.imgur.com/3/upload', headers=headers, files={'image': file})
        link = response.json()['data']['link']
        return link


