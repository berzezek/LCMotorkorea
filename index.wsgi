import os
import sys

sys.path.append('/home/c/cn73530/gotacar/public_html/carshop')
sys.path.append('/home/c/cn73530/gotacar/public_html/venv/lib/python3.6/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'carshop.settings'
import django
django.setup()
 
from django.core.handlers import wsgi
application = wsgi.WSGIHandler()
