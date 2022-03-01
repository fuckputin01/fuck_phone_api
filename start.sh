git pull
source ./../phonesvenv/bin/activate
pip install -r requirements.txt
set -a
source .env
set +a
python3 manage.py migrate
sudo service phones restart
sudo service nginx restart
disconnect
