#!/usr/bin/env bash



until cd /home/wsgi/backend/
do
    echo "Waiting for server volume..."
done

until python3 ./manage.py migrate 
do
    echo "Waiting for db to be ready..."
    sleep 2
done

# until python3 ./manage.py migrate --database=portal_db
# do
#     echo "Waiting for db to be ready..."
#     sleep 2
# done

python3 ./manage.py collectstatic --noinput


gunicorn config.wsgi --bind 0.0.0.0:8000 --workers 5 --threads 4 --log-level info --timeout 60 --max-requests 1000 --max-requests-jitter 50

#####################################################################################
# Options to DEBUG Django server
# Optional commands to replace abouve gunicorn command

# Option 1:
# run gunicorn with debug log level
# gunicorn server.wsgi --bind 0.0.0.0:8000 --workers 1 --threads 1 --log-level debug

# Option 2:
# run development server
# DEBUG=True ./manage.py runserver 0.0.0.0:8000