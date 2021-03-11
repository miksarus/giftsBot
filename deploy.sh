python -m venv venv --prompt="giftsbot"
source venv/bin/activate
pip install pip --upgrade
pip install -r requirements.txt

python sources/manage.py createsuperuser --settings=giftsBot.prod_settings
python sources/manage.py collectstatic --settings=giftsBot.prod_settings