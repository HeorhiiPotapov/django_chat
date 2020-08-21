# django_chat

# how to start local server

copy git repo

    git clone https://github.com/george-potapov13/django_chat.git

navigate to project's folder

    cd django_chat/
    
create python virtualenv

    python3 -m venv env
    
activate virtualenv
    
    source env/bin/activate
    
install required packages from requirements.txt
    
    pip install -r requirements.txt
    
navigate to main project folder
    
    cd chatproject/
    
create database
    
    ./manage.py migrate
    
create to users
    
    ./manage.py createsuperuser --username example --email example@gmail.com
    ./manage.py createsuperuser --username test --email test@gmail.com
    
run redis image in docker (docker must be installed)
    
    sudo docker run -p 6379:6379 -d redis:5
    
to verify the docker image started run:

    $ sudo docker images | grep redis

to start local server and make passible to chat with to different browsers run:

    $ ./manage.py runserver

open 2 different browsers login with username and password and start chatting


to start local server available for all subnet devices(more preffered):
require to add your subnet ip address ('192.168.x.x')
in chatproject/settings.py.ALLOWED_HOSTS variable

    $ ifconfig
    
copy your subnet ip address (it looks like this: '192.168.x.x')

    $ ./manage.py runserver 192.168.x.x:8000

open http://192.168.x.x:8000 on 2 different devices and start sending messages
