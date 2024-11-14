# Ejecuta las migraciones
python manage.py migrate

# Inicia el servidor
gunicorn --bind :${PORT} --workers 4 clinicarobles.wsgi