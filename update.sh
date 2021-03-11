source venv/bin/activate
git pull origin main
python sources/manage.py migrate --settings=giftsBot.prod_settings
python sources/manage.py collectstatic --settings=giftsBot.prod_settings
