import os
import questionary
import configparser

from telethon import TelegramClient


class ClientFactory:

    @staticmethod
    def create_client(credentials_path='config.ini', session_name="new"):
        if os.path.exists(credentials_path):
            config = configparser.ConfigParser()
            config.read(credentials_path)
            api_id = config['TelegramApi']['api_id']
            api_hash = config['TelegramApi']['api_hash']
        else:
            api_id = int(questionary.password('Api ID:').ask())
            api_hash = questionary.password('Api hash:').ask()

            config = configparser.ConfigParser()
            config['TelegramApi'] = {'api_id': api_id,
                                     'api_hash': api_hash,
                                     }
            with open(credentials_path, 'w') as configfile:
                config.write(configfile)

        client = TelegramClient('session_{}'.format(session_name), api_id, api_hash)
        client.start()
        return client
