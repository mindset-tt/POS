from flask import Flask
from flaskext.mysql import MySQL
from sshtunnel import SSHTunnelForwarder
import pymysql
from datetime import timedelta
app = Flask(__name__)
mysql = MySQL()
app.config['SECRET_KEY'] = 'cairocoders-ednalan'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)
tunnel = SSHTunnelForwarder(('47.250.49.41', 22), ssh_password="123456Aa!", ssh_username="root",remote_bind_address=("127.0.0.1", 3306))
tunnel.start()
conp = pymysql.connect(host='127.0.0.1', user="root", passwd="123456Aa!", database="test", port=tunnel.local_bind_port)
mysql.init_app(app)