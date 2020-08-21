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
