pip install -r requirements.txt
set -a
source .env
set +a
python3 manage.py migrate
gunicorn project.wsgi:application --bind 0.0.0.0:8000
