import telegram
import time
import os
import random
import argparse
from dotenv import load_dotenv


def send_images_to_telegram(images, chat_id, sleep):
    files_path = get_files_path(images)
    while True:
            for file_path in files_path:
                with open(file_path, 'rb') as photo:
                    try:
                        bot.send_photo(
                            chat_id=chat_id,
                            photo=photo,
                        )
                        time.sleep(sleep)
                    except telegram.error.NetworkError:
                        continue
            random.shuffle(files_path)

def get_files_path(dirpath_and_filenames):
    files_path = []
    for address, dirs, files in dirpath_and_filenames:
        for file in files:
            file_address = os.path.join(address, file)
            files_path.append(file_address)
    return files_path        


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=token)
    images = list(os.walk('images'))
    chat_id = os.environ['TG_CHAT_ID']
    parser = argparse.ArgumentParser(
        description='Программа отправляет с задержкой фотографии в телеграм канал'
    )
    parser.add_argument("--delay", type=int, help="Время задержки", default=14400)
    args = parser.parse_args()
    send_images_to_telegram(
        images,
        chat_id,
        sleep=args.delay,
    )
        