from flask import Flask

app = Flask(__name__)  # Holds the Flask instance
app.config['TEMPLATE_AUTO_RELOAD'] = True
app.config['DEBUG'] = True
from api import views