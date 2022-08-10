import telegram
import time
import os
import random
import argparse
from dotenv import load_dotenv


def send_images_to_telegram(images, chat_id, sleep=14400):
    count = 0
    try:
        while True:
            for address, dirs, files in images:
                for file in files:
                    file_adress = os.path.join(address, file)
                    bot.send_photo(
                        chat_id=chat_id,
                        photo=open(file_adress, 'rb'),
                    )
                    count += 1
                    if count >= len(files):
                        random.shuffle(files)
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

if __name__ == '__main__':
    load_dotenv()
    token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=token)
    images = list(os.walk('images'))
    chat_id = '@cosmofotomaks'
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
        