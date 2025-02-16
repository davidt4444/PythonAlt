
## Setup Dev
### install django
python3 -m pip install django --break-system-packages
### Setup a virtual environment
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
### project setup
django-admin startproject basic_content_service
cd basic_content_service
### create app for posts
// If you created virtual environment, you need to install django in the virtual environment
python3 -m pip install django --break-system-packages
python manage.py startapp posts
### move code over for 
Place your models.py, services.py, and views.py into the posts app directory
create urls.py in posts dir
### install mysqlclient
//debug this
python3 -m pip install mysqlclient --break-system-packages
//If it throws an error, first try to add mysql_client to the .zsh
// for mac
export PATH="/usr/local/mysql/bin:$PATH"

python3 -m pip install mysqlclient --break-system-packages

//If that doesn't work
brew install mysql
brew install pkg-config
brew install mysql-client
brew link --force mysql-client

python3 -m pip install mysqlclient --break-system-packages

//If that doesn't work
add mysql_client to the .zsh
export PATH="/usr/local/opt/mysql-client/bin:$PATH"

python3 -m pip install mysqlclient --break-system-packages

### extra database config
At this point, you may feel tempted to run the sql in gen_code/DJPost.sql 
to create the table in pythonbase. It is actually better to do it after the 
next steps in the migrations, which will handle it for you. 
You just have to put this in your models.py class.
    class Meta:
        db_table = 'posts_DJPost'

Next, install python-dotenv
python3 -m pip install python-dotenv --break-system-packages
 Add this to settings.py in the databases spot
 dotenv_path = os.path.join('../../../aws-resources/', 'localhost-mac.env') 
load_dotenv(dotenv_path=dotenv_path)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME', 'default_db_name'),  # Default name if not set
        'USER': os.getenv('DB_USER', 'default_user'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'default_password'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '3306'),
        'OPTIONS': {
            'charset': 'utf8mb4',
        }
    }
}



### data migrations
python manage.py makemigrations
python manage.py migrate
### create super user
python manage.py createsuperuser
### run the server
python manage.py runserver




