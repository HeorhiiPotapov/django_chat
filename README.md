# django_chat

Старт проекта

Копирование репозитория:

    git clone https://github.com/george-potapov13/django_chat.git

Навигация в директорию проекта

    cd django_chat/
    
Создание виртуального окружения

    python3 -m venv env
    
Активация окружения
    
    source env/bin/activate
    
Установка зависимостей
    
    pip install -r requirements.txt
    
Навигация в директорию проекта
    
    cd chatproject/
    
Создание базы данных
    
    ./manage.py migrate
    
Создание пользователей
    
    ./manage.py createsuperuser --username example --email example@gmail.com
    ./manage.py createsuperuser --username test --email test@gmail.com
    
Запуск сервера Redis
    
    sudo docker run -p 6379:6379 -d redis:5

Запуск сервера на локальном хосте

    $ ./manage.py runserver

приложение теперь доступно по адрессу http://127.0.0.1:8000/chat

Для того чтобы все устройства из подсети имели доступ к запущенному серверу
узнайте ip устройства в подсети с помощью команды:

    ifconfig
    
ip адресс должен иметь вид '192.168.x.x'
в settings.py проекта добавьте свой ip в переменную ALLOWED_HOSTS в виде '192.168.x.x'

Запуск сервера 

    ./manage.py runserver 192.168.x.x:8000
    
Теперь приложение доступно с любого устройства в подсети по адрессу http://192.168.x.x:8000/chat

# Описание

В этом проекте использованы такие технологии как Django framework, redis (для обработки событий чата), django channels (для работы с websocket)
На данный момент все задачи выполняются синхронно, хотя и django и django_channels позволяют выполнение асинхронных задач, в данном проекте предпочел синхронное выполнение.

# Структура

Для Осуществения возможности просмотра истории сообщений в базе данных созданы 2 модели: модель сообщения и модель комнаты.

Модель сообщания связанна с текущим авторизованым пользователем и комнотой в которой сообщение размещено.
Таким образом Каждая комната хранит только те сообщения которые к ней относятся.

Авторизация Пользователей происходит с помощью стандартной авторизации django, поддержка которой реализована в django_channels.

# Технологии используемые впервые и трудности с которыми столкнулся

Основной трудностью было использование WebSocket, так как раньше с этой технологией не сталкивался.
Потребовалось изучить доккументацию и доступные примеры кода на github.

В общей сложности, вместе с изучением новых для меня технологий, на выполнение было затрачено 22 часа

В процессе создания использовались такие рессурсы:
    https://channels.readthedocs.io/en/latest/introduction.html
    https://medium.com/@ksarthak4ever/django-websockets-and-channels-85b7d5e59dda
    https://realpython.com/getting-started-with-django-channels/
    https://github.com/andrewgodwin/channels-examples
    https://github.com/juanifioren/chat-example-with-channels
    https://github.com/jacobian/channels-example
