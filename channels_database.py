
import random
import pandas as pd
from googleapiclient.discovery import build

import httplib2 
from oauth2client.service_account import ServiceAccountCredentials	


class ChannelsDatabase:
    def __init__(self, path="telegram_db.csv"):
        self._db_main = pd.read_csv(path)
        self._db_main.sort_values(by=['priority'])

        self.CREDENTIALS_FILE = 'cleaner-342521-ec5546fa5567.json'

        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(self.CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

        self.httpAuth = self.credentials.authorize(httplib2.Http())
        self.driveService = build('drive', 'v2', http = self.httpAuth)
        self.service = build('sheets', 'v4', http = self.httpAuth)

    def channels_iterator(self, shuffle=False):
        table_channels = self.get_from_table()
        channels = self._db_main['channel'].tolist()
        channels = [item.strip() for item in channels]
        channels +=[self.clean_hash(item) for item in table_channels if self.clean_hash(item) not in channels]
        print("Кількість каналів: "+ str(len(channels)))
        reported = self.read_reported()
        channels = [item for item in channels if item not in reported]
        print("Кількість каналів, на які ще не відправлена скарга: "+ str(len(channels)))
        if shuffle:
            random.shuffle(channels)
        for telegram_channel in channels:
            yield telegram_channel
    def get_from_table(self, link='https://docs.google.com/spreadsheets/d/1UXsdKXaSWkkdCYlJJQ3Elv6NgPEmQ-wbVBTvgLV90Ss/edit#gid=0'):
        ranges = ["Telegram!A1:A99999"]
        dest_id = link.split('/')[5]
        results = self.service.spreadsheets().values().batchGet(spreadsheetId = dest_id, 
                                                ranges = ranges,
                                                majorDimension='COLUMNS', 
                                                valueRenderOption = 'FORMATTED_VALUE',  
                                                dateTimeRenderOption = 'FORMATTED_STRING').execute()
        if results['valueRanges'][0].get('values'):
            values= results['valueRanges'][0]['values'][0]
        return values
    def clean_hash(self, link):
        telegram_channel = link
        if "https://" in link:
            telegram_channel = link.split('/')[-1]
        elif '@' in link:
            telegram_channel = link[1:]
        return telegram_channel
    def read_reported(self):
        db_main = pd.read_csv('reported.csv')
        return db_main['reported'].values.tolist()
