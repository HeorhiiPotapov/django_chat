

# django_chat

    python3 -m venv env
    source env/bin/activate     
    pip install -r requirements.txt
    cd chatproject/      
    ./manage.py migrate 
    ./manage.py createsuperuser --username example --email example@gmail.com
    ./manage.py createsuperuser --username test --email test@gmail.com            
    sudo docker run -p 6379:6379 -d redis:5
    ./manage.py runserver
