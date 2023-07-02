import requests
from dotenv import dotenv_values

from .printer import Printer


class Daddy:
    def __init__(self):
        self.printer = Printer('[GoDaddy]')
        config = dotenv_values('.env')
        self.api_key = config['GO_DADDY_API_KEY']
        self.api_secret = config['GO_DADDY_API_SECRET']

    def print(self, *args):
        return self.printer.print(*args)

    def is_available(self, domain):
        headers = {'Authorization': f'sso-key {self.api_key}:{self.api_secret}'}
        response = requests.get(f'https://api.godaddy.com/v1/domains/available?domain={domain}', headers=headers)
        try:
            response.raise_for_status()
        except Exception as e:
            self.printer.error(e)
            return
        data = response.json()
        available = data['available']
        return available
