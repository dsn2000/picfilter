#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import logging
# В python path добавляется директория проекта
#logging.error( "11111" )
dn = os.path.dirname
#sys.path.append('/home/django-projects/')
PROJECT_ROOT = os.path.abspath( dn(dn(__file__)) )
DJANGO_PROJECT_ROOT = os.path.join(PROJECT_ROOT, 'apps')
sys.path.append( PROJECT_ROOT )
logging.error( PROJECT_ROOT )

# Установка файла настроек
os.environ['DJANGO_SETTINGS_MODULE'] = 'apps.settings'

# Запуск wsgi-обработчика
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

