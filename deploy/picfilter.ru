<VirtualHost 10.1.0.4>
    # Описание сервера
    ServerAdmin admin@wsgi.picfilter.ru
    ServerName wsgi.picfilter.ru

    # Логи
    ErrorLog    /home/django-projects/picfilter/logs/error_log
    CustomLog   /home/django-projects/picfilter/logs/access_log common

    # wsgi-обработчик (см. ниже)
    WSGIScriptAlias / /home/django-projects/picfilter/deploy/django.wsgi
    # Параметры запуска wsgi
    WSGIDaemonProcess dw-site user=dw group=dw home=/home/django-projects/picfilter/media/ \
                      processes=2 threads=4 maximum-requests=100 display-name=apache-dw-wsgi
    WSGIProcessGroup dw-site

    # Статические файлы django-админки
    Alias "/media_admin/" "/usr/lib/python2.5/site-packages/django/contrib/admin/media/"
    <Location "/media_admin/">
        SetHandler None
    </Location>

    # Статические файлы проекта
    Alias "/media/" "/home/django-projects/picfilter/media/"
    <Location "/media/">
        SetHandler None
    </Location>
</VirtualHost>
