from app import app
from flaskext.mysql import MySQL
import socket

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'webapp'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
localhost = socket.gethostbyname(socket.gethostname())
mysql = MySQL(app)
mysql.init_app(app)
