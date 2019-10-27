import gunicorn
import flask_restplus

bind = '0.0.0.0:8000'
workers = multiprocessing.cpu_count() * 2 + 1
loglevel = 'debug'
keepalive = 10
timeout = 3600
preload_app = True


gunicorn.SERVER_SOFTWARE = 'Microsoft-IIS/6.0'