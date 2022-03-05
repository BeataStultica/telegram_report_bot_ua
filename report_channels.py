import asyncio
import datetime
import random

from telethon import TelegramClient
from telethon import errors
from telethon import functions, types

from report_message_generator import generate_report_message
from client_factory import ClientFactory
from channels_database import ChannelsDatabase
from csv import writer

client = ClientFactory.create_client(session_name="report")
print('Bot started')


async def main():
    # тут задаєте кількість каналів, після яких програма закінчить надсилати скарги
    number_of_channels_rep = 1000
    number_completed = 0
    channels_db = ChannelsDatabase()

    while number_completed < number_of_channels_rep:
        for telegram_channel in channels_db.channels_iterator():
            try:
                result = await client(functions.account.ReportPeerRequest(
                    peer=telegram_channel,
                    reason=types.InputReportReasonViolence(),
                    message=generate_report_message())
                )
                print(telegram_channel.strip(), result)
            except ValueError:
                print("Channel not found")
                number_completed -= 1
            except errors.UsernameInvalidError:
                print("Nobody is using this username, or the username is unacceptable")
            except errors.FloodWaitError as e:
                seconds_left = e.seconds
                while seconds_left > 0:
                    print("Flood wait error. Waiting for ", str(datetime.timedelta(seconds=seconds_left)))
                    seconds_left -= 60
                    await asyncio.sleep(60)
            number_completed += 1
            with open('reported.csv', 'a', newline='\n') as f_object:
                writer_obj = writer(f_object)
                writer_obj.writerow([telegram_channel])
                f_object.close()
            # замість 10 можна написати меншу або більшу затримку, що пришвидшить надсилання скарг,
            #  але можливо збільшить шанс бану (можливо бан за таке не дають, але лишній захист не зашкодить)
            await asyncio.sleep(10 + 2 * random.random())


with client:
    client.loop.run_until_complete(main())
