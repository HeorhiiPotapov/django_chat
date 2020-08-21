# django_chat

$ source env/bin/activate
$ pip install -r requirements.txt
$ ./manage.py migrate
$ ./manage.py createsuperuser --username example --email example@gmail.com
$ ./manage.py createsuperuser --username test --email test@gmail.com
$ sudo docker run -p 6379:6379 -d redis:5

'''
to verify the docker image started corect run:
    $ sudo docker images | grep redis
'''

to start local server and make passible to chat with to different browsers run:

    $ ./manage.py runserver

open 2 different browsers and start chatting

'''
to start local server available for all subnet devices(more preffered):
require to add your subnet ip address ('192.168.x.x')
in chatproject/settings.py.ALLOWED_HOSTS variable
'''

    $ ./manage.py runserver 192.168.1.4:8000

open http://192.168.1.4:8000 on 2 different devices and start sending messages
