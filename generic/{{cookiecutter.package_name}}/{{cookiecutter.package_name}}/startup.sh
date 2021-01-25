#!/usr/bin/env sh
#   this script is to initialize for the app

cd /app
export LANG="C.UTF-8"
export LC_ALL="C.UTF-8"
export INSIDE_CONTAINER="1"

echo "server {
    listen ${USER_PORT};
    root /usr/share/nginx/html;
    location / {
        uwsgi_read_timeout 600s;
        include uwsgi_params;
        proxy_set_header X-Forwarded-For "\$proxy_add_x_forwarded_for";
        uwsgi_pass unix:///tmp/uwsgi.sock;
    }
}" >> /etc/nginx/conf.d/nginx.conf

chmod -R 777 /data
chmod -R 777 /var/tmp/nginx
chmod -R 777 /app
cd /app

adduser -D www-data -G www-data
/usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
