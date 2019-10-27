from flask import Flask, render_template
from logging.handlers import RotatingFileHandler
from logging import StreamHandler, DEBUG, getLogger
from sys import stdout
from app.api import init_api
from app.api.add_namespaces import add_namespaces
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

api, api_bp = init_api('/api')

app.register_blueprint(api_bp)

add_namespaces(api)

app.template_folder = 'app/templates'
app.static_folder = 'app/static'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def vue_app(path):
    return render_template('index.html')

if __name__ == '__main__':
    file_handler = RotatingFileHandler('api.log')
    app.logger.addHandler(file_handler)
    stdout = StreamHandler(stdout)
    stdout.setLevel(DEBUG)
    app.logger.addHandler(stdout)
    app.run()
else:
    gunicorn_logger = getLogger('gunicorn.error')
    app.logger.handler = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
