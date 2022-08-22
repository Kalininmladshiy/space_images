# Репозиторий space_images
Данный репозиторий представляет собой совокупность программ, которые скачивают изображения космоса от NASA, SpaceX, в указанную директорию, а затем из этой директории публикуют фотографии с помощью бота в телеграм канал. Так же здесь присутствуют вспомогательные программы по скачиванию изображений из интернета, а так же определения расширения файла.

# Файл space_telegram_bot.py
Данная основная программа, подключаясь к заранее созданному боту, в автоматическом режиме публикует фотографии из директории в телеграм канал. По умолчанияю задерка составляет 4 часа, но пользователь может менять данный параметр через аргумент в терминале.

# Файл fetch_EPIC_nasa_images.py
Данная вспомогательная программа скачивает фотографии земли из космоса от NASA в высоком разрешении. Пользователь может выбрать количество фотографий для скачивания  

# Файл fetch_nasa_images.py
Данная вспомогательная программа скачивает фотографии космоса от NASA. Пользователь может выбрать количество фотографий для скачивания

# Файл fetch_spacex_images.py
Данная вспомогательная программа скачивает фотографии запуска компании SpaceX. Пользователь может выбрать запуск, фотографии которого он хочет скачать. По умолчанию скачиваются фотографии последнего запуска.

# Файл utils.py
Содержит в себе вспомогательные функции по определению расширения скачиваемого файла и скачивания фотографий из интернета.

## Переменные среды

В данной программе используются 3 переменные среды: 1. `NASA_API_KEY`. В ней находится ключ для подключения к API сервиса NASA для скачивания фотографий. 2. `TG_TOKEN`. В ней находится токен для управления телеграм ботом. 3. `TG_CHAT_ID`. В ней находится название канала, куда планируется отправлять фотографии. Создайте файл .env и пропишите в него свой токен, вот так: `TG_TOKEN=afnroeroinorf13jr94bg3fn` и на новой строке ключ от NASA `NASA_API_KEY=fhgfhgfygfygfhfgyf`. Не забудьте про `TG_CHAT_ID=@name_of_channel` Файл поместите в папку с проектом. Чтобы создать такой файл вам может понадобиться текстовый редактор. Для Windows это Notepad++, для macOS — CotEditor. 

## Как установить

1. Скачиваем проект из репозитория
1. Устанавливаем менеджер управления зависимостями и виртуальным окружением `pipenv`:  
```
$ pip install --user pipenv
```
3. Переходим в папку проекта:  
```
$ cd project_folder
```
4. Запускаем виртуальное окружение:  
```
$ pipenv shell
```
5. Устанавливаем зависимости из файла `requirements.txt`:  
```
pipenv install -r requirements.txt
```
6. В зависимости от того какие фотографии хотим скачать, запускаем желаемый файл, например:  
```
$ fetch_nasa_images.py
```
7. Запускаем файл бота:  
```
$ space_telegram_bot.py
```
