import os
import questionary
import configparser

from telethon import TelegramClient


class ClientFactory:

    @staticmethod
    def create_client(credentials_path='config.ini', session_name="new"):
        api_id = os.getenv('API_ID') if os.getenv('API_ID') is not None else int(questionary.password('Api ID:').ask())
        api_hash = os.getenv('API_HASH') if os.getenv('API_HASH') is not None else questionary.password('Api hash:').ask()

        config = configparser.ConfigParser()
        config['TelegramApi'] = {'api_id': api_id, 'api_hash': api_hash}
        
        with open(credentials_path, 'w') as configfile:
            config.write(configfile)

        client = TelegramClient('session_{}'.format(session_name), api_id, api_hash)
        client.start()
        return client
