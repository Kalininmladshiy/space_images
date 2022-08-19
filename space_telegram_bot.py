import telegram
import time
import os
import random
import argparse
from dotenv import load_dotenv


def send_images_to_telegram(images, chat_id, sleep=14400):
    count = 0
    files_path = get_files_path(images)
    try:
        while True:
            for file_path in files_path:
                bot.send_photo(
                    chat_id=chat_id,
                    photo=open(file_path, 'rb'),
                )
                count += 1
                if count >= len(files_path):
                    random.shuffle(files_path)
                    count = 0
                time.sleep(sleep)
    except telegram.error.NetworkError:
        if args.delay:
            send_images_to_telegram(
                images,
                chat_id,
                sleep=args.delay,
            )
        else:
            send_images_to_telegram(
                images,
                chat_id,
            )        


def get_files_path(dirpath_and_filenames):
    files_path = []
    for address, dirs, files in dirpath_and_filenames:
        for file in files:
            file_adress = os.path.join(address, file)
            files_path.append(file_adress)
    return files_path        


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=token)
    images = list(os.walk('images'))
    chat_id = os.environ['CHAT_ID_TG']
    parser = argparse.ArgumentParser(
        description='Программа отправляет с задержкой фотографии в телеграм канал'
    )
    parser.add_argument("--delay", type=int, help="Время задержки")
    args = parser.parse_args()
    if args.delay:
        send_images_to_telegram(
            images,
            chat_id,
            sleep=args.delay,
        )
    else:
        send_images_to_telegram(
            images,
            chat_id,
        )
        