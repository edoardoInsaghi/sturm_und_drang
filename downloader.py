import os
import datetime
import time
import urllib.request


def download(timestamp, hours_interval=2, show_dir=False):

    while timestamp <= datetime.datetime.now():

        tp_str = timestamp.strftime("%Y/%m/%d/%H/00")   # 'need for url

        tp_file_name = tp_str.replace("/", "-")  # 'need for filename

        if f"image{tp_file_name}.png" not in os.listdir("data"):

            url = f'https://www.blitzortung.org/en/History/{tp_str}/image_b_hu.png'

            response = urllib.request.urlopen(url)
            data = response.read()

            with open(f"data/image{tp_file_name}.png", "w+b") as f:
                f.write(data)

        timestamp += datetime.timedelta(hours=hours_interval)

        time.sleep(0.05)

    if show_dir:
        print(os.listdir("data"))


first_timestamp = datetime.datetime(2018, 5, 30, 18, 0)   # 'initial timestamp
download(first_timestamp)



