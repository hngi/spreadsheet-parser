import time
import os
from datetime import datetime
from excel_parser.settings import BASE_DIR


def clear_upload():
    while True:
        time_list = []
        now = time.mktime(datetime.now().timetuple())
        directory = os.path.join(BASE_DIR, 'media/upload')
        for file in os.listdir(directory):
            file = os.path.join(directory, file)
            # get file creation/modification time
            file_time = os.path.getmtime(file)
            if now - file_time > 10:
                os.remove(file)
            else:
                # add time info to list
                time_list.append(file_time)

        # after check all files, choose the oldest file creation time from list
        # if time_list is empty, set sleep time as 300 seconds, else calculate it based on the oldest file creation time
        sleep_time = (now - min(time_list)) if time_list else 15
        time.sleep(sleep_time + 5)


def clear_download():
    while True:
        time_list = []
        now = time.mktime(datetime.now().timetuple())
        directory = os.path.join(BASE_DIR, 'media/download')
        for file in os.listdir(directory):
            file = os.path.join(directory, file)
            # get file creation/modification time
            file_time = os.path.getmtime(file)
            if now - file_time > 10:
                os.remove(file)
            else:
                # add time info to list
                time_list.append(file_time)

        # after check all files, choose the oldest file creation time from list
        # if time_list is empty, set sleep time as 300 seconds, else calculate it based on the oldest file creation time
        sleep_time = (now - min(time_list)) if time_list else 15
        time.sleep(sleep_time + 5)
