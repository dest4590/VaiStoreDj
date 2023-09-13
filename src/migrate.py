import os

# Make migrations
os.system('python manage.py makemigrations')
os.system('python manage.py migrate')


if input('Create user [y,n]: ') == 'y':
    nickname = input('Enter nickname: ')
    password = input('''Enter password (without " or '): ''')
    
    from django.contrib.auth import get_user_model
    User = get_user_model()
    User.objects.create_superuser(nickname, '', password)